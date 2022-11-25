"""
File: best_photoshop_award.py
Name: Mandy
----------------------------------
This file creates a photoshopped image
that is going to compete for the Best
Photoshop Award for SC001.
Please put all the images you will use in the image_contest folder
and make sure to choose the right folder when loading your images.
"""
from simpleimage import SimpleImage

BLACK_PIXEL = 160


def main():
    """
    創作理念：看極光
    """

    ko = SimpleImage('korea1.jpg')

    bg = SimpleImage('aurora.jpg')
    bg.make_as_big_as(ko)

    combined_img = combine(ko, bg)
    combined_img.show()


def combine(ko, bg):
    """
    : param1 bg: SimpleImage, the background image
    : param2 ko: SimpleImage, the real photo
    : return ko: SimpleImage, the background of real photo is replaced by background image
    """
    for y in range(ko.height):
        for x in range(ko.width):
            pixel_ko = ko.get_pixel(x, y)
            avg = (pixel_ko.red+pixel_ko.blue+pixel_ko.green) // 3
            total = pixel_ko.red+pixel_ko.blue+pixel_ko.green
            if total > BLACK_PIXEL:
                pixel_cl = bg.get_pixel(x, y)
                pixel_ko.red = pixel_cl.red
                pixel_ko.blue = pixel_cl.blue
                pixel_ko.green = pixel_cl.green

    return ko



# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
