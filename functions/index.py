# -*- coding: utf8 -*-
import json
import os
import re

from utils import check, create_image, generate_imgstr

scf_env = os.environ.get('PYTHONPATH')

def parse_params(event):
    # image_size
    image_size_raw = event.get('pathParameters').get('size')
    image_size_arr = re.split('[,x*]', image_size_raw)
    if len(image_size_arr) == 1:
        image_size = (int(image_size_arr[0]), int(image_size_arr[0]))
    else:
        image_size = (int(image_size_arr[0]), int(image_size_arr[1]))
    
    return dict(
        size = image_size
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