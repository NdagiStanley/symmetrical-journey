from PIL import Image, ImageFilter, ImageEnhance

# Access the image
image = Image.open('input.png')

# FILTERS

image.filter(ImageFilter.DETAIL).show()
image.filter(ImageFilter.BLUR).show()
image.filter(ImageFilter.EMBOSS).show()
image.rotate(180).show()
image.filter(ImageFilter.FIND_EDGES).show()
image.filter(ImageFilter.CONTOUR).show()

# Increase contrast by 30%
enh = ImageEnhance.Contrast(image)
enh.enhance(1.3).show()

# Brighten
image.point(lambda i: i * 1.2).show()

# Black and White
image.convert("L").show()

# Pixelate
backgroundColor = (0, ) * 3
pixelSize = 9
image = image.resize((image.size[0]/pixelSize, image.size[1]/pixelSize),
                     Image.NEAREST)
image = image.resize((image.size[0] * pixelSize, image.size[1] * pixelSize),
                     Image.NEAREST)
pixel = image.load()
for i in range(0, image.size[0], pixelSize):
    for j in range(0, image.size[1], pixelSize):
        for r in range(pixelSize):
            pixel[i + r, j] = backgroundColor
            pixel[i, j + r] = backgroundColor
image.save('output.png')
