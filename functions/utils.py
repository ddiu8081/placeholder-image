import base64

from PIL import Image, ImageDraw, ImageFont


def check(params):
    print('== check ==')
    # check image size
    image_size = params.get('image_size')
    if image_size[0] * image_size[1] > 1.2e+7:
        raise Exception('Image size is too large')
    return True

def create_image(params):
    print('== create_image ==')
    print(params)
    image_size = params.get('image_size')
    bg_color = params.get('bg_color')
    fg_color = params.get('fg_color')
    custom_text = params.get('custom_text')
    # draw background
    image = Image.new('RGB', image_size, bg_color)
    # draw text
    text = str(image_size[0]) + ' x ' + str(image_size[1])
    if custom_text:
        text = custom_text
    text_color = fg_color
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
