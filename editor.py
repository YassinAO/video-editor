from scripts import gif, split, watermark, frame, concatenate
import os

def menu_option():
    os.system('cls')
    select_option = input('''
     ------------------------------------------------
    |   Select one of the options below.             |
    |                                                |
    |   1 = Create a gif out of the video            |
    |   2 = Add a watermark to the video             |
    |   3 = Export video frames to images            |
    |   4 = Split video into multiple parts          |
    |   5 = Concatenate videos                       |
    |                                                |
    |   NOTE: curently only .mp4 extension support,  |
    |   more will be added in the future!            |  
     ------------------------------------------------                                             
    ''')

    # Give user the option to create a gif out of the video.
    if select_option == '1':
        gif.create_gif()

    # Give user the option to customize and position the watermark on the video.
    elif select_option == '2':
        watermark.customize()
        
    # Give user the option to export video frames to images.
    elif select_option == '3':
        frame.create_frames()

    # Give user the option to split the video into multiple parts.
    elif select_option == '4':
        split.create_split()

    # Give user the option to concatenate multiple videos.
    elif select_option == '5':
        concatenate.create_merge()
    else:
        print('Select one of the options given.')
        menu_option()

menu_option()
