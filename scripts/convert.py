'''
This function gives you the possibility to 
convert the extension of a video file.
'''

import os

def convert_video():
    file_path = input('Enter path to file: ')
    old_filename = file_path.rsplit('\\', 1)[-1]
    old_extension = os.path.splitext(file_path)[1]
    new_filename = old_filename.replace(old_extension, '')

    extension_support = ['.mp4', '.mkv', '.mov', '.avi']

    while True:
        new_extension = input('''
        Enter one of the supported extensions:
        .mp4
        .mkv
        .mov
        .avi
        ''')

        if new_extension in extension_support:
            converter = os.system(f'ffmpeg -i {file_path} -codec copy assets/videos/{new_filename}{new_extension}')
            break
        else:
            os.system('cls')
            print('Choose one of the supported extensions!')