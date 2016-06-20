import effects
import glob, os

from PIL import Image

size = 128, 128

# Determine which im
url = 'media/pics/sjpreview.jpg'

# Apply effects
effects.apply_effect(1, url).save('b_w.jpg')
effects.apply_effect(2, url).save('detail.jpg')
effects.apply_effect(3, url).save('blur.jpg')
effects.apply_effect(4, url).save('emboss.jpg')
effects.apply_effect(5, url).save('upside_down.jpg')
effects.apply_effect(6, url).save('find_edges.jpg')
effects.apply_effect(7, url).save('contour.jpg')
effects.apply_effect(8, url).save('contrast.jpg')
effects.apply_effect(9, url).save('bright.jpg')
effects.apply_effect(10, url).save('pixelate.jpg')

# Create thumbnails for the images
for infile in glob.glob("*.jpg"):
    file, ext = os.path.splitext(infile)
    im = Image.open(infile)
    im.thumbnail(size)
    # Save them in a previews folder
    im.save("media/previews/" + file + ".thumbnail", "JPEG")

# Delete the images created
os.system("rm *.jpg")
