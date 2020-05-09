'''
This function gives you the possibility to 
split videos into multiple parts.
'''

import moviepy.editor as mp
from scripts import style
import os


def create_split(video_file_path):
    part_duration = 0
    start_time = [0]
    end_time = []
    old_filename = video_file_path.rsplit('\\', 1)[-1]
    old_extension = os.path.splitext(video_file_path)[1]
    new_filename = old_filename.replace(old_extension, '.mp4')
    video = (mp.VideoFileClip(video_file_path))
    color = style.bcolors()

    while True:
        try:
            video_parts = int(input(f'Enter amount of video parts {color.OKBLUE}(e.g. 2){color.ENDC}: '))
            break
        except ValueError:
            os.system('cls')
            print(f'{color.FAIL}Input is invalid - numbers only!{color.ENDC}')
            continue

    time_per_part = video.duration / video_parts

    for _ in range(int(video_parts)):
        part_duration += time_per_part
        start_time.append(round(part_duration, 2))
        end_time.append(round(part_duration, 2))

    # the last value in the start_time array gets deleted because it's only needed for the end_time array
    del start_time[-1]

    for part in range(int(video_parts)):
        video = (mp.VideoFileClip(video_file_path)
                 .subclip((start_time[int(part)]), (end_time[int(part)])))
        while True:
            if os.path.isfile(f'assets/videos/part-{part + 1}-{new_filename}'):
                overwrite = input(f'File \'assets/videos/part-{part + 1}-{new_filename}\' already exists. Overwrite ? [y/N] ')
                if overwrite.upper() == 'Y':
                    video.write_videofile(f'assets/videos/part-{part + 1}-{new_filename}')
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
                video.write_videofile(f'assets/videos/part-{part + 1}-{new_filename}')
                break

        # close the video to prevent 'OSError: [WinError 6] The handle is invalid'
        video.reader.close()
        video.audio.reader.close_proc()
