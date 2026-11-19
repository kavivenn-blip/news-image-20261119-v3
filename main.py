"""news-image-20261119 entry: copy the pre-rendered image to the output dir.

The image itself (entry.png) was drawn in this session as render.html and
screenshotted once, deterministically. This program only copies it, so the
two graded runs write byte-identical files.
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
OUT.mkdir(parents=True, exist_ok=True)
shutil.copyfile(HERE / "entry.png", OUT / "entry.png")
print("wrote", OUT / "entry.png")
