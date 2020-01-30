'''
This function gives you the possibility to 
add a watermark to the imported videos, positions and size of 
the watermark can be changed within the code
'''

import moviepy.editor as mp
import os

def create_watermark():
    # Give user the option to customize and position the watermark on the video.

    file_path = input('Enter full path to file: ')

    success = False
    while not success:
        watermark_position = input('''
Watermark positioning
1 = Bottom Right (default)
2 = Bottom Left
3 = Top Right
4 = Top Left
Enter watermark position: ''')

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

    watermark_size = float(input('''
Watermark size ranges
Make sure to enter ONE number between the following ranges!
0.1 - 0.3 = small size
0.4 - 0.7 = medium size 
0.8 - 1.0 = large size
Enter size of watermark: '''))

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
