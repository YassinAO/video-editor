'''
This function gives you the possibility to 
export frames from a video and save them in your directory.

TODO Enter a start and endtime within the commandline of which the frames should be extracted from.
'''

import moviepy.editor as mp
from scripts import style
import os


def create_frames(video_file_path):
    frame_time = 0
    frame_number = 0
    old_filename = video_file_path.rsplit('\\', 1)[-1]
    old_extension = os.path.splitext(video_file_path)[1]
    new_filename = old_filename.replace(old_extension, '.jpg')
    video = (mp.VideoFileClip(video_file_path))
    color = style.bcolors()

    for frame in video.iter_frames():
        # Create an image from a frame every 1/10 of a second.
        frame_time += 0.10
        frame_number += 1

        while True:
            if os.path.isfile(f'assets/frames/{frame_number}-{new_filename}'):
                overwrite = input(f'File \'assets/frames/{frame_number}-{new_filename}\' already exists. Overwrite ? [y/N] ')
                if overwrite.upper() == 'Y':
                    video.save_frame(f'assets/frames/{frame_number}-{new_filename}', t=frame_time)
                    print(f'{color.OKGREEN}Overwriting - done{color.ENDC}')
                    print('Creating image from frame ' + str(round(frame_time, 2)))
                    break
                elif overwrite.upper() == 'N':
                    print(f'{color.FAIL}Not overwriting - exiting{color.ENDC}')
                    break
                else:
                    os.system('cls')
                    print(f'{color.FAIL}Invalid input!{color.ENDC}')
                    continue
            else:
                video.save_frame(f'assets/frames/{frame_number}-{new_filename}', t=frame_time)
                print('Creating image from frame ' + str(round(frame_time, 2)))
                break
