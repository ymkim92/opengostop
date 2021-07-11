# Importing Image class from PIL module 
from PIL import Image
import click
import sys

def get_concat_h(im1, im2, overlap_percent):
    overlapping_width = im2.width*overlap_percent//100
    dst = Image.new('RGB', (im1.width + im2.width - overlapping_width, im1.height))
    dst.paste(im1, (0, 0))
    dst.paste(im2, (im1.width - overlapping_width, 0))
    return dst

@click.command()
@click.argument('src', nargs=-1, required=True)
@click.option('-d', '--dst')
@click.option('-o', '--overlap', default=0)
def build_image(src, dst, overlap):
    images = []
    for i in src:
        images.append(Image.open(i))
    
    dst_image = images.pop(0)
    for i in images:
        dst_image = get_concat_h(dst_image, i, overlap)

    if dst: 
        dst_image.save(dst)
    else:
        dst_image.show()

if __name__ == "__main__":
    build_image()