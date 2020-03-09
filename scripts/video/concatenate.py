'''
This function gives you the possibility to 
concatenate multiple videos.

TODO Make the user re-enter the video path when a wrong path has been given.
TODO Change exported filename.
'''

import os
import moviepy.editor as mp

videos = []

def create_concatenation():
    red_text  = '\033[31m'
    white_text = '\033[0m'
    green_text = '\033[92m'
    
    while True:
        try:
            video_amount = int(input('Enter amount of videos: '))
            break
        except ValueError:
            os.system('cls')
            print(f'{red_text}Input is invalid!{white_text}')

    num = 0
    for _ in range(int(video_amount)):
        num += 1
        video_file_path = input('Enter full path to video file ' + str(num) + ': ')

        if os.path.exists(video_file_path):
            videos.append(mp.VideoFileClip(video_file_path))
        else:
            os.system('cls')
            print(f'{red_text}File doesn\'t exist in this directory!{white_text}')

    old_filename = video_file_path.rsplit('\\', 1)[-1]
    old_extension = os.path.splitext(video_file_path)[1]
    new_filename = 'merged-' + old_filename.replace(old_extension, '.mp4')
    print(new_filename)

    # final_clip = mp.concatenate_videoclips(videos, method='compose')

    # final_clip.write_videofile(f'assets/videos/{new_filename}')
