'''
This function gives you the possibility to 
add a watermark to the imported videos, positions and size of 
the watermark can be changed within the code

TODO Change watermark position and size within commandline instead of source code.
'''

import moviepy.editor as mp
import os

def customize():
    success = False
    while not success:
        watermark_position = input('''
    Select position of watermark\n
        1 = Bottom Right (default)
        2 = Bottom Left
        3 = Top Right
        4 = Top Left
    ''')
        os.system('cls')

        if watermark_position == '1' or '2' or '3' or '4':
            success = True
        if watermark_position == '1':
            first_position = 'right'
            second_position = 'bottom'
        elif watermark_position == '2':
            first_position = 'left'
            second_position = 'bottom'
        elif watermark_position == '3':
            first_position = 'right'
            second_position = 'top'
        elif watermark_position == '4':
            first_position = 'left'
            second_position = 'top'
        else: 
            print('Select one of the options given.')

    create_watermark(first_position, second_position)


def create_watermark(first_position, second_position):
    # Give user the option to customize and position the watermark on the video.

    file_path = input('Enter path to file: ')

    # Used to rename the new file
    index = file_path.find('.mp4')
    new_filename = file_path[:index] + '-watermark.mp4'   
    video = mp.VideoFileClip(file_path)
    
    watermark = (mp.ImageClip('assets/watermark/watermark.png')
               .set_duration(video.duration)
               .resize(0.2)
               .margin(right=8, bottom=8, opacity=0)
               .set_pos((first_position, second_position)))

    # Overlay the watermark clip on the first video clip
    final_video = mp.CompositeVideoClip([video, watermark])

    # Write the result to a file (many options available!)
    final_video.write_videofile('./assets/videos/' + new_filename)  # quality can be raised by using: bitrate="20000k"
    