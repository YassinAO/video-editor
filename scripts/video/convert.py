'''
This function gives you the possibility to 
convert the extension of a video file.
'''

import os

def create_convertion():
    video_file_path = input('Enter full path to video file: ')
    old_filename = video_file_path.rsplit('\\', 1)[-1]
    old_extension = os.path.splitext(video_file_path)[1]
    new_filename = old_filename.replace(old_extension, '')
    extension_support = ['mp4', 'mkv', 'mov']
    red_text  = '\033[31m'
    white_text = '\033[0m'
    green_text = '\033[92m'

    # Make sure that the user provides a video file.
    if os.path.isfile(video_file_path):
        if video_file_path.lower().endswith(('.mp4', '.mkv', '.mov')):
            print(f'{green_text}Video file has been found!{white_text}')
        else:
            os.system('cls')
            print(f'{red_text}File isn\'t a video extension! (e.g.) .mp4 .mkv .mov{white_text}')
            create_convertion()   
    else:
        os.system('cls')
        print(f'{red_text}Video file doesn\'t exist in this directory!{white_text}')
        create_convertion()

    while True:
        new_extension = input('''
currently supported extensions
mp4
mkv
mov
Enter preferred extension: ''')

        if new_extension in extension_support:
            converter = os.system(f'ffmpeg -i {video_file_path} -codec copy assets/videos/{new_filename}.{new_extension}')
            break
        else:
            os.system('cls')
            print(f'{red_text}Choose one of the supported extensions!{white_text}')
