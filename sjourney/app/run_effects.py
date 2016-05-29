import effects
import glob, os

from PIL import Image

size = 128, 128
url = '../../media/pics/stanmd.jpg'

# Apply effects
effects.Effect(1, url).save('b_w.jpg')
effects.Effect(2, url).save('detail.jpg')
effects.Effect(3, url).save('blur.jpg')
effects.Effect(4, url).save('emboss.jpg')
effects.Effect(5, url).save('upside_down.jpg')
effects.Effect(6, url).save('find_edges.jpg')
effects.Effect(7, url).save('contour.jpg')
effects.Effect(8, url).save('contrast.jpg')
effects.Effect(9, url).save('bright.jpg')
effects.Effect(10, url).save('pixelate.jpg')

# Create thumbnails for the images
for infile in glob.glob("*.jpg"):
    file, ext = os.path.splitext(infile)
    im = Image.open(infile)
    im.thumbnail(size)
    # Save them in a previews folder
    im.save("../../media/previews/" + file + ".thumbnail", "JPEG")

# Delete the images created
os.system("rm *.jpg")
