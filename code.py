French_Name = ''
Uighur_Name = ''
position_fr = (0.28, 0.041)    #(0.28, 0.045)
fontsize_fr = 42;                   #35;
position_ug = (0.25, 0.485)
fontsize_ug = 60;
#################################################################################
# do not change blew
#################################################################################
from PIL import Image, ImageDraw, ImageFont
import imageio
import os
import webbrowser
from bidi.algorithm import get_display
import arabic_reshaper

def generate_fade_frames(image1, image2, steps):
    frames = []
    for step in range(steps):
        blend_ratio = step / float(steps - 1)
        faded_image = Image.blend(image1, image2, blend_ratio)
        frames.append(faded_image)
    return frames
def add_text_to_image(image_input, text, position, font_size,font_type):
    if isinstance(image_input, Image.Image):
        img = image_input
    else:
        img = Image.open(image_input)

    draw = ImageDraw.Draw(img)
    width, height = img.size
    absolute_position = (int(position[0] * width), int(position[1] * height))
    if font_type == "Uighur":
        font_path = "Microsoft Uighur regular.ttf"
        font = ImageFont.truetype(font_path, font_size)
        reshaped_text = arabic_reshaper.reshape(text)
        bidi_text = get_display(reshaped_text)
        draw.text(absolute_position,  reshaped_text, font=font, fill=(223, 158, 157))
    else:
        font = ImageFont.truetype("Apple Chancery.ttf", font_size)
        draw.text(absolute_position, text, font=font, fill=(223, 158, 157))
    return img

def create_fading_gif(images_paths, output_path='_'+French_Name+'.gif', frame_duration=0.1):
    frames = []
    durations = []
    for i, image_path in enumerate(images_paths):
        if isinstance(image_path, Image.Image):
            img = image_path.resize(size)
        else:
            img = Image.open(image_path).resize(size)
        fade_steps = 50     
        if i > 0:
            fade_frames = generate_fade_frames(frames[-1], img, steps=fade_steps)
            frames.extend(fade_frames[1:])
            durations.extend([frame_duration for _ in fade_frames[1:]])
        
        frames.append(img)
        durations.append(frame_duration)
    
    imageio.mimsave(output_path, [frame for frame in frames], duration=durations)
    print("---------- DONE ----------")
img3_with_text = add_text_to_image('p3.png', French_Name, position_fr, fontsize_fr,"French")
img3_with_text = add_text_to_image(img3_with_text, Uighur_Name, position_ug, fontsize_ug,"Uighur")
img3_with_text_path = 'p3_modified.png'
img3_with_text.save(img3_with_text_path)
images_paths = ['p1.png', 'p2.png', img3_with_text_path, 'p4.png', 'p5.png']
size = (500, 700)
create_fading_gif(images_paths)
img = Image.open('p3_modified.png')
img.show()
#normalized_path = os.path.abspath('faire-part.gif')
#file_url = f'file://{normalized_path}'
#safari = webbrowser.get('safari')
#safari.open(file_url)
