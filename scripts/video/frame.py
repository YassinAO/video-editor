'''
This function gives you the possibility to 
export frames from a video and save them in your directory.

TODO Enter a start and endtime within the commandline of which the frames should be extracted from.
'''

import os
import moviepy.editor as mp

def create_frames():
    video_file_path = input('Enter full path to video file: ')
    old_filename = video_file_path.rsplit('\\', 1)[-1]
    old_extension = os.path.splitext(video_file_path)[1]
    new_filename = old_filename.replace(old_extension, '')
    frametime = 0
    framenumber = 0
    red_text  = '\033[31m'
    white_text = '\033[0m'
    green_text = '\033[92m'

    # Make sure that the user provides a video file.
    if os.path.isfile(video_file_path):
        if video_file_path.lower().endswith(('.mp4', '.mkv', '.mov')):
            print(f'{green_text}Video file has been found!{white_text}')
        else:
            os.system('cls')
            print(f'{red_text}File isn\'t a video extension! (e.g.) .mp4 .mkv .mov{white_text}')
            create_frames()   
    else:
        os.system('cls')
        print(f'{red_text}Video file doesn\'t exist in this directory!{white_text}')
        create_frames()

    video = (mp.VideoFileClip(video_file_path))

    try:
        for frame in video.iter_frames():
            # Create an image from a frame every 1/10 of a second.
            frametime += 0.10
            framenumber += 1

            video.save_frame(f'assets/frames/{new_filename}-{framenumber}.jpg', t=frametime)
            print('Creating image from frame ' + str(round(frametime, 2)))
    except:
        print(f'{red}Process ended!{white}')
