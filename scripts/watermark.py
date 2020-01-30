'''
This function gives you the possibility to 
add a watermark to the imported videos. 
The user can choose the preferred position and size of the watermark.

TODO: Let the user import their own watermark.
'''

import moviepy.editor as mp
import os

def create_watermark():
    file_path = input('Enter full path to file: ')
    size_support = ['small', 'medium', 'large']
    position_support = ['bottom-right', 'bottom-left', 'top-right', 'top-left']
    red_text  = '\033[31m'
    white_text = '\033[0m'

    if os.path.isfile(file_path):
        pass
    else:
        os.system('cls')
        print(f'{red_text}File doesn\'t exist in this directory!{white_text}')
        create_watermark()

    while True:
        watermark_position = input('''
currently supported positions
bottom-right
bottom-left
top-right
top-left
Enter preferred position: ''')

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
            print(f'{red_text}Choose one of the supported positions!{white_text}')

    while True:
        watermark_size = (input('''
currently supported sizes
small
medium
large
Enter preferred size: '''))

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
            print(f'{red_text}Choose one of the supported sizes!{white_text}')

    # Used to rename the new file
    index= file_path.rsplit('\\', 1)[-1]   
    new_filename = 'watermarked-' + index
    
    video = mp.VideoFileClip(file_path)
    
    watermark = (mp.ImageClip('assets/watermark/watermark.png')
               .set_duration(video.duration)
               .resize(watermark_size)
               .margin(right=8, bottom=8, opacity=0)
               .set_pos((first_position, second_position)))

    # Overlay the watermark clip on the first video clip
    final_video = mp.CompositeVideoClip([video, watermark])

    # Write the result to a file (many options available!)
    final_video.write_videofile(f'assets/videos/{new_filename}')  # quality can be raised by using: bitrate="20000k"
