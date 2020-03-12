'''
This function gives you the possibility to 
concatenate multiple videos.
'''

import moviepy.editor as mp
from scripts import style
import os


def create_concatenation():   
    videos = []
    all_video_file_paths = []
    all_filenames = []
    color = style.bcolors()

    while True:
        try:
            video_amount = int(input('Enter amount of videos: '))
            break
        except ValueError:
            os.system('cls')
            print(f'{color.FAIL}Input is invalid!{color.ENDC}')
            continue

    number = 0
    for _ in range(int(video_amount)):
        number += 1
        while True:
            video_file_path = input(f'Enter full path to video file {str(number)}: ')
            if os.path.exists(video_file_path):
                if video_file_path.lower().endswith(('.mp4', '.mkv', '.mov')):
                    all_video_file_paths.append(video_file_path)
                    videos.append(mp.VideoFileClip(video_file_path))
                    print(f'{color.OKGREEN}Video file has been found!{color.ENDC}\n')
                    break
                else:
                    os.system('cls')
                    print(f'{color.FAIL}File isn\'t a video extension! (e.g.) .mp4 .mkv .mov{color.ENDC}')
                    continue
            else:
                os.system('cls')
                print(f'{color.FAIL}File doesn\'t exist in this directory!{color.ENDC}')
                continue

    for x in all_video_file_paths:
        old_filename = x.rsplit('\\', 1)[-1]
        old_extension = os.path.splitext(video_file_path)[1]
        new_filename = old_filename.replace(old_extension, '')
        all_filenames.append(new_filename)

    merged_filename = '-'.join(all_filenames) + '.mp4'
    final_clip = mp.concatenate_videoclips(videos, method='compose')

    while True:
        if os.path.isfile(f'assets/videos/merged-{merged_filename}'):
            overwrite = input(f'File \'assets/videos/marge-{new_filename}\' already exists. Overwrite ? [y/N] ')
            if overwrite.upper() == 'Y':
                final_clip.write_videofile(f'assets/videos/merged-{merged_filename}')
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
            final_clip.write_videofile(f'assets/videos/merged-{merged_filename}')
            break
