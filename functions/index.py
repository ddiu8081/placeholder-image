# -*- coding: utf8 -*-
import json
import os

from parse import parse_size, parse_color
from utils import check, create_image, generate_imgstr

scf_env = os.environ.get('PYTHONPATH')

def parse_params(event):
    path_str = event.get('pathParameters').get('param')
    path_str_list = path_str.split('/')
    image_size = (0, 0)
    bg_color = (221, 221, 221)
    fg_color = (170, 170, 170)
    if (len(path_str_list) == 1):
        image_size = parse_size(path_str_list[0])
    elif (len(path_str_list) == 2):
        image_size = parse_size(path_str_list[0])
        bg_color = parse_color(path_str_list[1])
    elif (len(path_str_list) == 3):
        image_size = parse_size(path_str_list[0])
        bg_color = parse_color(path_str_list[1])
        fg_color = parse_color(path_str_list[2])

    return dict(
        image_size = image_size,
        bg_color = bg_color,
        fg_color = fg_color,
    )

def main_handler(event, context):
    print("Received event: " + json.dumps(event, indent = 2)) 
    print("Received context: " + str(context))
    
    input_params = parse_params(event)
    try:
        check(input_params)
    except Exception as e:
        print(str(e))
        return {
            'isBase64Encoded': False,
            'statusCode': 200,
            'headers': { 'Content-Type': 'text/html' },
            'body': str(e),
        }
    image = create_image(input_params)
    
    if (scf_env):
        img_str = generate_imgstr(image)
        return {
            'isBase64Encoded': True,
            'statusCode': 200,
            'headers': { 'Content-Type': 'image/png' },
            'body': img_str,
        }
    else:
        image.show()

if (not scf_env):
    if __name__ == '__main__':
        event = {
            "path": "/map/data",
            "pathParameters": {
                "size": "640x480"
            },
            "queryString": {
                "param1": "value1"
            },
            "queryStringParameters": {
                "param1": "value1"
            }
        }
        main_handler(event, None)