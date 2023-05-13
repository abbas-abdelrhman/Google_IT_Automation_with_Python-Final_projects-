import os
from pathlib import Path
from PIL import Image

for img in os.listdir('original_images'):
    f = Path(f'images/{img}').stem
    outfile = f + ".jpg"
    try:
        original_img = Image.open(f"original_images/{img}")
        modified_im = original_img.rotate(90).resize((128, 128)).convert('RGB').save(f"modified_images/{outfile}")
    except:
        pass
