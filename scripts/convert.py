'''
This function gives you the possibility to 
convert the extension of a video file.
'''

import os

def create_convertion():
    file_path = input('Enter full path to file: ')
    old_filename = file_path.rsplit('\\', 1)[-1]
    old_extension = os.path.splitext(file_path)[1]
    new_filename = old_filename.replace(old_extension, '')
    extension_support = ['mp4', 'mkv', 'mov']
    red_text  = '\033[31m'
    white_text = '\033[0m'

    if os.path.isfile(file_path):
        pass
    else:
        os.system('cls')
        print(f'{red_text}File doesn\'t exist in this directory!{white_text}')
        create_convertion()

    while True:
        new_extension = input('''
currently supported extensions
mp4
mkv
mov
Enter preferred extension: ''')

        if new_extension in extension_support:
            converter = os.system(f'ffmpeg -i {file_path} -codec copy assets/videos/{new_filename}.{new_extension}')
            break
        else:
            os.system('cls')
            print(f'{red_text}Choose one of the supported extensions!{white_text}')
            