'''
This function gives you the possibility to 
export frames from a video and save them in your directory.

TODO Use every frame of the video for a reverse image search.

TODO Enter a  start and endtime within the commandline of which the frames should be extracted from.
'''

import os
import moviepy.editor as mp

def create_frames():
        
    file_path = input('Enter path to file: ')
    video = (mp.VideoFileClip(file_path))

    # Used to rename the new file
    index= file_path.rsplit('\\', 1)[-1]  
    new_filename = index.replace('.mp4', '')

    frametime = 0
    framenumber = 0

    try:
        for frame in video.iter_frames():
            # Create an image from a frame every 1/10 of a second.
            frametime += 0.10
            framenumber += 1
            video.save_frame(f'assets/frames/{new_filename}-{framenumber}.jpg', t=frametime)
            print('Creating image from frame ' + str(round(frametime, 2)))
    except:
        print('Process ended!')
