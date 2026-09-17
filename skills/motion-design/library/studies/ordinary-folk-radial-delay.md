# Ordinary Folk — Radial Delay

Updated2026-09-16. This source study covers the full 4.5 s Radial Delay composition, including its initially visible grid, spatially offset shrink/flicker and empty tail. Unlike the delivered-film studies, an original AE project is available and its actual controls are recorded inline.

[Original source](https://www.ordinaryfolk.co/play) · [Browse the library](../../assets/library.html)

## Evidence and limits

Original comp:1500×1500,24 fps,108 frames; personal viewing render:600×600.50 layers include 48 squares,1 controller and 1 background.96 enabled square expressions were inspected. Original source fields are distinct from the independent normalized-distance scheduler. Included terms retain the original project/media outside this repository for personal educational/noncommercial study. Numeric scheduler checks do not establish creative quality.

All intervals have a record. This is complete visual sequence coverage, not access to every original production setting. Observed behavior, original-source settings, local implementation and proposed reconstruction remain separately labeled. Audio mix, sound design and continuous playback preference are outside the completed inspection.

## Coverage and shot inventory

Ranges overlap at transitions and when a focused study sits inside a larger passage. They are analytical units, not an asserted edit-decision list. Counts describe coordinated visible jobs unless original source layers are explicitly available.

| Entry | Source interval | Coordinated details |
| --- | --- | --- |
| [A grid disappears through spatially delayed master curves](../../assets/library.html#RIG-OF-RADIAL/technical) | 0.000–4.500s | 50 original source layers:   1 controller,48 squares,1 background.96 enabled square expressions:   2 per square. Two independent master property curves. |

## Construction notes

Blender is the current preferred implementation route for this workspace. The shared skill also supports AE and explicitly requested generation. These studies require no Seedance credits. Read [native construction guidance](../../references/native-study-construction.md) for interpolation, focus, compositing and lighting alternatives.

Start with the highest-risk handoff, preserve its incoming/outgoing context, and create an editable build. Save the new project, controls and comparison back to the same stable entry. A study being documented does not mark its proposed recreation approved.

## Full technical records

### A grid disappears through spatially delayed master curves

One control rig schedules 48 squares by their distance from an off-center control, with independent shrink and flickering opacity.

[Open clip, timeline and technical view](../../assets/library.html#RIG-OF-RADIAL/technical) · [Machine-readable record](../entries/RIG-OF-RADIAL.json)

**Sequence, timing and attention**

- One control rig schedules 48 squares by their distance from an off-center control, with independent shrink and flickering opacity.
- Times below delimit observed phases, not recovered keyframes. Overlaps are intentional.

Observed event windows — measured-reference

| Source time | Visible event |
| --- | --- |
| 0.000–0.900 s | Grid:48 squares initially visible |
| 0.917–1.833 s | Master scale:100 to 0 |
| 1.000–1.917 s | Master opacity: multiple flicker keys |
| 1.000–3.000 s | Instances:    delayed shrink/fade |
| 3.000–4.500 s | Tail: empty background in late samples |

**Scene structure and component count**

- 50 original source layers:   1 controller,48 squares,1 background.96 enabled square expressions:   2 per square. Two independent master property curves.
- These are visible functional groups or proposed construction objects, not a claim about the original layer count.

Proposed editable hierarchy — proposed

```text
Radial Delay Rig (1500×1500,24fps,4.5s)
  fade [invisible controller; opacity0]
    scale / fader / delay / random sliders
  square-1 … square-48 [Scale + Opacity expressions]
  BG
```

**Camera, movement and interpolation**

- This is a fixed graphic composition. The spatial controller changes per-square sample time rather than moving a camera. Moving the controller changes the distance field; it does not create an automatic outward wave.
- Use separate curves for position, orientation and scale. An intermediate pose should not force a full stop unless the reference visibly pauses. Judge the projected silhouette and screen velocity, not just whether handles are Bézier.

**Lighting, materials and focus**

- Flat outlined squares on a light background. Source evidence does not require a 3 D lighting rig; visual rhythm comes from shape size and opacity.
- Flickering opacity is explicitly authored on the master fader. It should not be confused with motion blur, temporal aliasing or a generic soft fade. Preserve separate master curves when studying the original mechanism.
- Lighting descriptions name the visible treatment and an inferred reconstruction. Original light powers, lens, aperture, shutter and compositing settings are unknown unless explicitly recorded below.

**Construction controls and implementation order**

- Block the incoming and outgoing states first. Establish the main object trajectory, then schedule child actions and reading intervals. Add focus and exposure blur after the trajectory is intelligible. The following controls are a build plan, not measured source settings.

Native construction controls — proposed

| Control / component | Build instruction |
| --- | --- |
| Source delay | 50 in downloaded state; reciprocal distance mapping. |
| Source random | 2 frames at 24 fps gives a nominal±0.083333 s jitter interval. |
| Controller position | [946.23379445076,527.793335050344,0] in source comp pixels. |
| Scale variant | Square 1 multiplies delay by frame duration; other scale expressions and opacity use the raw delay slider. |

**Transitions, failure modes and review**

- Spatial scheduling modulates when each square samples the same master animation; there is no narrative camera handoff.
- Zero distance is singular for reciprocal mapping. An independent reusable rig should define a clamp or alternate normalized mapping explicitly. Do not silently call the source a linear radial wave.
- Review this excerpt with both adjacent joins at normal speed, then diagnose at half speed. Check first-visible frames, accidental stops, silhouette clipping, text readability and outgoing blur. A contact sheet does not establish perceptual smoothness or audio quality.

**Exact original master controls**

- Values below come from the inspected AEP export, not a reconstructed guess. Sliders are unitless source controls; temporal speed is slider-units/second and influence is percent. The two scale-unit variants are preserved as an observed inconsistency.

Master keyframes and temporal ease — original-source

| Property | Frame | Value | In speed | In influence% | Out speed | Out influence% |
| --- | --- | --- | --- | --- | --- | --- |
| /Effects/fader/Slider | 24 | 100 | 0 | 16.666666667 | 0 | 83.2694931407201 |
| /Effects/fader/Slider | 32 | 33.2582244873047 | -236.989191948841 | 35.6434545930588 | -236.98919194884 | 28.0049331548536 |
| /Effects/fader/Slider | 33 | 100 | -154.835104547575 | 39.1788918780795 | -154.835104547575 | 26.745201419972 |
| /Effects/fader/Slider | 36 | 20.834300994873 | -317.063204407599 | 40.5795240748931 | -317.0632044076 | 30.9598192644353 |
| /Effects/fader/Slider | 37 | 55.1837120056152 | -170.614215103672 | 35.7799073119003 | -170.614215103674 | 23.4020642481305 |
| /Effects/fader/Slider | 46 | 0 | 0 | 44.5728922723105 | 0 | 16.666666667 |
| /Effects/scale/Slider | 22 | 100 | 0 | 16.666666667 | 0 | 78.5056703969052 |
| /Effects/scale/Slider | 44 | 0 | 0 | 100 | 0 | 16.666666667 |

**Scheduling math and Blender translation**

- Conceptual paraphrase of the original mechanism: sample the master curve at current time minus a reciprocal-distance offset and stable random offset. Timeless seeded random sampling is used; do not assume changing frame evaluation should change the seed.
- In Blender, calculate each element’s scheduled time, evaluate independently authored master scale/opacity curves at that time, and bake those results. A frame-by-frame bake should also support subframe interpolation for exposure blur.
- The independent module uses bounded normalized inward/outward distance, stable element IDs and seconds. It intentionally differs from the original reciprocal mapping and flicker. Numeric checks have passed; no production shot is approved.

Independent schedule, deliberately different from source — proposed

```text
distance01 = clamp(distance / maximum_distance, 0, 1)
phase = distance01 if direction == "outward" else 1 - distance01
onset = start_seconds + phase * spread_seconds + stable_jitter(id)
local_time = max(0, time_seconds - onset)
scale = authored_scale_curve(local_time)
opacity = authored_opacity_curve(local_time)
# Define center behavior, clamp jitter and preserve an explicit final dwell.
```

**Source terms and reproducibility**

- Original files are retained outside the shared repository for personal educational/noncommercial study under the included terms. Source artwork, project and copied expressions are not distributed with this library.
- The downloaded archive SHA-256 is 2 dfd 5 d 631 f 13 be 9 b 1695 c 97 e 1 c 9 a 7 a 1 c 3 d 4496 afbea 5 ef 86593 d 355958 da 94 a 9. The collection report date 2019-10-21 is not asserted as publication date.
- Inspection used AE 26.5 x 89 and reported no expression errors at inspection time; this is not exhaustive evaluation of all parameter settings.

**Review scope**

Documented reference analysis and native construction plan; no new production render or user acceptance.

- Personal-use source is not a commercial template.
- Numeric checks do not establish visual quality.
- Independent scheduler changes the source mapping; production comparison and user preference remain pending.
