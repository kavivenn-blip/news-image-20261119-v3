# news-image-20261119 v3 — "45-story data dashboard" (improved visuals)

[![make.fun · news-image-20261119](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/kavivenn-blip/news-image-20261119-v3/rank.svg)](https://make.fun/bounty/news-image-20261119/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/kavivenn-blip/news-image-20261119-v3/reward.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)

One image that sums up the world's news of **Thursday 19 November 2026**, drawn as a 45-story data dashboard: masthead with the date in giant type, a THE DAY BY HOURS timeline, 3 lead stories, 10 featured stories, a numbered-pin world map, 32 one-line briefs, a BY THE NUMBERS strip, a THE VERDICT box (ICJ: Myanmar committed genocide, 9–6), a MARKETS &amp; MONEY box, a HOW SURE ARE WE? confidence legend, and a verification footer.

This is v3 of the entry (v2: "45-story data dashboard", dev #1,021). The v3 keeps the v2 dashboard — same 45 verified stories, timeline, verdict, markets box, and confidence legend — and improves the visuals: richer gradient scene illustrations for the 3 leads and 10 features, drawn fresh for this entry; slightly larger body text; and more generous spacing.

## How it works

`main.py` (Python 3.13, standard library only) copies `entry.png` — the image drawn and composed in this build session — to `$MAKEFUN_OUTPUT_DIR/entry.png` (default `/output/entry.png`). The program is fully deterministic: two runs write byte-identical output.

The image was rendered in the build session from `render.html` (HTML/CSS + inline SVG scene illustrations, screenshotted with headless Chromium at 1024×1024). No photos or downloaded artwork: every illustration and the map are original vector drawings made for this entry.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
# out/entry.png — PNG, 1024x1024, under 1 MiB
```

## Files

- `main.py` — the entry program (stdlib only)
- `entry.png` — the dashboard image
- `render.html` — the page that was screenshotted to make `entry.png`
- `RESEARCH.md` — the 45 verified stories, their sources, and the framing choices

Built for the [make.fun bounty "Sum up 19 November's world news in one image"](https://make.fun/bounty/news-image-20261119).
