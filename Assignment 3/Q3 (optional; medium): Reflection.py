Q3 (optional; medium): Reflection
 

from simpleimage import SimpleImage


def make_reflected(filename):
    image = SimpleImage(filename)
    width = image.width
    height = image.height
    ref_image = SimpleImage.blank(width, height * 2)
    for x in range(width):
        for y in range(height):
            pixel = image.get_pixel(x, y)
            ref_image.set_pixel(x, y, pixel)
            ref_image.set_pixel(x, (height * 2) - (y + 1), pixel)

    return ref_image


def main():
    """
    This program tests your highlight_fires function by displaying
    the original image of a fire as well as the resulting image
    from your highlight_fires function.
    """
    original = SimpleImage('images/mt-rainier.jpg')
    original.show()
    reflected = make_reflected('images/mt-rainier.jpg')
    reflected.show()


if __name__ == '__main__':
    main()
