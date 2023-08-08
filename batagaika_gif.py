import os
from PIL import Image, ImageFont, ImageDraw

image_paths = os.listdir('images')


def draw_inscription(
    image,
    font_path,
    font_size,
    font_fill,
    text_align,
    text_pos,
    text
):
    img = image
    font = ImageFont.truetype(font_path, font_size)
    drawer = ImageDraw.Draw(img)
    drawer.text((text_pos), text, font=font, fill=font_fill, align=text_align)


def create_frames(out_path):
    for image_path in image_paths:
        image = Image.open('images/' + image_path)
        draw_inscription(image, 'fonts/ARIALBD.TTF', 84, 'white', 'left', (50, 50), 'Batagaika crater\n2014-2023')
        draw_inscription(image, 'fonts/ARIAL.TTF', 54, 'white', 'left', (50, 230), 'Sakha Republic, Russia')
        draw_inscription(image, 'fonts/ARIALBD.TTF', 72, 'white', 'right', (1351, 1634), f'{image_path[:-4]}')
        draw_inscription(image, 'fonts/ARIAL.TTF', 54, 'white', 'right', (1471, 1717), f'{"Landsat-8" if int(image_path[:4]) < 2019 else "Sentinel-2"}\nband 8')
        image.save(f'{out_path}frame_{image_path}')
    frames_list = os.listdir('frames')
    return frames_list


def create_gif(file_out, frames, duration, loop):
    frames = [Image.open(f'frames/{frame}') for frame in os.listdir('frames')]
    frames[0].save(
        file_out,
        save_all=True,
        append_images=frames[1:],
        optimize=True,
        duration=duration,
        loop=loop
    )
