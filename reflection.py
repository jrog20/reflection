"""
File: reflection.py
This program mirrors an image, below the original image.
"""

from simpleimage import SimpleImage

def main():
    original = SimpleImage('images/farrier.jpg')
    original.show()

    reflected = make_reflected('images/farrier.jpg')
    reflected.show()

def make_reflected(filename):
    image = SimpleImage(filename)
    width = image.width
    height = image.height

    mirror = SimpleImage.blank(width, height * 2)

    for y in range(height):
        for x in range(width):
            pixel = image.get_pixel(x, y)
            mirror.set_pixel(x, y, pixel)
            mirror.set_pixel(x, (height * 2) - (y + 1), pixel)
    return mirror


if __name__ == '__main__':
    main()
