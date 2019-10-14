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

    currentframe = 0
    framename = 0

    for frame in video.iter_frames():
        # Create an image from a frame every 1/10 of a second.
        currentframe += 0.10
        framename += 1
        video.save_frame('assets/frames/image' + str(framename) +'.jpg', t=currentframe)
        print('Creating image from frame ' + str(round(currentframe, 2)))
