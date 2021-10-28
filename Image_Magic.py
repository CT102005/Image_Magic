# Image Magic
# Load an image and manipulate the pixels

from PIL import Image


def to_greyscale(pixel: tuple, algo="average") -> tuple:
    """convert a pixel to greyscale
    Can also specify the greyscale algorithm.
    Defaults to average.
    Args:
        pixel:
            a 3-tuple of ints from 0 - 255, e.g. (140, 120, 225).
            Represents (red, green, blue)
        algo: the greyscale conversion algorithm
            specified by the user
            valid values are "average", "luma"
            defaults to "average"

    Returns:
        a 3-tuple pixel (r, g, b) in greyscale
    """

    # grab r g b
    red = pixel[0]
    green = pixel[1]
    blue = pixel[2]

    red, green, blue = pixel
    # calculate the average
    if algo.lower() == "luma":
        grey = int(red * 0.3 + green * 0.59 + blue * 0.11)
    else:
        grey = int((red + green + blue)/3)
    # create a gray pixel
    return grey, grey, grey

def to_greyscale_luma(pixel: tuple) -> tuple:
    """convert to greyscale using luma algorithm

    Args:
        pixel: a 3-tuple of ints from 0 - 255, e.g. (140, 120, 225). Represents (red, green, blue)

    Returns:
        a 3-tuple pixel (r, g, b) in greyscale
    """
    red, green, blue = pixel
    grey = int(red * 0.3 + green * 0.59 + blue * 0.11)
    return grey, grey, grey

def brighter(pixel: tuple) -> tuple:
    """Increases the brightness of a pixel

    Args:
        Pixel: a 3-tuple of (red, green, blue)
            subpixels

    Returns:
        a 3-tuple representing a brighter pixel
    """
    red, green, blue = pixel
    if red <= 230:
        red = int(red) + 25
    else:
        red = 255
    if green <= 230:
        green = int(green) + 25
    else:
        green = 255
    if blue <= 230:
        blue = int(blue) + 25
    else:
        blue = 255
    return red, green, blue

def brightness(pixel: tuple, magnitude: int) -> tuple:
    """Increases the brightness of a pixel

    Args:
        Pixel: a 3-tuple of (red, green, blue)
            subpixels

    Returns:
        a 3-tuple representing a brighter pixel
    """
    red, green, blue = pixel
    MAX = 255
    MIN = 0
    if red + magnitude > MAX:
        red = MAX
    elif red + magnitude < MIN:
        red = MIN
    else:
        red = int(red) + magnitude

    if green + magnitude > MAX:
        green = MAX
    elif green + magnitude < MIN:
        green = MIN
    else:
        green = int(green) + magnitude

    if blue + magnitude > MAX:
        blue = MAX
    elif blue + magnitude < MIN:
        blue = MIN
    else:
        blue = int(blue) + magnitude
    return red, green, blue

# Load the image (pumpkin)
image = Image.open('./halloween-unsplash.jpg')
# Grab pixel information
a_pixel = image.getpixel((0, 0))  # grab pixel (0, 0) top-left
output_image = Image.open('./halloween-unsplash.jpg')
print(a_pixel)

# red value of the pixel
print(f"red:{a_pixel[0]}")
print(f"green:{a_pixel[1]}")
print(f"blue:{a_pixel[2]}")

# Iterate over EVERY PIXEL
# Gets dimensions (size) of the image
image_width = image.width
image_height = image.height

# Modify the image to convert it from colour to grayscale
# (r, g, b) --> (?, ?, ?)
# take the r g b, add them up and divide by three
# replace r, g, b with that AVERAGE value

# Top to bottom
for y in range(image_height):
    # Left to right
    for x in range(image_width):
        # Grab information for THIS pixel
        pixel = image.getpixel((x, y))
        # TODO: add function call to to_greyscale
        brighter_pixel = brightness(pixel, -100)
        # put that in the new image
        output_image.putpixel((x, y), brighter_pixel)
output_image.save('brightness_lower2.jpg')