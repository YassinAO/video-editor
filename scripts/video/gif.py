'''
This function gives you the possibility to
create a gif from a video, by giving a start and end time.
'''

import moviepy.editor as mp
from scripts import style
import os


def time_symetrize(video_clip):
    return mp.concatenate([video_clip, video_clip.fx(mp.vfx.time_mirror)])


def create_gif(video_file_path):
    size_support = ['small', 'medium', 'large']
    type_support = ['normal', 'loop']
    old_filename = video_file_path.rsplit('\\', 1)[-1]
    old_extension = os.path.splitext(video_file_path)[1]
    new_filename = old_filename.replace(old_extension, '.gif')
    video = (mp.VideoFileClip(video_file_path))
    color = style.bcolors()

    while True:
        try:
            start_time = int(input('Enter start time (seconds): '))
            if start_time < 0 or start_time > int(video.duration):
                os.system('cls')
                print(f'{color.FAIL}Start time is out of video length range!{color.ENDC}')
                continue
            break
        except ValueError:
            os.system('cls')
            print(f'{color.FAIL}Input is invalid!{color.ENDC}')
            continue

    while True:
        try:
            end_time = int(input('Enter end time (seconds): '))
            if end_time < 0 or end_time > int(video.duration):
                os.system('cls')
                print(f'{color.FAIL}End time is out of video length range!{color.ENDC}')
                continue
            break
        except ValueError:
            os.system('cls')
            print(f'{color.FAIL}Input is invalid!{color.ENDC}')
            continue

    while True:
        gif_size = input('''
currently supported sizes
small
medium
large
Enter preferred size: ''')

        if gif_size in size_support:
            if gif_size == 'small':
                gif_size = 0.3
            elif gif_size == 'medium':
                gif_size = 0.5
            elif gif_size == 'large':
                gif_size = 0.7
            break
        else:
            os.system('cls')
            print(f'{color.FAIL}Choose one of the supported sizes!{color.ENDC}')
            continue

    while True:
        gif_type = input('''
currently supported types
normal
loop
Enter preferred type: ''')

        if gif_type in type_support:
            if gif_type == 'normal':
                video = (mp.VideoFileClip(video_file_path)
                         .subclip(start_time, end_time)
                         .resize(gif_size))

            elif gif_type == 'loop':
                video = (mp.VideoFileClip(video_file_path)
                         .subclip(start_time, end_time)
                         .resize(gif_size)
                         .fx(time_symetrize))
            break
        else:
            os.system('cls')
            print(f'{color.FAIL}Choose one of the supported types!{color.ENDC}')
            continue

    final_gif = mp.CompositeVideoClip([video])
    
    while True:
        if os.path.isfile(f'assets/gifs/{new_filename}'):
            overwrite = input(f'File \'assets/gifs/{new_filename}\' already exists. Overwrite ? [y/N] ')
            if overwrite.upper() == 'Y':
                final_gif.write_gif(f'assets/gifs/{new_filename}')
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
            final_gif.write_gif(f'assets/gifs/{new_filename}')
            break
