# Cero launch film

Updated2026-09-16. The complete Cero launch film alternates reward/UI explanations with direct point-of-sale footage edits. Every interval is covered, including all three two-shot payment montages, the final cafe shot, circular mosaic, promise and wordmark.

[Original source](https://x.com/joinCero/status/2087953404190466515) · [Browse the library](../../assets/library.html)

## Evidence and limits

Source:1920×1080,60 fps,2087 decoded video frames. Publication metadata:2026-08-13. Source creator/agency and production software are unverified. Four existing dense passages were inspected at 12 samples/second; this expansion adds labeled 0.5 s overview frames across the entire film. Boundaries outside the dense passages are approximate, generally within 0.5 s. Footage provenance and sound were not audited. New build plans are unrendered.

All intervals have a record. This is complete visual sequence coverage, not access to every original production setting. Observed behavior, original-source settings, local implementation and proposed reconstruction remain separately labeled. Audio mix, sound design and continuous playback preference are outside the completed inspection.

## Coverage and shot inventory

Ranges overlap at transitions and when a focused study sits inside a larger passage. They are analytical units, not an asserted edit-decision list. Counts describe coordinated visible jobs unless original source layers are explicitly available.

| Entry | Source interval | Coordinated details |
| --- | --- | --- |
| [01 · A tossed coin becomes a reward](../../assets/library.html#SHOT-CERO-TOSS/technical) | 0.000–4.400s | 6 jobs:    hand/plate action, coin flight, scene replacement, phone arrival, ribbon, transaction-value change. One coin becomes the reward focus. |
| [02 · Two payment contexts](../../assets/library.html#SHOT-CERO-PAYMENTS-A/technical) | 4.350–5.950s | 3 jobs per insert: hand/phone action, terminal contact, screen content. Two footage shots. |
| [03 · A sentence introduces the pack](../../assets/library.html#SHOT-CERO-PACK-COPY/technical) | 5.900–8.450s | 5 jobs:    phrase changes, pack appearance, wrapper detail, confetti burst, phone pickup. Three text units. |
| [04 · A pack leaves the phone and reveals prizes](../../assets/library.html#SHOT-CERO-PACK-PRIZES/technical) | 8.200–11.450s | 6 jobs:    phone rise, phone tilt, pack release/spin, prize spread, rays, ticket takeover. At least five visible prize classes; exact particle count unmeasured. |
| [05 · Jackpot type becomes a score screen](../../assets/library.html#SHOT-CERO-JACKPOT/technical) | 11.350–13.950s | 5 jobs:    digit assembly, dimensional light, rays, phone framing, score/arc fill. |
| [06 · Cafe and grocery payment inserts](../../assets/library.html#SHOT-CERO-PAYMENTS-B/technical) | 13.900–15.300s | Two footage shots; 3 visual dependencies each: hand, phone UI, payment terminal. |
| [07 · Salary notification becomes a multiplier wheel](../../assets/library.html#SHOT-CERO-SALARY/technical) | 15.250–19.350s | 6 jobs:    notification, wheel arrival, rotation, pointer/result, amount roll, framing. One wheel with repeated sectors. |
| [08 · Grocery and cinema proof beats](../../assets/library.html#SHOT-CERO-PAYMENTS-C/technical) | 19.250–20.400s | Two footage shots; foreground props, phone and counter action are separate visible groups. |
| [09 · Inputs assemble into a score, then a phone](../../assets/library.html#SHOT-CERO-SCORE/technical) | 20.350–24.850s | 7 jobs:    solo factor changes, icon arcs, increments, wide assembly, score roll, arc fill, phone docking. Six factors in the aggregate. |
| [10 · A credit panel leaves its UI slot and returns](../../assets/library.html#SHOT-CERO-CREDIT/technical) | 24.750–26.950s | 6 jobs:    panel projection, material sweep, lock change, docking, value roll, bar fill. |
| [11 · One purchase expands into many](../../assets/library.html#SHOT-CERO-MOSAIC/technical) | 26.850–30.500s | 4 jobs:    payment action, circular masking, tile multiplication, field reframe/exit. Four initial windows; later count varies with cropping. |
| [12 · Coin, promise and wordmark](../../assets/library.html#SHOT-CERO-END/technical) | 30.350–34.783s | 4 jobs:    coin presentation, promise reveal, glyph/color resolve, final hold. |

## Construction notes

Blender is the current preferred implementation route for this workspace. The shared skill also supports AE and explicitly requested generation. These studies require no Seedance credits. Read [native construction guidance](../../references/native-study-construction.md) for interpolation, focus, compositing and lighting alternatives.

Start with the highest-risk handoff, preserve its incoming/outgoing context, and create an editable build. Save the new project, controls and comparison back to the same stable entry. A study being documented does not mark its proposed recreation approved.

## Full technical records

### 01 · A tossed coin becomes a reward

A first-person coin toss supplies an object that carries the film from everyday footage into product UI.

[Open clip, timeline and technical view](../../assets/library.html#SHOT-CERO-TOSS/technical) · [Machine-readable record](../entries/SHOT-CERO-TOSS.json)

**Sequence, timing and attention**

- A first-person coin toss supplies an object that carries the film from everyday footage into product UI.
- Times below delimit observed phases, not recovered keyframes. Overlaps are intentional.

Observed event windows — measured-reference

| Source time | Visible event |
| --- | --- |
| 0.000–0.600 s | Hand: releases coin |
| 0.500–1.800 s | Coin: travels upward through street view |
| 1.800–2.500 s | Handoff: coin grows into graphic stage |
| 2.500–3.250 s | UI: phone and 100% reward resolve |
| 3.250–4.400 s | Detail: push to transaction; value becomes free |

**Scene structure and component count**

- 6 jobs:    hand/plate action, coin flight, scene replacement, phone arrival, ribbon, transaction-value change. One coin becomes the reward focus.
- These are visible functional groups or proposed construction objects, not a claim about the original layer count.

Proposed editable hierarchy — proposed

```text
FOOTAGE_PLATE > street / hand
COIN_ROOT > mesh / two face marks
PHONE_ROOT > frame / screen / reward
RIBBON > rear and front segments
TRANSACTION > logo / amount / free badge
```

**Camera, movement and interpolation**

- The toss uses large apparent depth change. Track coin center, projected diameter and face orientation at the plate-to-UI handoff. Once in UI, push toward the transaction row; preserve the coin as the reward badge rather than spawning an unrelated disc.
- Use separate curves for position, orientation and scale. An intermediate pose should not force a full stop unless the reference visibly pauses. Judge the projected silhouette and screen velocity, not just whether handles are Bézier.

**Lighting, materials and focus**

- High-key white studio treatment. Use a near-white background, large soft area lights, restrained contact shadow and a narrow edge reflection for dark product rims. Keep lime or accent emissions from washing out white UI text.
- Motion blur belongs to the rotating/translating coin; the phone UI is selectively softened behind the reward. Keep the highlighted transaction clear. A background blur can be composited separately from exposure blur.
- Lighting descriptions name the visible treatment and an inferred reconstruction. Original light powers, lens, aperture, shutter and compositing settings are unknown unless explicitly recorded below.

**Construction controls and implementation order**

- Block the incoming and outgoing states first. Establish the main object trajectory, then schedule child actions and reading intervals. Add focus and exposure blur after the trajectory is intelligible. The following controls are a build plan, not measured source settings.

Native construction controls — proposed

| Control / component | Build instruction |
| --- | --- |
| Plate preparation | Use owned or licensed live footage; solve or manually track the coin trajectory in screen space. |
| Identity handoff | Match center/diameter/rotation across plate and dimensional coin before replacing the background. |
| Ribbon | Use a curve with bevel or flat strip mesh, with correct front/back occlusion around the phone. |
| Amount | Keep amount text separately editable; mask rolling or replacing digits inside the row. |

**Transitions, failure modes and review**

- The transaction close-up makes the benefit legible before real-world tap-to-pay footage returns.
- A coin that teleports to the center or changes diameter at the graphic handoff breaks the connection. Live-action capture is a separate dependency; a pure Blender substitute changes the style.
- Review this excerpt with both adjacent joins at normal speed, then diagnose at half speed. Check first-visible frames, accidental stops, silhouette clipping, text readability and outgoing blur. A contact sheet does not establish perceptual smoothness or audio quality.

**Review scope**

Documented reference analysis and native construction plan; no new production render or user acceptance.

- Exact original scene hierarchy and easing are unavailable.
- Approximate event windows are not exact cut boundaries unless explicitly stated.
- Proposed rig has not been rendered or compared here.

### 02 · Two payment contexts

Two first-person payment shots ground the graphic reward in recognizable everyday behavior.

[Open clip, timeline and technical view](../../assets/library.html#SHOT-CERO-PAYMENTS-A/technical) · [Machine-readable record](../entries/SHOT-CERO-PAYMENTS-A.json)

**Sequence, timing and attention**

- Two first-person payment shots ground the graphic reward in recognizable everyday behavior.
- Times below delimit observed phases, not recovered keyframes. Overlaps are intentional.

Observed event windows — measured-reference

| Source time | Visible event |
| --- | --- |
| 4.350–5.150 s | Footage 1: food-counter terminal and phone |
| 5.150–5.950 s | Footage 2: outdoor/waterpark payment |

**Scene structure and component count**

- 3 jobs per insert: hand/phone action, terminal contact, screen content. Two footage shots.
- These are visible functional groups or proposed construction objects, not a claim about the original layer count.

Proposed editable hierarchy — proposed

```text
EDIT
  food-counter plate > tracked screen insert if required
  outdoor-counter plate > tracked screen insert if required
COLOR_MATCH
AUDIO_CONTACTS (not audited)
```

**Camera, movement and interpolation**

- Keep the point of view close to the user’s hand. Match the phone/terminal action rather than trying to force an unbroken virtual camera between locations.
- Use separate curves for position, orientation and scale. An intermediate pose should not force a full stop unless the reference visibly pauses. Judge the projected silhouette and screen velocity, not just whether handles are Bézier.

**Lighting, materials and focus**

- Natural daylight and practical environment lighting in supplied footage; a studio light rig alone cannot reproduce it. For a Blender alternative, rebuild the payment interaction with stylized props and accept a different visual treatment.
- Preserve plate shutter characteristics when adding a screen insert. Track corner pin plus occlusion by fingers; use local grain/softness matching rather than a blanket Gaussian blur.
- Lighting descriptions name the visible treatment and an inferred reconstruction. Original light powers, lens, aperture, shutter and compositing settings are unknown unless explicitly recorded below.

**Construction controls and implementation order**

- Block the incoming and outgoing states first. Establish the main object trajectory, then schedule child actions and reading intervals. Add focus and exposure blur after the trajectory is intelligible. The following controls are a build plan, not measured source settings.

Native construction controls — proposed

| Control / component | Build instruction |
| --- | --- |
| Coverage | Two distinct environments and edits; source tool chain and footage provenance unknown. |
| Screen insert | Planar tracking plus hand holdout, matched exposure and perspective. |
| Cut timing | Keep tap action and product screen recognizable within each short shot. |

**Transitions, failure modes and review**

- A direct change to white typography starts the pack explanation.
- Do not describe this as a continuous camera transition. Replacing the footage with generic product floats removes the everyday-use proof.
- Review this excerpt with both adjacent joins at normal speed, then diagnose at half speed. Check first-visible frames, accidental stops, silhouette clipping, text readability and outgoing blur. A contact sheet does not establish perceptual smoothness or audio quality.

**Review scope**

Documented reference analysis and native construction plan; no new production render or user acceptance.

- Exact original scene hierarchy and easing are unavailable.
- Approximate event windows are not exact cut boundaries unless explicitly stated.
- Proposed rig has not been rendered or compared here.

### 03 · A sentence introduces the pack

Short serif statements and a lime package connect spending to a playful reward.

[Open clip, timeline and technical view](../../assets/library.html#SHOT-CERO-PACK-COPY/technical) · [Machine-readable record](../entries/SHOT-CERO-PACK-COPY.json)

**Sequence, timing and attention**

- Short serif statements and a lime package connect spending to a playful reward.
- Times below delimit observed phases, not recovered keyframes. Overlaps are intentional.

Observed event windows — measured-reference

| Source time | Visible event |
| --- | --- |
| 5.900–6.300 s | Copy: I just |
| 6.300–7.200 s | Pack/copy: opened the packs |
| 7.200–8.200 s | Confetti: for the upside |
| 8.200–8.450 s | Next: phone begins entering |

**Scene structure and component count**

- 5 jobs:    phrase changes, pack appearance, wrapper detail, confetti burst, phone pickup. Three text units.
- These are visible functional groups or proposed construction objects, not a claim about the original layer count.

Proposed editable hierarchy — proposed

```text
COPY > short line / pack line / upside line
PACK_ROOT > wrapper / folded strip
CONFETTI > instanced colored planes
PHONE_NEXT
```

**Camera, movement and interpolation**

- Use deliberate changes of framing and type size. The pack sits beside and overlaps the sentence; keep its silhouette from blocking the important words during the readable interval.
- Use separate curves for position, orientation and scale. An intermediate pose should not force a full stop unless the reference visibly pauses. Judge the projected silhouette and screen velocity, not just whether handles are Bézier.

**Lighting, materials and focus**

- High-key white studio treatment. Use a near-white background, large soft area lights, restrained contact shadow and a narrow edge reflection for dark product rims. Keep lime or accent emissions from washing out white UI text.
- Confetti has depth spread and edge-of-frame cropping; a few near-camera pieces can soften while central copy stays sharp. Do not assign every particle identical blur or rotation.
- Lighting descriptions name the visible treatment and an inferred reconstruction. Original light powers, lens, aperture, shutter and compositing settings are unknown unless explicitly recorded below.

**Construction controls and implementation order**

- Block the incoming and outgoing states first. Establish the main object trajectory, then schedule child actions and reading intervals. Add focus and exposure blur after the trajectory is intelligible. The following controls are a build plan, not measured source settings.

Native construction controls — proposed

| Control / component | Build instruction |
| --- | --- |
| Typography | Separate sentence units with fixed final baselines; animate reveal and global framing independently. |
| Pack | Use a thin beveled/deformed wrapper mesh with serrated ends; parent brand texture to geometry. |
| Confetti | Instance planes with deterministic seeds, varied depth and rotations; animate travel away from center. |

**Transitions, failure modes and review**

- The next phone rises while the celebration clears; the pack reappears inside its UI.
- An equal-duration three-card slideshow would discard the asymmetric visual development. Avoid confetti over the center reading zone.
- Review this excerpt with both adjacent joins at normal speed, then diagnose at half speed. Check first-visible frames, accidental stops, silhouette clipping, text readability and outgoing blur. A contact sheet does not establish perceptual smoothness or audio quality.

**Review scope**

Documented reference analysis and native construction plan; no new production render or user acceptance.

- Exact original scene hierarchy and easing are unavailable.
- Approximate event windows are not exact cut boundaries unless explicitly stated.
- Proposed rig has not been rendered or compared here.

### 04 · A pack leaves the phone and reveals prizes

The reward pack escapes its screen, becomes a dimensional hero, and opens a field of prizes before yielding to a ticket.

[Open clip, timeline and technical view](../../assets/library.html#SHOT-CERO-PACK-PRIZES/technical) · [Machine-readable record](../entries/SHOT-CERO-PACK-PRIZES.json)

**Sequence, timing and attention**

- The reward pack escapes its screen, becomes a dimensional hero, and opens a field of prizes before yielding to a ticket.
- Times below delimit observed phases, not recovered keyframes. Overlaps are intentional.

Observed event windows — measured-reference

| Source time | Visible event |
| --- | --- |
| 8.200–8.900 s | Phone: rises with pack in screen |
| 8.850–9.500 s | Separation: phone tips away; pack remains |
| 9.500–10.050 s | Pack: rotation reveals thin profile |
| 9.900–10.700 s | Prizes:    fan around package |
| 10.700–11.450 s | Ticket: crosses foreground into jackpot |

**Scene structure and component count**

- 6 jobs:    phone rise, phone tilt, pack release/spin, prize spread, rays, ticket takeover. At least five visible prize classes; exact particle count unmeasured.
- These are visible functional groups or proposed construction objects, not a claim about the original layer count.

Proposed editable hierarchy — proposed

```text
PHONE_ROOT > shell / screen / PACK_ANCHOR
PACK_ROOT (reparent using world transform) > wrapper / logo
PRIZES > car / ball / watch / electronics / banknotes
RAYS > radial wedges
TICKET_ROOT
```

**Camera, movement and interpolation**

- Preserve the pack’s world-space pose when it separates from the phone. Let phone pitch, pack rotation and prize spread overlap with different settles. Keep the central package recognizable through the thin orientation.
- Use separate curves for position, orientation and scale. An intermediate pose should not force a full stop unless the reference visibly pauses. Judge the projected silhouette and screen velocity, not just whether handles are Bézier.

**Lighting, materials and focus**

- High-key white studio treatment. Use a near-white background, large soft area lights, restrained contact shadow and a narrow edge reflection for dark product rims. Keep lime or accent emissions from washing out white UI text.
- The pack’s fast spin can receive exposure blur while the surrounding prizes settle at different speeds. Layer the radial rays behind the objects. Keep ticket edges crisp enough to communicate a physical card.
- Lighting descriptions name the visible treatment and an inferred reconstruction. Original light powers, lens, aperture, shutter and compositing settings are unknown unless explicitly recorded below.

**Construction controls and implementation order**

- Block the incoming and outgoing states first. Establish the main object trajectory, then schedule child actions and reading intervals. Add focus and exposure blur after the trajectory is intelligible. The following controls are a build plan, not measured source settings.

Native construction controls — proposed

| Control / component | Build instruction |
| --- | --- |
| Detachment | Bake or constrain the package to the screen first; release without a world-position jump. |
| Pack geometry | Provide front/back and crimped thickness, not one double-sided flat plane with impossible edges. |
| Prize spread | Give each class its own radial slot, rotation and delay; maintain depth ordering. |
| Ticket | Animate a new foreground plane through the prize field, with amount as editable text. |

**Transitions, failure modes and review**

- The foreground ticket transfers its amount into the dimensional jackpot claim.
- If the phone fades before the pack has separated, the causal link is lost. Identical spring settings for car, paper money and pack remove differences in weight.
- Review this excerpt with both adjacent joins at normal speed, then diagnose at half speed. Check first-visible frames, accidental stops, silhouette clipping, text readability and outgoing blur. A contact sheet does not establish perceptual smoothness or audio quality.

**Review scope**

Documented reference analysis and native construction plan; no new production render or user acceptance.

- Exact original scene hierarchy and easing are unavailable.
- Approximate event windows are not exact cut boundaries unless explicitly stated.
- Proposed rig has not been rendered or compared here.

### 05 · Jackpot type becomes a score screen

A large dimensional amount receives a brief hero moment before the phone score becomes the next focus.

[Open clip, timeline and technical view](../../assets/library.html#SHOT-CERO-JACKPOT/technical) · [Machine-readable record](../entries/SHOT-CERO-JACKPOT.json)

**Sequence, timing and attention**

- A large dimensional amount receives a brief hero moment before the phone score becomes the next focus.
- Times below delimit observed phases, not recovered keyframes. Overlaps are intentional.

Observed event windows — measured-reference

| Source time | Visible event |
| --- | --- |
| 11.350–11.900 s | Amount: separated digits converge |
| 11.900–12.650 s | Read: jackpot holds over rays |
| 12.650–13.200 s | Phone: enters as amount clears |
| 13.100–13.950 s | Score: number and arc increase |

**Scene structure and component count**

- 5 jobs:    digit assembly, dimensional light, rays, phone framing, score/arc fill.
- These are visible functional groups or proposed construction objects, not a claim about the original layer count.

Proposed editable hierarchy — proposed

```text
JACKPOT > label / individually extruded digits
RAYS
PHONE > score arc / digit display / UI panels
```

**Camera, movement and interpolation**

- Control the amount as a full text group with individual digit offsets, then let the phone replace its visual weight. The score rise is a separate action from phone framing.
- Use separate curves for position, orientation and scale. An intermediate pose should not force a full stop unless the reference visibly pauses. Judge the projected silhouette and screen velocity, not just whether handles are Bézier.

**Lighting, materials and focus**

- High-key white studio treatment. Use a near-white background, large soft area lights, restrained contact shadow and a narrow edge reflection for dark product rims. Keep lime or accent emissions from washing out white UI text.
- Dimensional letters need soft highlight gradients and dark side faces for depth. Blur should fall during the amount hold; keep the phone score sharp as it becomes the focal content.
- Lighting descriptions name the visible treatment and an inferred reconstruction. Original light powers, lens, aperture, shutter and compositing settings are unknown unless explicitly recorded below.

**Construction controls and implementation order**

- Block the incoming and outgoing states first. Establish the main object trajectory, then schedule child actions and reading intervals. Add focus and exposure blur after the trajectory is intelligible. The following controls are a build plan, not measured source settings.

Native construction controls — proposed

| Control / component | Build instruction |
| --- | --- |
| Amount | Separate digits for rolling/settling; use consistent bevel and extrusion depth. |
| Rays | Radial wedges parented behind the hero, with independent intensity. |
| Score arc | Repeated ticks with a progress mask or per-tick material threshold. |
| Score digits | Use masked columns or explicit number updates; synchronize endpoint with arc, not necessarily all intermediate rates. |

**Transitions, failure modes and review**

- The score screen cuts back to payment footage after its feature reveal.
- A flat lime text plane loses the dimensional amount. A score that jumps to its final value before the arc fills feels disconnected.
- Review this excerpt with both adjacent joins at normal speed, then diagnose at half speed. Check first-visible frames, accidental stops, silhouette clipping, text readability and outgoing blur. A contact sheet does not establish perceptual smoothness or audio quality.

**Review scope**

Documented reference analysis and native construction plan; no new production render or user acceptance.

- Exact original scene hierarchy and easing are unavailable.
- Approximate event windows are not exact cut boundaries unless explicitly stated.
- Proposed rig has not been rendered or compared here.

### 06 · Cafe and grocery payment inserts

Two quick payment inserts reinforce the repeated everyday action between reward explanations.

[Open clip, timeline and technical view](../../assets/library.html#SHOT-CERO-PAYMENTS-B/technical) · [Machine-readable record](../entries/SHOT-CERO-PAYMENTS-B.json)

**Sequence, timing and attention**

- Two quick payment inserts reinforce the repeated everyday action between reward explanations.
- Times below delimit observed phases, not recovered keyframes. Overlaps are intentional.

Observed event windows — measured-reference

| Source time | Visible event |
| --- | --- |
| 13.900–14.350 s | Footage 1: cafe counter |
| 14.350–15.300 s | Footage 2: grocery terminal |

**Scene structure and component count**

- Two footage shots; 3 visual dependencies each: hand, phone UI, payment terminal.
- These are visible functional groups or proposed construction objects, not a claim about the original layer count.

Proposed editable hierarchy — proposed

```text
EDIT > cafe plate / grocery plate
SCREEN_INSERTS > tracked UI
GRADE > scene-specific exposure
```

**Camera, movement and interpolation**

- The handheld first-person framing gives the payment action continuity across different counters; retain distinct environments and direct edits.
- Use separate curves for position, orientation and scale. An intermediate pose should not force a full stop unless the reference visibly pauses. Judge the projected silhouette and screen velocity, not just whether handles are Bézier.

**Lighting, materials and focus**

- Practical interior lighting differs between cafe and grocery store. Match each plate locally; keep phone screen emission plausible in that exposure.
- Screen inserts need movement blur, hand occlusion and perspective matching. Original footage generation/capture method remains unverified.
- Lighting descriptions name the visible treatment and an inferred reconstruction. Original light powers, lens, aperture, shutter and compositing settings are unknown unless explicitly recorded below.

**Construction controls and implementation order**

- Block the incoming and outgoing states first. Establish the main object trajectory, then schedule child actions and reading intervals. Add focus and exposure blur after the trajectory is intelligible. The following controls are a build plan, not measured source settings.

Native construction controls — proposed

| Control / component | Build instruction |
| --- | --- |
| Track | Use phone surface corners and hand holdouts. |
| Edit | Select a readable screen/contact moment in each short insert. |
| Blender alternative | A stylized countertop/tap action can carry the same story but is not a literal footage recreation. |

**Transitions, failure modes and review**

- A macro phone notification starts the salary/reward chapter.
- A graphic transition added between every insert may slow the montage. Preserve the directness of these proof beats.
- Review this excerpt with both adjacent joins at normal speed, then diagnose at half speed. Check first-visible frames, accidental stops, silhouette clipping, text readability and outgoing blur. A contact sheet does not establish perceptual smoothness or audio quality.

**Review scope**

Documented reference analysis and native construction plan; no new production render or user acceptance.

- Exact original scene hierarchy and easing are unavailable.
- Approximate event windows are not exact cut boundaries unless explicitly stated.
- Proposed rig has not been rendered or compared here.

### 07 · Salary notification becomes a multiplier wheel

An incoming salary notification becomes a wheel whose result changes the displayed amount.

[Open clip, timeline and technical view](../../assets/library.html#SHOT-CERO-SALARY/technical) · [Machine-readable record](../entries/SHOT-CERO-SALARY.json)

**Sequence, timing and attention**

- An incoming salary notification becomes a wheel whose result changes the displayed amount.
- Times below delimit observed phases, not recovered keyframes. Overlaps are intentional.

Observed event windows — measured-reference

| Source time | Visible event |
| --- | --- |
| 15.250–16.200 s | Notification: salary message on macro phone |
| 16.200–17.100 s | Wheel: enters large and resolves |
| 17.100–17.750 s | Wheel: readable 2 x result |
| 17.750–19.100 s | Amount: rolls from 3200 toward 6400 |
| 19.100–19.350 s | Join: return to payment context |

**Scene structure and component count**

- 6 jobs:    notification, wheel arrival, rotation, pointer/result, amount roll, framing. One wheel with repeated sectors.
- These are visible functional groups or proposed construction objects, not a claim about the original layer count.

Proposed editable hierarchy — proposed

```text
PHONE_MACRO > rounded shell / lockscreen / notification
WHEEL_ROOT > segments / rim nodes / pointer / result label
SALARY_CENTER > label / masked number columns
CAMERA
```

**Camera, movement and interpolation**

- Move from a tightly cropped phone to a large wheel, then vary framing around its center. Keep the pointer’s coordinate system independent of the rotating segment group so the selected result is legible.
- Use separate curves for position, orientation and scale. An intermediate pose should not force a full stop unless the reference visibly pauses. Judge the projected silhouette and screen velocity, not just whether handles are Bézier.

**Lighting, materials and focus**

- High-key white studio treatment. Use a near-white background, large soft area lights, restrained contact shadow and a narrow edge reflection for dark product rims. Keep lime or accent emissions from washing out white UI text.
- The wheel can be soft during fast rotation but must resolve before the multiplier/result read. Mask digit columns within the center disc; do not blur the complete amount panel to fake rolling numbers.
- Lighting descriptions name the visible treatment and an inferred reconstruction. Original light powers, lens, aperture, shutter and compositing settings are unknown unless explicitly recorded below.

**Construction controls and implementation order**

- Block the incoming and outgoing states first. Establish the main object trajectory, then schedule child actions and reading intervals. Add focus and exposure blur after the trajectory is intelligible. The following controls are a build plan, not measured source settings.

Native construction controls — proposed

| Control / component | Build instruction |
| --- | --- |
| Wheel | Build radial colored sectors and a fixed pointer. Key total rotation as one continuous value. |
| Amount | Animate masked digit columns with delayed carries and a stable currency symbol. |
| Scale | Author wheel scale/framing separately from rotation; use a quieter result interval. |
| Content | Source amounts are visual study content, not financial claims to reuse. |

**Transitions, failure modes and review**

- Another pair of real-world purchases separates the salary mechanic from the score explanation.
- A random spin with a sudden end snap weakens the result. The multiplier must agree with the final displayed amount.
- Review this excerpt with both adjacent joins at normal speed, then diagnose at half speed. Check first-visible frames, accidental stops, silhouette clipping, text readability and outgoing blur. A contact sheet does not establish perceptual smoothness or audio quality.

**Review scope**

Documented reference analysis and native construction plan; no new production render or user acceptance.

- Exact original scene hierarchy and easing are unavailable.
- Approximate event windows are not exact cut boundaries unless explicitly stated.
- Proposed rig has not been rendered or compared here.

### 08 · Grocery and cinema proof beats

Two short point-of-sale shots keep the second reward mechanic connected to spending.

[Open clip, timeline and technical view](../../assets/library.html#SHOT-CERO-PAYMENTS-C/technical) · [Machine-readable record](../entries/SHOT-CERO-PAYMENTS-C.json)

**Sequence, timing and attention**

- Two short point-of-sale shots keep the second reward mechanic connected to spending.
- Times below delimit observed phases, not recovered keyframes. Overlaps are intentional.

Observed event windows — measured-reference

| Source time | Visible event |
| --- | --- |
| 19.250–19.850 s | Footage 1: grocery bags and terminal |
| 19.850–20.400 s | Footage 2: cinema popcorn payment |

**Scene structure and component count**

- Two footage shots; foreground props, phone and counter action are separate visible groups.
- These are visible functional groups or proposed construction objects, not a claim about the original layer count.

Proposed editable hierarchy — proposed

```text
EDIT > grocery-bag plate / cinema plate
PHONE_SCREEN_INSERT > perspective / hand matte
COLOR
```

**Camera, movement and interpolation**

- Maintain first-person phone presentation, then cut to a different context rather than animating every background change.
- Use separate curves for position, orientation and scale. An intermediate pose should not force a full stop unless the reference visibly pauses. Judge the projected silhouette and screen velocity, not just whether handles are Bézier.

**Lighting, materials and focus**

- Natural shop lighting and warmer cinema practicals; preserve local exposure and contrast.
- Retain natural plate motion softness and screen readability at the contact beat; do not apply a graphic defocus transition over the entire payment action.
- Lighting descriptions name the visible treatment and an inferred reconstruction. Original light powers, lens, aperture, shutter and compositing settings are unknown unless explicitly recorded below.

**Construction controls and implementation order**

- Block the incoming and outgoing states first. Establish the main object trajectory, then schedule child actions and reading intervals. Add focus and exposure blur after the trajectory is intelligible. The following controls are a build plan, not measured source settings.

Native construction controls — proposed

| Control / component | Build instruction |
| --- | --- |
| Phone insert | Track per shot; do not reuse a transform from the previous environment. |
| Foreground | Keep bags/popcorn as recognisable context props. |
| Timing | Prioritize the readable payment gesture in the brief windows. |

**Transitions, failure modes and review**

- The montage yields to a clean icon-and-label score explanation.
- Calling the montage one continuous shot would misdescribe the source. Exact source cut frames need a dedicated every-frame boundary check.
- Review this excerpt with both adjacent joins at normal speed, then diagnose at half speed. Check first-visible frames, accidental stops, silhouette clipping, text readability and outgoing blur. A contact sheet does not establish perceptual smoothness or audio quality.

**Review scope**

Documented reference analysis and native construction plan; no new production render or user acceptance.

- Exact original scene hierarchy and easing are unavailable.
- Approximate event windows are not exact cut boundaries unless explicitly stated.
- Proposed rig has not been rendered or compared here.

### 09 · Inputs assemble into a score, then a phone

Individual score factors are explained, then arranged around an aggregate score that returns to the product screen.

[Open clip, timeline and technical view](../../assets/library.html#SHOT-CERO-SCORE/technical) · [Machine-readable record](../entries/SHOT-CERO-SCORE.json)

**Sequence, timing and attention**

- Individual score factors are explained, then arranged around an aggregate score that returns to the product screen.
- Times below delimit observed phases, not recovered keyframes. Overlaps are intentional.

Observed event windows — measured-reference

| Source time | Visible event |
| --- | --- |
| 20.350–21.050 s | Factor 1: Cash held |
| 21.050–21.600 s | Factor 2: On-chain Wallets |
| 21.600–22.150 s | Factor 3: Bank accounts |
| 22.150–22.650 s | Factor 4: Socials |
| 22.650–23.700 s | Aggregate: six factors around rolling 1000 |
| 23.700–24.850 s | Dock: diagram reduces into phone |

**Scene structure and component count**

- 7 jobs:    solo factor changes, icon arcs, increments, wide assembly, score roll, arc fill, phone docking. Six factors in the aggregate.
- These are visible functional groups or proposed construction objects, not a claim about the original layer count.

Proposed editable hierarchy — proposed

```text
FACTORS > icon / arc / label / description / increment badge
SCORE_ROOT > radial ticks / masked digit columns
DIAGRAM_ROOT
PHONE_ROOT > shell / UI anchor for score
```

**Camera, movement and interpolation**

- The first four featured factors are replaced in one central explanatory slot, then the wide diagram includes six factors. Reconstruct the score-to-phone move by keeping the score geometry persistent and changing its parent transform into the UI slot.
- Use separate curves for position, orientation and scale. An intermediate pose should not force a full stop unless the reference visibly pauses. Judge the projected silhouette and screen velocity, not just whether handles are Bézier.

**Lighting, materials and focus**

- High-key white studio treatment. Use a near-white background, large soft area lights, restrained contact shadow and a narrow edge reflection for dark product rims. Keep lime or accent emissions from washing out white UI text.
- Digits roll inside masks while tick progress changes independently. The diagram-to-phone move benefits from controlled depth softness on peripherals, while the central 1000 remains recognizable.
- Lighting descriptions name the visible treatment and an inferred reconstruction. Original light powers, lens, aperture, shutter and compositing settings are unknown unless explicitly recorded below.

**Construction controls and implementation order**

- Block the incoming and outgoing states first. Establish the main object trajectory, then schedule child actions and reading intervals. Add focus and exposure blur after the trajectory is intelligible. The following controls are a build plan, not measured source settings.

Native construction controls — proposed

| Control / component | Build instruction |
| --- | --- |
| Factor modules | Six reusable modules; first four get solo attention. Preserve icon color mapping. |
| Increment badges | Animate independently of arc fill; do not copy financial values into a new product without its real data. |
| Aggregate | Use six spatial slots around the same arc and one central number group. |
| Docking | Match the projected arc bounds with its final phone screen location before completing the handoff. |

**Transitions, failure modes and review**

- The docked score leaves the credit panel in position for a foreground explanation.
- Replacing the diagram with an unrelated static phone screenshot loses object identity. Digit and tick endings should agree even when their interior timing differs.
- Review this excerpt with both adjacent joins at normal speed, then diagnose at half speed. Check first-visible frames, accidental stops, silhouette clipping, text readability and outgoing blur. A contact sheet does not establish perceptual smoothness or audio quality.

**Review scope**

Documented reference analysis and native construction plan; no new production render or user acceptance.

- Exact original scene hierarchy and easing are unavailable.
- Approximate event windows are not exact cut boundaries unless explicitly stated.
- Proposed rig has not been rendered or compared here.

### 10 · A credit panel leaves its UI slot and returns

A locked panel moves beyond the phone boundary, changes state in the foreground, then docks with a readable value.

[Open clip, timeline and technical view](../../assets/library.html#SHOT-CERO-CREDIT/technical) · [Machine-readable record](../entries/SHOT-CERO-CREDIT.json)

**Sequence, timing and attention**

- A locked panel moves beyond the phone boundary, changes state in the foreground, then docks with a readable value.
- Times below delimit observed phases, not recovered keyframes. Overlaps are intentional.

Observed event windows — measured-reference

| Source time | Visible event |
| --- | --- |
| 24.750–25.250 s | Panel: projects outside phone |
| 25.150–25.600 s | Unlock: gray becomes lime |
| 25.600–26.000 s | Dock: panel returns to interface |
| 25.900–26.750 s | Values:    amount and bar fill |
| 26.750–26.950 s | Cut: live payment resumes |

**Scene structure and component count**

- 6 jobs:    panel projection, material sweep, lock change, docking, value roll, bar fill.
- These are visible functional groups or proposed construction objects, not a claim about the original layer count.

Proposed editable hierarchy — proposed

```text
PHONE_ROOT > shell / base UI / PANEL_SLOT
CREDIT_PANEL > rounded body / title / lock / value / fill bar
RAYS > rear layer
```

**Camera, movement and interpolation**

- Keep the panel as a single persistent object with expanded and docked transforms. It should overlap the phone edges while expanded, then align exactly to the screen slot. Do not scale the whole phone to simulate panel projection.
- Use separate curves for position, orientation and scale. An intermediate pose should not force a full stop unless the reference visibly pauses. Judge the projected silhouette and screen velocity, not just whether handles are Bézier.

**Lighting, materials and focus**

- High-key white studio treatment. Use a near-white background, large soft area lights, restrained contact shadow and a narrow edge reflection for dark product rims. Keep lime or accent emissions from washing out white UI text.
- A soft lime material/glow change spreads across the panel while it moves. Keep the lock symbol sharp enough to read. Blur does not substitute for the material transition.
- Lighting descriptions name the visible treatment and an inferred reconstruction. Original light powers, lens, aperture, shutter and compositing settings are unknown unless explicitly recorded below.

**Construction controls and implementation order**

- Block the incoming and outgoing states first. Establish the main object trajectory, then schedule child actions and reading intervals. Add focus and exposure blur after the trajectory is intelligible. The following controls are a build plan, not measured source settings.

Native construction controls — proposed

| Control / component | Build instruction |
| --- | --- |
| Expanded state | Increase panel width and depth independently from its height; preserve corner proportions. |
| Material change | Animate a gradient/mask from gray to lime, and switch the lock state at the focal moment. |
| Docked state | Match slot center, bounds and depth before swapping from 3 D to flatUI if needed. |
| Values | Reveal amount and progress after the state change, with an explicit final readable interval. |

**Transitions, failure modes and review**

- Panel explanation completes before the next payment insert.
- The panel must not shrink its text during docking so far that the readable value arrives prematurely. A pure dissolve cannot explain the expansion.
- Review this excerpt with both adjacent joins at normal speed, then diagnose at half speed. Check first-visible frames, accidental stops, silhouette clipping, text readability and outgoing blur. A contact sheet does not establish perceptual smoothness or audio quality.

**Review scope**

Documented reference analysis and native construction plan; no new production render or user acceptance.

- Exact original scene hierarchy and easing are unavailable.
- Approximate event windows are not exact cut boundaries unless explicitly stated.
- Proposed rig has not been rendered or compared here.

### 11 · One purchase expands into many

A last payment shot becomes a circular tile, then a field of repeated purchase moments.

[Open clip, timeline and technical view](../../assets/library.html#SHOT-CERO-MOSAIC/technical) · [Machine-readable record](../entries/SHOT-CERO-MOSAIC.json)

**Sequence, timing and attention**

- A last payment shot becomes a circular tile, then a field of repeated purchase moments.
- Times below delimit observed phases, not recovered keyframes. Overlaps are intentional.

Observed event windows — measured-reference

| Source time | Visible event |
| --- | --- |
| 26.850–27.800 s | Footage: cafe payment close-up |
| 27.800–28.450 s | Mask: four circular purchase windows |
| 28.450–30.150 s | Field: circles multiply and fill frame |
| 30.150–30.500 s | Clear: mosaic yields to brand coin |

**Scene structure and component count**

- 4 jobs:    payment action, circular masking, tile multiplication, field reframe/exit. Four initial windows; later count varies with cropping.
- These are visible functional groups or proposed construction objects, not a claim about the original layer count.

Proposed editable hierarchy — proposed

```text
FOOTAGE_LIBRARY > earlier payment excerpts
TILE_ROOT > circular masks / independent plate crops
FIELD_ROOT > grid positions / scale / pan
COIN_NEXT
```

**Camera, movement and interpolation**

- Separate the movement inside each footage crop from the tile’s movement through the field. Use the layout root for the large reframe and per-tile transforms for staggered arrivals.
- Use separate curves for position, orientation and scale. An intermediate pose should not force a full stop unless the reference visibly pauses. Judge the projected silhouette and screen velocity, not just whether handles are Bézier.

**Lighting, materials and focus**

- White negative space connects the footage circles to the graphic chapters. Preserve each plate’s lighting inside its mask, then grade the collection for similar exposure.
- Use clean antialiased circular mattes; do not blur tile boundaries as a substitute for antialiasing. Fast moving tiles can get exposure blur if their contents remain identifiable.
- Lighting descriptions name the visible treatment and an inferred reconstruction. Original light powers, lens, aperture, shutter and compositing settings are unknown unless explicitly recorded below.

**Construction controls and implementation order**

- Block the incoming and outgoing states first. Establish the main object trajectory, then schedule child actions and reading intervals. Add focus and exposure blur after the trajectory is intelligible. The following controls are a build plan, not measured source settings.

Native construction controls — proposed

| Control / component | Build instruction |
| --- | --- |
| Masks | Clip each source shot into its own circle; anchor crops to the phone/hand action. |
| Layout | Start with four visible circles, then expand to a denser repeated field. |
| Variation | Offset footage playback times and crops; avoid accidentally showing the exact same frame in every tile. |

**Transitions, failure modes and review**

- The many purchase moments resolve to the familiar lime brand coin.
- The source has a changing tile count; record four at the initial cluster, not a fabricated fixed count for the whole mosaic.
- Review this excerpt with both adjacent joins at normal speed, then diagnose at half speed. Check first-visible frames, accidental stops, silhouette clipping, text readability and outgoing blur. A contact sheet does not establish perceptual smoothness or audio quality.

**Review scope**

Documented reference analysis and native construction plan; no new production render or user acceptance.

- Exact original scene hierarchy and easing are unavailable.
- Approximate event windows are not exact cut boundaries unless explicitly stated.
- Proposed rig has not been rendered or compared here.

### 12 · Coin, promise and wordmark

A quiet three-step closing moves from the brand coin to a plain-language promise and final wordmark.

[Open clip, timeline and technical view](../../assets/library.html#SHOT-CERO-END/technical) · [Machine-readable record](../entries/SHOT-CERO-END.json)

**Sequence, timing and attention**

- A quiet three-step closing moves from the brand coin to a plain-language promise and final wordmark.
- Times below delimit observed phases, not recovered keyframes. Overlaps are intentional.

Observed event windows — measured-reference

| Source time | Visible event |
| --- | --- |
| 30.350–31.050 s | Coin: central brand mark |
| 31.050–32.200 s | Promise: The upside of spending |
| 32.200–32.950 s | Wordmark: letters/colors resolve |
| 32.950–34.783 s | Hold: settled brand |

**Scene structure and component count**

- 4 jobs:    coin presentation, promise reveal, glyph/color resolve, final hold.
- These are visible functional groups or proposed construction objects, not a claim about the original layer count.

Proposed editable hierarchy — proposed

```text
COIN_ROOT
PROMISE > full line
WORDMARK > individually controlled glyphs
RAYS / WHITE_FIELD
```

**Camera, movement and interpolation**

- Reduce motion density as the film ends. The wordmark’s letter/color resolution is short; hold the completed logo rather than continuing a decorative orbit.
- Use separate curves for position, orientation and scale. An intermediate pose should not force a full stop unless the reference visibly pauses. Judge the projected silhouette and screen velocity, not just whether handles are Bézier.

**Lighting, materials and focus**

- High-key white studio treatment. Use a near-white background, large soft area lights, restrained contact shadow and a narrow edge reflection for dark product rims. Keep lime or accent emissions from washing out white UI text.
- Any transition softness resolves before the final hold. Keep the clean serif wordmark edge intact and avoid bloom that changes letter counters.
- Lighting descriptions name the visible treatment and an inferred reconstruction. Original light powers, lens, aperture, shutter and compositing settings are unknown unless explicitly recorded below.

**Construction controls and implementation order**

- Block the incoming and outgoing states first. Establish the main object trajectory, then schedule child actions and reading intervals. Add focus and exposure blur after the trajectory is intelligible. The following controls are a build plan, not measured source settings.

Native construction controls — proposed

| Control / component | Build instruction |
| --- | --- |
| Wordmark | Use accurate vector geometry and baseline alignment; animate selected glyphs rather than distorting the entire logo. |
| Promise | Keep a stable final line and brief readable interval. |
| Tail | Retain the end hold through frame 2086. |

**Transitions, failure modes and review**

- The film ends on a stable brand against white.
- Do not rush the settled wordmark to make all three closing beats equal duration. Source branding is study material, not an asset for an unrelated client.
- Review this excerpt with both adjacent joins at normal speed, then diagnose at half speed. Check first-visible frames, accidental stops, silhouette clipping, text readability and outgoing blur. A contact sheet does not establish perceptual smoothness or audio quality.

**Review scope**

Documented reference analysis and native construction plan; no new production render or user acceptance.

- Exact original scene hierarchy and easing are unavailable.
- Approximate event windows are not exact cut boundaries unless explicitly stated.
- Proposed rig has not been rendered or compared here.
