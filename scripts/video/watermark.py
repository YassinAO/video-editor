'''
This function gives you the possibility to 
add a watermark to the imported videos. 
The user can choose the preferred position and size of the watermark.
'''

import moviepy.editor as mp
from scripts import style
import os


def create_watermark(video_file_path, watermark_file_path):
    size_support = ['small', 'medium', 'large']
    position_support = ['bottom-right', 'bottom-left', 'top-right', 'top-left']
    old_filename = video_file_path.rsplit('\\', 1)[-1]
    old_extension = os.path.splitext(video_file_path)[1]
    new_filename = old_filename.replace(old_extension, '.mp4')
    color = style.bcolors()

    while True:
        watermark_position = input(f'''
Currently supported positions
bottom-right\nbottom-left\ntop-right\ntop-left
Enter preferred position {color.OKBLUE}(e.g. bottom-right){color.ENDC}: ''')

        if watermark_position in position_support:
            if watermark_position == 'bottom-right':
                first_position = 'right'
                second_position = 'bottom'
            elif watermark_position == 'bottom-left':
                first_position = 'left'
                second_position = 'bottom'
            elif watermark_position == 'top-right':
                first_position = 'right'
                second_position = 'top'
            elif watermark_position == 'top-left':
                first_position = 'left'
                second_position = 'top'
            break
        else:
            os.system('cls')
            print(f'{color.FAIL}Choose one of the supported positions!{color.ENDC}')
            continue

    while True:
        watermark_size = input(f'''
Currently supported sizes
small\nmedium\nlarge
Enter preferred size {color.OKBLUE}(e.g. small){color.ENDC}: ''')

        if watermark_size in size_support:
            if watermark_size == 'small':
                watermark_size = 0.3
            elif watermark_size == 'medium':
                watermark_size = 0.5
            elif watermark_size == 'large':
                watermark_size = 0.7
            break
        else:
            os.system('cls')
            print(f'{color.FAIL}Choose one of the supported sizes!{color.ENDC}')
            continue

    video = mp.VideoFileClip(video_file_path)

    watermark = (mp.ImageClip(watermark_file_path)
                 .set_duration(video.duration)
                 .resize(watermark_size)
                 .margin(left=8, right=8, top=8, bottom=8, opacity=0)
                 .set_pos((first_position, second_position)))

    final_video = mp.CompositeVideoClip([video, watermark])

    while True:
        if os.path.isfile(f'assets/videos/watermarked-{new_filename}'):
            overwrite = input(f'File \'assets/videos/watermarkd-{new_filename}\' already exists. Overwrite ? [y/N] ')
            if overwrite.upper() == 'Y':
                final_video.write_videofile(f'assets/videos/watermarked-{new_filename}')
                print(f'{color.OKGREEN}Overwriting - done{color.ENDC}')
                break
            elif overwrite.upper() == 'N':
                print(f'{color.FAIL}Not overwriting - exiting{color.ENDC}')
                break
            else:
                os.system('cls')
                print(f'{color.FAIL}Invalid input!{color.ENDC}')
                continue
        else:
            # quality can be raised by using the bitrate parameter e.g. bitrate="20000k"
            final_video.write_videofile(f'assets/videos/watermarked-{new_filename}')
            break
