'''
This function gives you the possibility to 
concatenate multiple videos.
'''

import os
import moviepy.editor as mp

videos = []

def create_concatenation():
    red_text  = '\033[31m'
    white_text = '\033[0m'
    
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
        file_path = input('Enter full path to file ' + str(num) + ': ')

        if os.path.exists(file_path):
            videos.append(mp.VideoFileClip(file_path))
        else:
            print('File not found')

    index= file_path.rsplit('\\', 1)[-1]
    new_filename= 'merged-' + index

    final_clip = mp.concatenate_videoclips(videos, method='compose')

    final_clip.write_videofile(f'assets/videos/{new_filename}')
