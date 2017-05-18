#!/usr/bin/env python

from PIL import Image
import sys

def invert_pixel(pixel):
    return (255 - pixel[0], 255 - pixel[1], 255 - pixel[2])

def invert_image(image):
    width = image.size[0]
    height = image.size[1]
    total = width * height
    output_image = Image.new("RGB", (width, height), (0,0,0))
    counter = 0
    for i in xrange(width):
        for j in xrange(height):
            show_progress(counter, total)
            pixel = image.getpixel((i, j))
            output_pixel = invert_pixel(pixel)
            output_image.putpixel((i, j), output_pixel)
            counter += 1
    return output_image

def show_progress(progress, total):
    percent = (((progress * 1.0) / total) * 100)
    sys.stdout.write("[+] %2f%%\r" % (percent))
    sys.stdout.flush()


def main():
    if len(sys.argv) != 2:
        print "Usage : "
        print "       python ImageInvertor.py [Image]"
        print "Author : "
        print "       WangYihang <wangyihanger@gmail.com>"
        exit(1)
    image = Image.open(sys.argv[1])
    image.show()
    output_image = invert_image(image)
    output_image.show()

if __name__ == "__main__":
    main()
