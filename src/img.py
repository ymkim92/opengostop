# Improting Image class from PIL module 
from PIL import Image 
import argparse
import sys
  
def show_card(x, y):
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
    
    # Shows the image in image viewer 
    im1.show() 

def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('x', type=int, choices=range(0, 8))
    parser.add_argument('y', type=int, choices=range(0, 6))
    return parser.parse_args(sys.argv[1:])


if __name__ == "__main__":
    args = get_arguments()
    show_card(args.x, args.y)