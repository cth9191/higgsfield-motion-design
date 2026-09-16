'use strict';
const catalog = window.MOTION_LIBRARY;
const byId = new Map(catalog.entries.map(item => [item.id, item]));
const studies = new Map(catalog.studies.map(item => [item.id, item]));
const assetState = Object.fromEntries(Object.entries(catalog.assets).map(([key, value]) => [key, {...value, available:false}]));
const cache = new Map();
let currentId = null;
let routeVersion = 0;
let lastOpener = null;
const $ = id => document.getElementById(id);
const human = value => value.replaceAll('-', ' ');
const reviewLabels = {mixed:'Partial feedback', pending:'Review pending', rejected:'Local result rejected', approved:'Approved in stated scope'};

function node(tag, attributes={}, text) {
  const element = document.createElement(tag);
  for (const [key, value] of Object.entries(attributes)) element.setAttribute(key, value);
  if (text !== undefined) element.textContent = text;
  return element;
}
function list(items, ordered=false) {
  const element = node(ordered ? 'ol' : 'ul');
  for (const item of items) element.append(node('li', {}, item));
  return element;
}
function displayValue(value) {
  if (Array.isArray(value)) return value.join(', ');
  if (value !== null && typeof value === 'object') return Object.entries(value).map(([key, item]) => key + ': ' + displayValue(item)).join('\n');
  return String(value);
}
function pauseAll() { document.querySelectorAll('video').forEach(video => video.pause()); }
function assetLink(id) {
  const asset = assetState[id];
  return asset?.available ? node('a', {class:'asset-link', href:asset.url, target:'_blank', rel:'noopener'}, asset.label + ' ↗') :
    node('span', {class:'asset-link unavailable'}, (asset?.label || id) + ' · not connected');
}
function media(container, assetId, title, sourceUrl) {
  container.replaceChildren();
  const fallback = () => {
    const box = node('div', {class:'media-fallback'});
    box.append(node('strong', {}, 'Reference preview'), node('span', {}, 'Local preview not connected. The breakdown remains available.'),
      node('a', {href:sourceUrl, target:'_blank', rel:'noopener noreferrer'}, 'View original source ↗'));
    container.replaceChildren(box);
  };
  const asset = assetState[assetId];
  if (!asset?.available) { fallback(); return; }
  const video = node('video', {controls:'', playsinline:'', preload:'metadata', 'aria-label':title});
  video.muted = true;
  video.src = asset.url;
  video.addEventListener('error', fallback, {once:true});
  video.addEventListener('play', () => document.querySelectorAll('video').forEach(other => { if (other !== video) other.pause(); }));
  container.append(video);
}
function renderCards() {
  pauseAll();
  const terms = ($('search').value.toLowerCase().match(/[\p{L}\p{N}_]+/gu) || []);
  const visible = catalog.entries.filter(item => {
    const text = JSON.stringify(item).toLowerCase().replaceAll('-', ' ').replaceAll('_', ' ');
    return terms.every(term => text.includes(term)) &&
      (!$('video-type').value || item.video_types.includes($('video-type').value)) &&
      (!$('kind').value || item.kind === $('kind').value) &&
      (!$('tool').value || item.tools.includes($('tool').value));
  });
  const grid = $('grid'); grid.replaceChildren();
  for (const item of visible) {
    const card = node('article', {class:'card', 'data-entry':item.id});
    const visual = node('div', {class:'card-media'});
    media(visual, item.preview_asset, item.title + ' reference preview', studies.get(item.study_id).source_url);
    const bottom = node('div', {class:'card-bottom'});
    const link = node('a', {class:'card-link', href:'#' + item.id + '/inspiration'}, 'Explore the breakdown →');
    link.addEventListener('click', () => { lastOpener = link; });
    bottom.append(node('span', {class:'badge ' + item.review_state}, reviewLabels[item.review_state]), link);
    card.append(visual, node('p', {class:'eyebrow'}, studies.get(item.study_id).title + ' / ' + item.kind), node('h2', {}, item.title), node('p', {}, item.summary), bottom);
    grid.append(card);
  }
  $('result-count').textContent = visible.length + (visible.length === 1 ? ' entry' : ' entries');
  $('empty-state').hidden = visible.length !== 0;
}
function selectTab(view, updateUrl=true) {
  for (const name of ['inspiration','technical']) {
    const active = name === view;
    $('tab-' + name).setAttribute('aria-selected', String(active));
    $('tab-' + name).tabIndex = active ? 0 : -1;
    $('panel-' + name).hidden = !active;
  }
  if (updateUrl && currentId) history.replaceState(null, '', '#' + currentId + '/' + view);
}
function renderTimeline(entry) {
  const [first, end] = entry.clip.source_frames;
  const length = end - first, fps = entry.clip.fps;
  const timeline = $('timeline'); timeline.replaceChildren();
  const axis = node('div', {class:'time-axis'}), ticks = node('div', {class:'ticks'});
  for (let i=0;i<=4;i++) ticks.append(node('span', {}, ((first + length*i/4)/fps).toFixed(2) + 's'));
  axis.append(node('span', {class:'track-name'}, 'Global source time'), ticks); timeline.append(axis);
  for (const track of entry.tracks) {
    const row = node('div', {class:'time-row'}), bars = node('div', {class:'track-bars'}), lanes = [];
    for (const event of [...track.events].sort((a,b) => a.frames[0]-b.frames[0])) {
      let lane = lanes.findIndex(last => last <= event.frames[0]);
      if (lane === -1) lane = lanes.length;
      lanes[lane] = event.frames[1];
      const label = `${event.label}: ${(event.frames[0]/fps).toFixed(3)}–${(event.frames[1]/fps).toFixed(3)}s; ${human(event.basis)}`;
      const mark = node('button', {type:'button', class:'event' + (event.basis==='local-implementation' ? ' local' : ''), title:label, 'aria-label':label, 'aria-pressed':'false'}, event.label);
      mark.style.left = ((event.frames[0]-first)/length*100) + '%';
      mark.style.width = ((event.frames[1]-event.frames[0])/length*100) + '%';
      mark.style.top = (lane*36) + 'px';
      mark.addEventListener('click', () => {
        timeline.querySelectorAll('button').forEach(button => button.setAttribute('aria-pressed','false'));
        mark.setAttribute('aria-pressed','true');
        const video = $('detail-media').querySelector('video');
        if (video) { video.pause(); video.currentTime = (event.frames[0]-first)/fps; }
      });
      bars.append(mark);
    }
    bars.style.minHeight = (Math.max(1,lanes.length)*36) + 'px';
    row.append(node('span', {class:'track-name'}, track.label), bars); timeline.append(row);
  }
}
function renderEntry(summary, entry, view) {
  $('entry-review').hidden=false;
  $('entry-title').textContent = summary.title;
  $('entry-kind').textContent = studies.get(summary.study_id).title + ' / ' + summary.kind;
  $('entry-review').className = 'badge ' + summary.review_state;
  $('entry-review').textContent = reviewLabels[summary.review_state];
  media($('detail-media'), entry.clip.asset_id, summary.title + ' source excerpt', studies.get(summary.study_id).source_url);
  const [first,end] = entry.clip.source_frames;
  $('clip-caption').textContent = `${(first/entry.clip.fps).toFixed(3)}–${(end/entry.clip.fps).toFixed(3)}s in source · ${entry.clip.fps}fps · excerpt player starts at 0`;
  $('source-link').href = studies.get(summary.study_id).source_url;
  $('media-note').textContent = entry.clip.note;
  $('meta').replaceChildren();
  for (const item of entry.inspiration.meta) { const box=node('div'); box.append(node('strong',{},item.label),node('p',{},item.value)); $('meta').append(box); }
  const inspiration = $('panel-inspiration'); inspiration.replaceChildren();
  inspiration.append(node('p',{},entry.inspiration.purpose),node('h3',{},'How the shot develops'),list(entry.inspiration.beats,true),node('h3',{},'Where it helps'),list(entry.inspiration.use_when),node('h3',{},'Attention handoff'),node('p',{},entry.inspiration.attention));
  const technical = $('panel-technical'); technical.replaceChildren(node('p',{class:'basis'},entry.technical.basis));
  for (const section of entry.technical.sections) technical.append(node('h3',{},section.title),list(section.items));
  technical.append(node('h3',{},'Recorded controls'));
  const table=node('table',{class:'parameter-table'}), head=node('thead'), header=node('tr');
  for (const text of ['Control','Value / units']) header.append(node('th',{scope:'col'},text));
  head.append(header);table.append(head);const body=node('tbody');
  for (const item of entry.technical.parameters) {
    const row=node('tr'),value=node('td',{class:'parameter-value'},displayValue(item.value));
    value.append(node('small',{},item.unit + ' · ' + human(item.basis)));
    row.append(node('td',{},item.name),value);body.append(row);
  }
  table.append(body);technical.append(table,node('h3',{},'Editable implementation & evidence'));
  for (const item of entry.technical.implementations) {
    const group=node('div',{class:'implementation'}), links=node('div',{class:'asset-links'});
    for (const id of item.asset_ids) links.append(assetLink(id));
    group.append(node('h3',{},item.label),node('p',{class:'small'},item.tool + ' · ' + item.status + ' (see review scope)'),links);technical.append(group);
  }
  $('review-content').replaceChildren(node('p',{},entry.review.scope),list(entry.review.limitations),node('p',{class:'small'},entry.review.date + ' · ' + entry.review.inspection));
  $('evidence').replaceChildren(...entry.evidence_assets.map(assetLink));
  for (const id of entry.evidence_assets) if (assetState[id]?.available && assetState[id].kind==='image') $('review-content').append(node('img',{class:'failure-image',src:assetState[id].url,alt:assetState[id].label,loading:'lazy'}));
  $('related').replaceChildren(...entry.related_ids.map(id => node('a',{href:'#'+id+'/inspiration'},byId.get(id).title + ' →')));
  renderTimeline(entry);selectTab(view,false);
}
async function route() {
  const version = ++routeVersion;
  pauseAll();$('app-error').hidden=true;
  const [id, requestedView] = location.hash.slice(1).split('/');
  const summary = byId.get(id);
  if (!id || !summary) {
    currentId=null;$('browse-view').hidden=false;$('detail-view').hidden=true;
    if (id) {$('app-error').textContent='That entry is not in this library. Choose an available study.';$('app-error').hidden=false;}
    if (lastOpener?.isConnected) lastOpener.focus();
    return;
  }
  currentId=id;$('browse-view').hidden=true;$('detail-view').hidden=false;
  $('entry-title').textContent='Loading the breakdown…';
  $('entry-kind').textContent=studies.get(summary.study_id).title;
  $('entry-review').hidden=true;
  for (const element of ['panel-inspiration','panel-technical','detail-media','meta','timeline','review-content','evidence','related']) $(element).replaceChildren();
  $('clip-caption').textContent='';$('media-note').textContent='';$('source-link').href=studies.get(summary.study_id).source_url;
  try {
    if (!cache.has(id)) {
      const response = await fetch(new URL(summary.detail, new URL('../',location.href)));
      if (!response.ok) throw new Error('Entry could not be loaded.');
      cache.set(id,await response.json());
    }
    if (version !== routeVersion) return;
    renderEntry(summary,cache.get(id),requestedView==='technical' ? 'technical' : 'inspiration');
    $('entry-title').focus({preventScroll:true});
    window.scrollTo(0,0);
  } catch (error) {
    if (version !== routeVersion) return;
    $('entry-title').textContent=summary.title;
    $('app-error').textContent=location.protocol==='file:' ? 'Open this page through the local library viewer to load the breakdowns. See the Library guide below.' : 'The breakdown could not be loaded. Return to the library and try again.';
    $('app-error').hidden=false;
  }
}
for (const [id,field] of [['video-type','video_types'],['tool','tools']]) {
  for (const value of [...new Set(catalog.entries.flatMap(item=>item[field]))].sort()) $(id).append(node('option',{value},human(value)));
}
$('filter-form').addEventListener('submit',event=>event.preventDefault());
for (const id of ['search','video-type','kind','tool']) $(id).addEventListener('input',renderCards);
$('filter-form').addEventListener('reset',()=>setTimeout(renderCards,0));
$('back').addEventListener('click',()=>{location.hash='';});
for (const view of ['inspiration','technical']) {
  $('tab-'+view).addEventListener('click',()=>selectTab(view));
  $('tab-'+view).addEventListener('keydown',event=>{
    if (!['ArrowLeft','ArrowRight','Home','End'].includes(event.key)) return;
    event.preventDefault();const target=event.key==='Home'?'inspiration':event.key==='End'?'technical':view==='inspiration'?'technical':'inspiration';
    selectTab(target);$('tab-'+target).focus();
  });
}
window.addEventListener('hashchange',route);
(async function init(){
  try {const response=await fetch('/api/assets');if(response.ok) Object.assign(assetState,await response.json());} catch {}
  $('catalog-count').textContent=catalog.studies.length+' source '+(catalog.studies.length===1?'study':'studies')+' · '+catalog.entries.length+' connected entries';
  renderCards();await route();
})();
