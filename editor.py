'''
TODO Make use of multi processing to speed up the process.
'''

from scripts import gif, split, watermark, frame, concatenate, convert
import os

def menu_option():
    red_text  = '\033[31m'
    white_text = '\033[0m'

    select_option = input('''
 ------------------------------------------------
|   MENU                                         |
|                                                |
|   1 = Create a gif out of the video            |
|   2 = Add a watermark to the video             |
|   3 = Export video frames to images            |
|   4 = Split video into multiple parts          |
|   5 = Concatenate videos                       |
|   6 = Convert video extension                  |
 ------------------------------------------------                                                 
Enter preferred option: ''')

    # Give user the option to create a gif out of the video.
    if select_option == '1':
        gif.create_gif()

    # Give user the option to customize and position the watermark on the video.
    elif select_option == '2':
        watermark.create_watermark()
        
    # Give user the option to export video frames to images.
    elif select_option == '3':
        frame.create_frames()

    # Give user the option to split the video into multiple parts.
    elif select_option == '4':
        split.create_split()

    # Give user the option to concatenate multiple videos.
    elif select_option == '5':
        concatenate.create_concatenation()
    
    # Give user the option to convert the video extension.
    elif select_option == '6':
        convert.create_convertion()

    else:
        os.system('cls')
        print(f'{red_text}Select one of the options from the menu!{white_text}')
        menu_option()

menu_option()
