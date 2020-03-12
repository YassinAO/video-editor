'''
This function gives you the possibility to 
convert the extension of a video file.
'''
from scripts import style
import os


def create_convertion(video_file_path):
    extension_support = ['mp4', 'mkv', 'mov']
    old_filename = video_file_path.rsplit('\\', 1)[-1]
    old_extension = os.path.splitext(video_file_path)[1]
    new_filename = old_filename.replace(old_extension, '')
    color = style.bcolors()

    while True:
        new_extension = input('''
currently supported extensions
mp4
mkv
mov
Enter preferred extension: ''')

        if new_extension in extension_support:
            os.system(f'ffmpeg -i {video_file_path} -codec copy assets/videos/{new_filename}.{new_extension}')
            break
        else:
            os.system('cls')
            print(f'{color.FAIL}Choose one of the supported extensions!{color.ENDC}')
            continue
