import base64

from PIL import Image, ImageDraw, ImageFont


def check(params):
    print('== check_image_size ==')
    # check image size
    size = params.get('size')
    if size[0] * size[1] > 1.2e+7:
        raise Exception('Image size is too large')
    return True

def create_image(params):
    print('== create_image ==')
    print(params)
    # draw background
    size = params.get('size')
    bg_color = (221, 221, 221)
    image = Image.new('RGB', size, bg_color)
    # draw text
    text = str(size[0]) + ' x ' + str(size[1])
    text_color = (170, 170, 170)
    draw_text(
        image = image,
        text = text,
        text_color = text_color
    )
    return image

def generate_imgstr(img):
    img.save('/tmp/img.png')
    # move to beginning of file so `send_file()` it will read from start   
    # file_object.seek(0)
    with open("/tmp/img.png", "rb") as f:
        data = f.read()
    base64_data = base64.b64encode(data)    
    base64_str = base64_data.decode('utf-8')
    return base64_str

def draw_text(image, text, text_color=(0, 0, 0)):
    draw = ImageDraw.Draw(image)
    font_size = min(image.size[0] // 10, image.size[1] // 3, 160)
    font_style = ImageFont.truetype('Exo2-Regular.ttf', font_size)
    position = ((image.size[0]) / 2, (image.size[1]) / 2)
    draw.text(
        xy = (position),
        text = text,
        font = font_style,
        fill = text_color,
        anchor = 'mm'
    )
    return image
