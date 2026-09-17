# Build the observed motion in an editable scene

Use this with a selected shot record. A film can reveal screen behavior without revealing its creator's renderer, camera focal length or keyframe handles. Keep recovered original settings separate from our native build and proposed controls. Blender builds do not require Higgsfield or Seedance.

## Interpolation that survives a sequence

A spatial Bézier path and a temporal easing curve answer different questions: where an object travels and how quickly it travels there. A smooth path can still stop at every timing key. Use a scalar travel curve to move along a path, with nonzero tangents at intended pass-throughs and a longer controlled arrival. For one isolated settle, the quintic curve `6u^5−15u^4+10u^3` gives zero first/second derivatives at both ends; repeating it between every pose introduces repeated stops. The CR008 camera entry shows exact monotone Hermite timing nodes as an alternative.

Phone orientation needs particular care. Place the pivot at its intended center of mass. Interpolate quaternions along a consistent hemisphere to avoid a long rotation, or unwrap Euler angles intentionally when a complete turn is desired. Keep travel, tilt, roll and size independently timed. Assess projected corner trajectories at the incoming/outgoing joins: technically smooth channels can still yield a rough silhouette or excessive apparent acceleration.

For a perspective object at distance z, projected size is proportional to focal length times object size divided by z. Moving the camera, changing the lens and scaling the object are not interchangeable when other objects at different depths are present. Choose the intended cause of the reframe, then preserve useful parallax. Record lens, sensor fit, camera distance, object dimensions and final screen bounds when a native build is made; do not invent these from a flat reference.

## Three different kinds of softness

1. **Exposure blur:** accumulates motion during an exposure. It depends on screen velocity and shutter duration; rotating phone edges can smear differently from its center. Test at fractional times or with the renderer's motion blur. A proposed diagnostic pair is 90° versus180° shutter at the actual output frame rate, not a universal source setting.
2. **Depth of field:** depends on depth, lens, focus distance and aperture. An outgoing object can remain soft even after it slows if focus has transferred to a different plane. Separate the camera's focus target from its aim target when that helps.
3. **Designed defocus:** a composited blur envelope used to transfer attention. It may be independent of physical depth. Animate it separately from opacity and object movement.

For the rejected Infinex exit, isolate foreground color and alpha with enough overscan, inspect straight versus premultiplied interpretation, blur without exposing a rectangular pass boundary, composite, then apply the intended opacity envelope. As a proposed starting diagnostic for Gaussian blur, pad by at least three standard deviations of the blur kernel, and verify the actual renderer/effect's support because its radius parameter may not be sigma. Never treat this as a verified fix until the comparison render has been inspected.

Render the same short join with: no blur; exposure only; defocus only; intended combination. These are diagnostic views, not four compulsory production variants. Inspect text counters, alpha edges and silhouette at first/last visibility. More blur is not automatically more faithful.

## Independent property timing

Keep a small event table for every object: first visible, dominant travel, readable pose, next event onset and last visible. A four-card fan can use roughly0.1s onset spacing while each card settles much longer. Copy can become opaque before translation settles; outgoing focus can soften before opacity falls. Choose overlap because one event explains the next, then preserve a quieter reading interval.

For character reveals, keep the completed typography layout stable. Use separate glyph transforms, masks or text animators; do not recalculate kerning or line wrapping every frame. Scrambling changes displayed glyphs before they resolve; it is distinct from typing, opacity reveal and motion blur. Mask numeric columns for rolling digits, retain fixed currency symbols, and make the final amount agree with its arc/bar endpoint.

## Lighting environments and alternatives

The Infinex look can be described as a **warm abstract studio environment** or **copper gradient studio**. These are descriptive names, not the name of a verified HDRI. Broad sources and reflective objects create the readable highlights; the background may be a separate gradient or defocused environment pass.

| Treatment | Native setup to try | Where it helps | What to inspect |
| --- | --- | --- | --- |
| Warm copper studio | Broad warm key, restrained rim, low neutral fill, separate orange/copper field | Infinex-like dark product silhouettes | Rim continuity, warm highlights, text contrast |
| High-key white studio | Large soft sources, near-white field, subtle contact/reflection detail | Cero-style bright UI and packages | White-on-white separation; lime clipping |
| Low-key neutral studio | Charcoal field, overhead soft reflection, bright grazing bevels | Bhumimov UI and thin card edges | Black crush; readable text; excessive specular bands |
| Purple/magenta colored studio | Colored areas plus warm emissive beam planes and limited glow | Jaw-style celebratory card hero | Saturation clipping; colored light over copy |
| Cool blue-gray studio | Neutral broad key, blue rim, desaturated field | A calmer technical product interpretation | Device edge contrast; cold skin/footage mismatch |
| Neutral product cyclorama | Curved floor/wall, broad key/fill, controlled shadow | Physically grounded phone or package | Contact and scale cues; unwanted horizon |

Choose one light ratio and reflection layout before animating every light. A moving highlight may come from object rotation, camera movement, an animated light or a composited sweep. Do not animate all four to imitate one visible sweep. Save light dimensions, transforms, energy, color-management settings and material roughness in the implemented record once measured from the actual project.

## Storage and completion

Portable source/shot records, independently authored recipes and this guidance live in the repository. Original video, restricted source projects, fonts, textures, .blend/.aep files, render passes and comparisons stay in the private workspace and are exposed only through explicit local asset bindings. A full breakdown includes uncertainty and known failures. A new native recreation becomes a tested recipe only after an actual render and recorded inspection; user acceptance remains a separate state.
