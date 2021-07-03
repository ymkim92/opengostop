# Importing Image class from PIL module 
from PIL import Image, ImageChops
import argparse
import sys

# https://stackoverflow.com/questions/10615901/trim-whitespace-using-pil/10616717#10616717
empty_part_pixel_color = (0, 0, 0, 0)  
def trim(im):
    # im.show()
    bg = Image.new(im.mode, im.size, empty_part_pixel_color)
    diff = ImageChops.difference(im, bg)
    diff = ImageChops.add(diff, diff, 2.0, -100)
    bbox = diff.getbbox()
    # print(f'bbox {bbox}')
    if bbox:
        return im.crop(bbox)

def get_card(x, y):
    # Opens a image in RGB mode 
    im = Image.open(r"images/cards.png") 

    # Size of the image in pixels (size of orginal image) 
    # (This is not mandatory) 
    width, height = im.size 

    print(im.size)  
    # Setting the points for cropped image 
    card_width = width/8
    card_height = height/6

    left = card_width*x
    top = card_height*y
    right = left + card_width
    bottom = top + card_height
    
    print( left, top, right, bottom)
    # Cropped image of above dimension 
    # (It will not change orginal image) 
    im1 = im.crop((left, top, right, bottom)) 
    
    print(im1.size)  
    print(im1.mode)  
    # im1.save("images/gostop.png") 
    im1 = trim(im1)

    return im1

def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('x', type=int, choices=range(0, 8))
    parser.add_argument('y', type=int, choices=range(0, 6))
    return parser.parse_args(sys.argv[1:])


if __name__ == "__main__":
    # args = get_arguments()
    # get_card(args.x, args.y)
    for i in range(8):
        for j in range(6):
            card_image = get_card(i, j)
            card_image.save(f"images/{i}{j}.png")