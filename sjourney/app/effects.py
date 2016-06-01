from PIL import Image, ImageFilter, ImageEnhance

def Effect(effect, url):
    """
    Accepts effect as an integer
    The url as a string
    The return value should be an image
    """

    # Access the image and convert to RGBA to allow the filters
    try:
        image = Image.open(url).convert('RGBA')
        effect = int(effect)
    except:
        print("cannot open image file error")
        return None

    # Black and White
    if effect == 1:
        print "A"
        pic = image.convert("L")

    # FILTERS
    elif effect == 2:
        pic = image.filter(ImageFilter.DETAIL)

    elif effect == 3:
        pic = image.filter(ImageFilter.BLUR)

    elif effect == 4:
        pic = image.filter(ImageFilter.EMBOSS)

    elif effect == 5:
        pic = image.rotate(180)

    elif effect == 6:
        pic = image.filter(ImageFilter.FIND_EDGES)

    elif effect == 7:
        pic = image.filter(ImageFilter.CONTOUR)

    # Increase contrast by 30%
    elif effect == 8:
        enh = ImageEnhance.Contrast(image)
        pic = enh.enhance(1.3)

    # Brighten
    elif effect == 9:
        pic = image.point(lambda i: i * 1.2)

    # Pixelate
    elif effect == 10:
        background_color = (0, ) * 3
        pixel_size = 9
        img = image.resize((image.size[0] / pixel_size,
                            image.size[1] / pixel_size), Image.NEAREST)
        img = img.resize((img.size[0] * pixel_size,
                          img.size[1] * pixel_size), Image.NEAREST)
        pixel = img.load()
        for i in range(0, img.size[0], pixel_size):
            for j in range(0, img.size[1], pixel_size):
                for r in range(pixel_size):
                    pixel[i + r, j] = background_color
                    pixel[i, j + r] = background_color
        pic = img

    return pic
