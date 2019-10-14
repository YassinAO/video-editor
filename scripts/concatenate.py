'''
This function gives you the possibility to 
concatenate multiple videos.

'''

import os
import moviepy.editor as mp

videos = []

def merge():

    while True:
        try:
            video_amount = int(input('Enter amount of videos: '))
            break
        except ValueError:
            os.system('cls')
            print('Invalid input')
            
    num = 0
    for _ in range(int(video_amount)):
        num += 1
        file_path = input('Enter path to file ' + str(num) + ': ')

        if os.path.exists(file_path):
            videos.append(mp.VideoFileClip(file_path))
        else:
            print('File not found')

    index= file_path.rsplit('\\', 1)[-1]
    new_filename= 'merged-' + index

    final_clip = mp.concatenate_videoclips(videos, method='compose')
    final_clip.write_videofile('assets/videos/' + new_filename)