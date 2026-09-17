# Bhumimov UI film and Blender camera study

Updated2026-09-16. The whole 8.5 s Bhumimov UI reference is mapped into interface assembly, lateral camera sweep, send-control separation and result reveal/exit. The focused CR 008 A/B camera experiment is documented inside the sweep entry, with exact timing nodes and downloadable local evidence.

[Original source](https://x.com/Bhumimov/status/2097367794312675749) · [Browse the library](../../assets/library.html)

## Evidence and limits

Original project, prompt and camera rig remain unknown. Creator reported an Astra workflow; that claim is not independently reproduced by these Blender builds. Local V 01 was rejected for insufficient choreography. V 02 and CR 008 B are editable, rendered and technically checked, with creative preference pending. Source and reconstructed still sequences were inspected; this is not an uninterrupted normal-speed aesthetic review. Native V 02 uses 1-based Blender frames; library clips use 0-based source frames. CR 008 changes locationXYZ only, preserving 283 other curves.

All intervals have a record. This is complete visual sequence coverage, not access to every original production setting. Observed behavior, original-source settings, local implementation and proposed reconstruction remain separately labeled. Audio mix, sound design and continuous playback preference are outside the completed inspection.

## Coverage and shot inventory

Ranges overlap at transitions and when a focused study sits inside a larger passage. They are analytical units, not an asserted edit-decision list. Counts describe coordinated visible jobs unless original source layers are explicitly available.

| Entry | Source interval | Coordinated details |
| --- | --- | --- |
| [01 · A logo lands and builds the prompt interface](../../assets/library.html#SHOT-CAMERA-ASSEMBLY/technical) | 0.000–1.667s | 6 jobs:    logo landing, field growth, heading, typing, three-button stagger, macro transition. |
| [02 · Camera sweeps from the request to Send](../../assets/library.html#SHOT-CAMERA-SWEEP/technical) | 1.333–4.333s | 4 interacting jobs:    camera travel, focus resolve, UI dissolve, button isolation. CR 008 changes exactly 3 location channels;283 other animation curves were verified unchanged. |
| [03 · The send circle releases its arrow](../../assets/library.html#SHOT-CAMERA-SEND/technical) | 3.533–5.500s | 5 jobs:    UI fade, arrow reveal, disc tilt, arrow/disc separation, incoming result. |
| [04 · Result card drops, opens and leaves](../../assets/library.html#SHOT-CAMERA-RESULT/technical) | 5.233–8.500s | 5 jobs:    card drop, card hinge, summary reveal/turn, reading hold, anticipated exit. |

## Construction notes

Blender is the current preferred implementation route for this workspace. The shared skill also supports AE and explicitly requested generation. These studies require no Seedance credits. Read [native construction guidance](../../references/native-study-construction.md) for interpolation, focus, compositing and lighting alternatives.

Start with the highest-risk handoff, preserve its incoming/outgoing context, and create an editable build. Save the new project, controls and comparison back to the same stable entry. A study being documented does not mark its proposed recreation approved.

## Full technical records

### 01 · A logo lands and builds the prompt interface

The interface is constructed in parts around an arriving logo rather than appearing as a finished panel.

[Open clip, timeline and technical view](../../assets/library.html#SHOT-CAMERA-ASSEMBLY/technical) · [Machine-readable record](../entries/SHOT-CAMERA-ASSEMBLY.json)

**Sequence, timing and attention**

- The interface is constructed in parts around an arriving logo rather than appearing as a finished panel.
- Times below delimit observed phases, not recovered keyframes. Overlaps are intentional.

Observed event windows — measured-reference

| Source time | Visible event |
| --- | --- |
| 0.000–0.550 s | Logo: rises and lands large |
| 0.500–1.150 s | Input: grows and levels |
| 0.750–1.350 s | Suggestions:    buttons expand in sequence |
| 0.850–1.550 s | Heading/input: copy resolves |
| 1.530–1.650 s | Transition: rapid oblique macro |

**Scene structure and component count**

- 6 jobs:    logo landing, field growth, heading, typing, three-button stagger, macro transition.
- These are visible functional groups or proposed construction objects, not a claim about the original layer count.

Proposed editable hierarchy — proposed

```text
UI_ROOT > input field / heading groups / typed prefixes
LOGO_ROOT > vector mark
PILLS >3independent groups
SEND_DISC > blank circle
CAMERA / focus target
```

**Camera, movement and interpolation**

- Keep the opening largely frontal. The short transition into macro changes the viewpoint deliberately; it should not become a continuous decorative orbit throughout the opening.
- Use separate curves for position, orientation and scale. An intermediate pose should not force a full stop unless the reference visibly pauses. Judge the projected silhouette and screen velocity, not just whether handles are Bézier.

**Lighting, materials and focus**

- Low-key neutral studio: charcoal field, a broad gray overhead reflection and bright grazing edges. Use large soft sources and bevels; do not raise ambient illumination until dark UI panels lose separation.
- The oblique macro enters very soft and resolves into its focus plane. The logo and UI arrival need their own opacity groups; integer-valued opacity previously caused snapping and was corrected to a float.
- Lighting descriptions name the visible treatment and an inferred reconstruction. Original light powers, lens, aperture, shutter and compositing settings are unknown unless explicitly recorded below.

**Construction controls and implementation order**

- Block the incoming and outgoing states first. Establish the main object trajectory, then schedule child actions and reading intervals. Add focus and exposure blur after the trajectory is intelligible. The following controls are a build plan, not measured source settings.

Native construction controls — proposed

| Control / component | Build instruction |
| --- | --- |
| Logo | Author a landing with a small settle and scale reduction into header position. |
| Field | Expand horizontally from a small extent with a short overshoot. |
| Suggestions | Three button groups with distinct start times and common final scale. |

**Transitions, failure modes and review**

- The fully formed interface is the same object seen in the oblique macro.
- A single finished UI panel scaling up was the rejected V 01 behavior. The component order is the essential construction.
- Review this excerpt with both adjacent joins at normal speed, then diagnose at half speed. Check first-visible frames, accidental stops, silhouette clipping, text readability and outgoing blur. A contact sheet does not establish perceptual smoothness or audio quality.

**Existing local V02 controls**

- These are our authored reconstruction controls, not recovered Bhumimov settings. Full construction script and native scene are attached. Times use t=(BlenderFrame−1)/30. Baked keys use linear interpolation between authored samples.

Authored V02 values — local-implementation

| Component | Time/value relationship |
| --- | --- |
| Logo Y, scene units | 0 s:   -4.7;0.18:-0.3;0.33:0.12;0.48:-0.1;0.8:-0.6;1.18:2.2 |
| Logo scale | 0 s:   3.2;0.3:3;0.68:1.6;0.88:1.2;1.2:1.05 |
| Pill onset | Deep research 0.76 s;Create an image 0.90 s;Look something up 1.02 s |
| Pill scale | onset:0.001;onset+0.17 s:   1.08;onset+0.31 s:   1 |
| Field extent | 0.53 s:   0.001;0.66:0.58;0.84:1.10;1.13:1 |

**Review scope**

Source observations plus existing local V02 construction. V01 was rejected; V02 is technically rendered, not user-approved.

- Original source rig and curves unavailable.
- V01 was rejected for missing the reference choreography.
- Typography, perspective, shading and timing differences remain; technical validation does not establish fidelity.

### 02 · Camera sweeps from the request to Send

An oblique close-up resolves focus, then a lateral sweep moves attention along the request toward the circular send control.

[Open clip, timeline and technical view](../../assets/library.html#SHOT-CAMERA-SWEEP/technical) · [Machine-readable record](../entries/SHOT-CAMERA-SWEEP.json)

**Sequence, timing and attention**

- An oblique close-up resolves focus, then a lateral sweep moves attention along the request toward the circular send control.
- Times below delimit observed phases, not recovered keyframes. Overlaps are intentional.

Observed event windows — measured-reference

| Source time | Visible event |
| --- | --- |
| 1.533–1.600 s | Macro: short viewpoint transition |
| 1.600–2.200 s | Focus:    settles onto request |
| 2.200–3.200 s | Travel: lateral movement toward circle |
| 3.200–3.600 s | Arrival: send button favored |
| 3.550–4.333 s | Handoff: interface dissolves around button |

**Scene structure and component count**

- 4 interacting jobs:    camera travel, focus resolve, UI dissolve, button isolation. CR 008 changes exactly 3 location channels;283 other animation curves were verified unchanged.
- These are visible functional groups or proposed construction objects, not a claim about the original layer count.

Proposed editable hierarchy — proposed

```text
SCENE
  UI_ROOT > request / heading / pills
  SEND_ROOT > disc / arrow
  CAMERA > locationXYZ / orientation / lens / DOF
  FOCUS_TARGET
CR008_B changes only camera locationXYZ
```

**Camera, movement and interpolation**

- The local B study preserves the original V 02 path and changes its travel timing only. Monotone cubic Hermite interpolation defines scalar progress; interior control points are pass-throughs. This differs from easing every segment independently to zero velocity.
- Use separate curves for position, orientation and scale. An intermediate pose should not force a full stop unless the reference visibly pauses. Judge the projected silhouette and screen velocity, not just whether handles are Bézier.

**Lighting, materials and focus**

- Low-key neutral studio: charcoal field, a broad gray overhead reflection and bright grazing edges. Use large soft sources and bevels; do not raise ambient illumination until dark UI panels lose separation.
- The reference shows stronger sweep blur than the local comparison. B holds aperture, lens, focus and shutter unchanged to isolate camera-location timing. It does not fix the reference mismatch in blur or perspective.
- Lighting descriptions name the visible treatment and an inferred reconstruction. Original light powers, lens, aperture, shutter and compositing settings are unknown unless explicitly recorded below.

**Construction controls and implementation order**

- Block the incoming and outgoing states first. Establish the main object trajectory, then schedule child actions and reading intervals. Add focus and exposure blur after the trajectory is intelligible. The following controls are a build plan, not measured source settings.

Native construction controls — proposed

| Control / component | Build instruction |
| --- | --- |
| Path | Sample the original monotonic-X camera polyline between source scene frames 67 and 92. |
| Progress | Normalize X travel, evaluate new scalar timing, then interpolate along the saved polyline. |
| Bake | Modify only camera location at Blender frames 68–96; preserve other channels. |
| Review | Compare normal-speed A/B first, then reference/B; no winning version selected. |

**Transitions, failure modes and review**

- The circle holds attention while the rest of the interface disappears.
- A mathematical continuity check does not prove a pleasing projected path. B arrives five rendered frames later, so inspect whether it weakens the button handoff.
- Review this excerpt with both adjacent joins at normal speed, then diagnose at half speed. Check first-visible frames, accidental stops, silhouette clipping, text readability and outgoing blur. A contact sheet does not establish perceptual smoothness or audio quality.

**Exact CR008 B timing and preservation**

- B uses t=(sceneFrame−1)/30; the library excerpt uses zero-based source frames 40–129. Both denote 1.3333–4.3333 s.
- The original path is resampled by normalized X, not constant arc length. Interior tangents are weighted harmonic means of neighboring secants; endpoint slopes are zero. The result is baked at 30 fps with linear interpolation between samples.

Hermite segment used for travel — local-implementation

```text
u = (t - t0) / (t1 - t0)
h = t1 - t0
p = (2*u**3 - 3*u**2 + 1)*p0 \
  + (u**3 - 2*u**2 + u)*h*m0 \
  + (-2*u**3 + 3*u**2)*p1 \
  + (u**3 - u**2)*h*m1
# Sample the preserved camera polyline using p.
# Tangents at interior nodes are nonzero unless a monotonicity break requires zero.
```

B travel nodes — local-implementation

| Time(s) | Progress(0–1) | Slope(1/s) |
| --- | --- | --- |
| 2.2 | 0.0 | 0.0 |
| 2.4 | 0.04 | 0.37842778793418685 |
| 2.533333333333333 | 0.27 | 1.9240384615384623 |
| 2.6666666666666665 | 0.56 | 1.8280155642023328 |
| 2.8333333333333335 | 0.82 | 1.0462042742887114 |
| 3.033333333333333 | 0.975 | 0.24630818619582656 |
| 3.2 | 1.0 | 0.0 |

**A/B controls, render and limits**

- A retains the V 02 symmetric quintic travel around 2.333–3.030 s. B begins gradual pickup at 2.2 s and finishes at 3.2 s. No overshoot or new shake.
- Both previews are 960×476,30 fps,90 frames. Existing render times:   A 42.35 s,B 41.97 s; diagnostic stills 4.46 s. These are render timings, not total labor.
- Original V 02 hash, location values outside the edit interval and 283 non-location animation curves were verified unchanged. B was built in Blender 5.1.2.

**Review scope**

One rendered camera-timing comparison; visual preference pending. Source blur, typography and perspective differences remain.

- Exact original scene hierarchy and easing are unavailable.
- Approximate event windows are not exact cut boundaries unless explicitly stated.
- Proposed rig has not been rendered or compared here.

### 03 · The send circle releases its arrow

The circular control survives the interface dissolve, then arrow and disc separate to launch the result.

[Open clip, timeline and technical view](../../assets/library.html#SHOT-CAMERA-SEND/technical) · [Machine-readable record](../entries/SHOT-CAMERA-SEND.json)

**Sequence, timing and attention**

- The circular control survives the interface dissolve, then arrow and disc separate to launch the result.
- Times below delimit observed phases, not recovered keyframes. Overlaps are intentional.

Observed event windows — measured-reference

| Source time | Visible event |
| --- | --- |
| 3.550–4.000 s | Interface: disappears around circle |
| 3.500–3.950 s | Arrow: becomes visible |
| 4.000–5.020 s | Button: subtle tilt and held focus |
| 5.020–5.400 s | Separation: arrow up; disc down |
| 5.250–5.500 s | Result: card enters from above |

**Scene structure and component count**

- 5 jobs:    UI fade, arrow reveal, disc tilt, arrow/disc separation, incoming result.
- These are visible functional groups or proposed construction objects, not a claim about the original layer count.

Proposed editable hierarchy — proposed

```text
SEND_ROOT > disc / rim
ARROW > separate mesh and opacity
UI_FADE
RESULT_CARD_NEXT
CAMERA_RESET hidden by sparse composition
```

**Camera, movement and interpolation**

- Preserve the send circle’s projected center/diameter while the camera resets behind the sparse composition. The arrow must be a child with an independent translation so its launch can separate from the disc.
- Use separate curves for position, orientation and scale. An intermediate pose should not force a full stop unless the reference visibly pauses. Judge the projected silhouette and screen velocity, not just whether handles are Bézier.

**Lighting, materials and focus**

- Low-key neutral studio: charcoal field, a broad gray overhead reflection and bright grazing edges. Use large soft sources and bevels; do not raise ambient illumination until dark UI panels lose separation.
- The local V 02 final pass disabled exposure across the hidden camera reset to prevent a ghost trail. Blur from a discontinuous camera reset should not contaminate the stable button.
- Lighting descriptions name the visible treatment and an inferred reconstruction. Original light powers, lens, aperture, shutter and compositing settings are unknown unless explicitly recorded below.

**Construction controls and implementation order**

- Block the incoming and outgoing states first. Establish the main object trajectory, then schedule child actions and reading intervals. Add focus and exposure blur after the trajectory is intelligible. The following controls are a build plan, not measured source settings.

Native construction controls — proposed

| Control / component | Build instruction |
| --- | --- |
| Button | Match its screen-space pose across the camera change. |
| Arrow | Animate local Y separately from parent; use its own alpha. |
| Disc | Retain a visible material edge, then fade during its downward departure. |

**Transitions, failure modes and review**

- The launched arrow and departing disc overlap the full-size card descending from above.
- An early arrow or generic button pulse was a V 01 mismatch. The controlled separation, not a uniform shrink, drives the result reveal.
- Review this excerpt with both adjacent joins at normal speed, then diagnose at half speed. Check first-visible frames, accidental stops, silhouette clipping, text readability and outgoing blur. A contact sheet does not establish perceptual smoothness or audio quality.

**Existing local V02 controls**

- These are our authored reconstruction controls, not recovered Bhumimov settings. Full construction script and native scene are attached. Times use t=(BlenderFrame−1)/30. Baked keys use linear interpolation between authored samples.

Authored V02 values — local-implementation

| Component | Time/value relationship |
| --- | --- |
| UI opacity | 1−ease(t,3.55,3.99) |
| Arrow opacity | ease(t,3.5,3.90)×(1−ease(t,5.24,5.38)) |
| Arrow localY | 5.02 s:   0;5.20:0.8;5.32:4.2;5.40:9 |
| Disc opacity | 1−ease(t,5.25,5.4) |
| Opacity type | Floating-point custom property; integer property previously snapped |

**Review scope**

Source observations plus existing local V02 construction. V01 was rejected; V02 is technically rendered, not user-approved.

- Original source rig and curves unavailable.
- V01 was rejected for missing the reference choreography.
- Typography, perspective, shading and timing differences remain; technical validation does not establish fidelity.

### 04 · Result card drops, opens and leaves

A full-sized result card descends from above, hinges aside for a summary, then anticipates an upward exit.

[Open clip, timeline and technical view](../../assets/library.html#SHOT-CAMERA-RESULT/technical) · [Machine-readable record](../entries/SHOT-CAMERA-RESULT.json)

**Sequence, timing and attention**

- A full-sized result card descends from above, hinges aside for a summary, then anticipates an upward exit.
- Times below delimit observed phases, not recovered keyframes. Overlaps are intentional.

Observed event windows — measured-reference

| Source time | Visible event |
| --- | --- |
| 5.230–6.100 s | Card: descends and settles |
| 6.040–6.950 s | Summary: arrives as card hinges |
| 6.950–7.170 s | Read: result pair holds |
| 7.170–7.600 s | Anticipation: group dips |
| 7.600–8.500 s | Exit: group accelerates upward |

**Scene structure and component count**

- 5 jobs:    card drop, card hinge, summary reveal/turn, reading hold, anticipated exit.
- These are visible functional groups or proposed construction objects, not a claim about the original layer count.

Proposed editable hierarchy — proposed

```text
RESULT_ROOT > global anticipation/exit
  CARD_ROOT > match card / flags / labels
  SUMMARY_ROOT > editable text plane / opacity
CAMERA
```

**Camera, movement and interpolation**

- Use opposing Y rotations for card and summary to make room without losing their relationship. Keep the card near full size on entry; a small panel scaling from below was a rejected approximation. Exit anticipation and upward acceleration share one parent root.
- Use separate curves for position, orientation and scale. An intermediate pose should not force a full stop unless the reference visibly pauses. Judge the projected silhouette and screen velocity, not just whether handles are Bézier.

**Lighting, materials and focus**

- Low-key neutral studio: charcoal field, a broad gray overhead reflection and bright grazing edges. Use large soft sources and bevels; do not raise ambient illumination until dark UI panels lose separation.
- Keep text sharp during the paired reading pose and allow motion softness during the rapid exit. Broad soft reflections should define card curvature without creating a bright highlight over match details.
- Lighting descriptions name the visible treatment and an inferred reconstruction. Original light powers, lens, aperture, shutter and compositing settings are unknown unless explicitly recorded below.

**Construction controls and implementation order**

- Block the incoming and outgoing states first. Establish the main object trajectory, then schedule child actions and reading intervals. Add focus and exposure blur after the trajectory is intelligible. The following controls are a build plan, not measured source settings.

Native construction controls — proposed

| Control / component | Build instruction |
| --- | --- |
| Drop | Author a fast early descent with a longer final settle, then freeze the vertical landing before hinge movement dominates. |
| Hinge | Card turns one way; summary turns the other. Parent both to the exit root. |
| Summary | Separate opacity from position and rotation so it becomes readable while still settling. |
| Exit | Brief negativeY anticipation, then accelerating positiveY travel; preserve baseline relationship. |

**Transitions, failure modes and review**

- Both result components leave together under one root, completing the 8.5 s sequence.
- A continuous slow upward drift omits the anticipation. Do not change the sports facts for a commercial video without checking current content; here they are only source-study artwork.
- Review this excerpt with both adjacent joins at normal speed, then diagnose at half speed. Check first-visible frames, accidental stops, silhouette clipping, text readability and outgoing blur. A contact sheet does not establish perceptual smoothness or audio quality.

**Existing local V02 controls**

- These are our authored reconstruction controls, not recovered Bhumimov settings. Full construction script and native scene are attached. Times use t=(BlenderFrame−1)/30. Baked keys use linear interpolation between authored samples.

Authored V02 values — local-implementation

| Component | Time/value relationship |
| --- | --- |
| Card dropY | 5.23 s:   16;5.30:8.4;5.367:4.1;5.5:2.35;5.8:1.1;6.10:0.05 |
| Card hinge | 6.1–6.95 s;X 0→−3.3 scene units;Y rotation 0→25 deg;scale 1.37→1.12 |
| Summary | 6.08–6.93 s;X 13.5→6.2;Y rotation 0→−22 deg;opacity 6.04–6.35 s |
| Exit rootY | 7.17 s:   0;7.43:−0.68;7.6:−0.53;7.8:0;8.0:1.8;8.167:5.7;8.33:12;8.5:18 |

**Review scope**

Source observations plus existing local V02 construction. V01 was rejected; V02 is technically rendered, not user-approved.

- Original source rig and curves unavailable.
- V01 was rejected for missing the reference choreography.
- Typography, perspective, shading and timing differences remain; technical validation does not establish fidelity.
