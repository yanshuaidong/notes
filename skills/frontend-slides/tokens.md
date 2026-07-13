# Design Tokens — Warm Paper Editorial

## Color palette

| Token          | Value                         | Use                                 |
|----------------|-------------------------------|-------------------------------------|
| `--bg`         | `#F4E8C8`                     | Page & slide background             |
| `--surface`    | `rgba(255,252,242,0.68)`      | Card, table, code bg                |
| `--surface-s`  | `rgba(255,252,242,0.86)`      | Nav buttons, stronger surface       |
| `--text`       | `#171512`                     | Headings, bold text                 |
| `--text-2`     | `#3A342B`                     | Body / paragraph text               |
| `--text-m`     | `rgba(58,52,43,0.62)`         | Captions, labels, counters          |
| `--green`      | `#4E6750`                     | Accent: subtitle, badge, link       |
| `--green-l`    | `rgba(78,103,80,0.13)`        | Table header bg, muted fill         |
| `--gold`       | `#C28E2D`                     | Accent: quote border, dot-active    |
| `--gold-l`     | `rgba(226,187,112,0.24)`      | Hover glow, light fill              |
| `--rose`       | `#A8463E`                     | Warning / "before" state            |
| `--border`     | `rgba(93,67,33,0.16)`         | All card/table borders              |
| `--border-s`   | `rgba(93,67,33,0.28)`         | Emphasis border                     |

## Shadows

| Token         | Value                                    |
|---------------|------------------------------------------|
| `--shadow`    | `0 18px 24px rgba(68,54,28,0.08)`        |
| `--shadow-md` | `0 20px 34px rgba(68,54,28,0.12)`        |
| `--shadow-sm` | `0 8px 18px rgba(68,54,28,0.06)`         |

## Radii

| Token    | Value  |
|----------|--------|
| `--r`    | `12px` |
| `--r-lg` | `16px` |

## Typography

| Element      | Font                              | Size clamp            | Weight | Leading |
|--------------|-----------------------------------|-----------------------|--------|---------|
| Hero title   | Georgia / 'Songti SC' (serif)     | clamp(52px,6vw,84px)  | 500    | 1.06    |
| H2 title     | Georgia / 'Songti SC' (serif)     | clamp(36px,4vw,54px)  | 500    | 1.12    |
| Subtitle     | system sans                       | 18px                  | 600    | 1.7     |
| Badge/kicker | system sans, ALL CAPS             | 12px, letter-spacing:3px | 700 | —    |
| Body         | system sans                       | 15–17px               | 400    | 1.74–1.9|
| Caption/note | system sans                       | 12–14px               | 400    | 1.5–1.68|
| Code         | JetBrains Mono / Fira Code        | 12px                  | 400    | 1.7     |

## Slide background radial gradients (per-slide variation)

All slides share the same base `#F4E8C8`, with two subtle radial overlays to
add warmth and depth. Change the `circle at X% Y%` coordinates per slide for
visual variety:

```css
background:
  radial-gradient(circle at 18% 20%, rgba(226,187,112,0.18), transparent 30%),
  radial-gradient(circle at 88% 74%, rgba(78,103,80,0.13),  transparent 34%),
  #F4E8C8;
```

Common position presets:
- Cover: `22% 26%` / `82% 68%`
- Content L: `16% 22%` / `86% 72%`
- Content R: `82% 24%` / `14% 76%`
- Summary: `18% 20%` / `88% 74%`

## Paper grain overlay (pseudo-element)

Applied via `.slide::before` — creates a subtle crosshatch texture that
references physical paper without being distracting:

```css
.slide::before {
  content: '';
  position: absolute; inset: 0;
  background-image:
    linear-gradient(rgba(93,67,33,0.035) 1px, transparent 1px),
    linear-gradient(90deg, rgba(93,67,33,0.025) 1px, transparent 1px);
  background-size: 32px 32px, 44px 44px;
  mix-blend-mode: multiply;
  opacity: 0.5;
  pointer-events: none; z-index: 0;
}
.slide > * { position: relative; z-index: 1; }
```
