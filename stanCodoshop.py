"""
File: stanCodoshop.py
Name: Mandy
----------------------------------------------
SC101_Assignment3 Adapted from Nick Parlante's
Ghost assignment by Jerry Liao.
"""

import os
import sys
from simpleimage import SimpleImage


def get_pixel_dist(pixel, red, green, blue):
    """
    Returns a value that refers to the "color distance" between a pixel and a mean RGB value.

    Input:
        pixel (Pixel): the pixel with RGB values to be compared
        red (int): the average red value of the pixels to be compare
        green (int): the average green value of the pixels to be compared
        blue (int): the average blue value of the pixels to be compared

    Returns:
        dist (float): the "color distance" of a pixel to the average RGB value of the pixels to be compared.
    """

    dist = ((red - pixel.red) ** 2 + (green - pixel.green) ** 2 + (blue - pixel.blue) ** 2) ** 0.5

    return dist


def get_average(pixels):
    """
    Given a list of pixels, finds their average red, blue, and green values.

    Input:
        pixels (List[Pixel]): a list of pixels to be averaged

    Returns:
        rgb (List[int]): a list of average red, green, and blue values of the pixels
                        (returns in order: [red, green, blue])
    """

    total_r = sum(pixel.red for pixel in pixels)/len(pixels)
    total_g = sum(pixel.green for pixel in pixels)/len(pixels)
    total_b = sum(pixel.blue for pixel in pixels)/len(pixels)

    # total_r = 0
    # total_g = 0
    # total_b = 0
    # #
    # for i in range(len(pixels)):  # input pixels as a list, use len to take element
    #     total_r += pixels[i].red
    #     total_g += pixels[i].green
    #     total_b += pixels[i].blue

    rgb = [total_r // len(pixels), total_g // len(pixels), total_b // len(pixels)]

    return rgb


def get_best_pixel(pixels):
    """
    Given a list of pixels, returns the pixel with the smallest "color distance", which has the closest color to the average.

    Input:
        pixels (List[Pixel]): a list of pixels to be compared
    Returns:
        best (Pixel): the pixel which has the closest color to the average
    """
    # avg=get_average(pixels)
    # dist_l=[]
    # for pixel in pixels:
    #     dist=get_pixel_dist(pixel,avg[0],avg[1],avg[2])
    #     dist_l.append((dist,pixel))
    # return min(dist_l, key=lambda t:t[0])[1] #在dist_l的list裡比dist(t[0]),return pixel(t[1])

    # create "dis_lst" list: [pixel, dis]
    pixel_d = {}
    avg_lst = get_average(pixels)  # return a list of average
    avg_r = avg_lst[0]
    avg_g = avg_lst[1]
    avg_b = avg_lst[2]

    for i in range(len(pixels)):  # each pixel in pixels list
        dis = get_pixel_dist(pixels[i], avg_r, avg_g, avg_b)  # calculate distance
        pixel_d[pixels[i]] = dis

    # put "distance"(ele[1]) in order, from smallest to largest
    best_pixel = min(pixel_d.items(), key=lambda ele: ele[1])

    return best_pixel[0]  # ele 0: pixel name


def solve(images):
    """
    Given a list of image objects, compute and display a Ghost solution image
    based on these images. There will be at least 3 images and they will all
    be the same size.

    Input:
        images (List[SimpleImage]): list of images to be processed
    """
    width = images[0].width
    height = images[0].height
    result = SimpleImage.blank(width, height)

    # ----- YOUR CODE STARTS HERE ----- #
    # Write code to populate image and create the 'ghost' effect

    pixels_lst = []  # stores pixel(x,y) in every image

    for x in range(width):
        for y in range(height):
            for i in range(len(images)):
                pixel = images[i].get_pixel(x, y)
                pixels_lst.append(pixel)
            best_pix = get_best_pixel(pixels_lst)
            new_pix = result.get_pixel(x, y)
            new_pix.red = best_pix.red
            new_pix.green = best_pix.green
            new_pix.blue = best_pix.blue
            pixels_lst = []

    # ----- YOUR CODE ENDS HERE ----- #

    print("Displaying image!")
    result.show()


def jpgs_in_dir(dir):
    """
    (provided, DO NOT MODIFY)
    Given the name of a directory, returns a list of the .jpg filenames
    within it.

    Input:
        dir (string): name of directory
    Returns:
        filenames(List[string]): names of jpg files in directory
    """
    filenames = []
    for filename in os.listdir(dir):
        if filename.endswith('.jpg'):
            filenames.append(os.path.join(dir, filename))
    return filenames


def load_images(dir):
    """
    (provided, DO NOT MODIFY)
    Given a directory name, reads all the .jpg files within it into memory and
    returns them in a list. Prints the filenames out as it goes.

    Input:
        dir (string): name of directory
    Returns:
        images (List[SimpleImages]): list of images in directory
    """
    images = []
    jpgs = jpgs_in_dir(dir)
    for filename in jpgs:
        print("Loading", filename)
        image = SimpleImage(filename)
        images.append(image)
    return images


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # We just take 1 argument, the folder containing all the images.
    # The load_images() capability is provided above.
    images = load_images(args[0])
    solve(images)


if __name__ == '__main__':
    main()
