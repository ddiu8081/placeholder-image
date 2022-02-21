import re

def parse_size(raw):
    image_size_arr = re.split('[,x*]', raw)
    if len(image_size_arr) == 1:
        image_size = (int(image_size_arr[0]), int(image_size_arr[0]))
    else:
        image_size = (int(image_size_arr[0]), int(image_size_arr[1]))
    return image_size

def parse_color(raw):
    color_rgb = tuple(int(raw[i:i+2], 16) for i in (0, 2, 4))
    return color_rgb
