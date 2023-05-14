#!/usr/bin/env python3

import os
from pathlib import Path
from PIL import Image

for img in os.listdir('supplier-data/images'):
    f = Path(f'images/{img}').stem
    outfile = f + ".jpeg"
    try:
        original_img = Image.open(f"supplier-data/images/{img}")
        modified_im = original_img.rotate(90).resize((600,400)).convert('RGB').save(f"supplier-data/images/{outfile}")
    except:
        pass

