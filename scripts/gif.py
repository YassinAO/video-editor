'''
This function gives you the possibility to 
create a gif from a video, by giving a start and end time.
'''

import moviepy.editor as mp
import os

def time_symetrize(video_clip):
    return mp.concatenate([video_clip, video_clip.fx(mp.vfx.time_mirror)])

def create_gif():
    # Give user the option to create a gif out of the video.

    gif_size = float(input('''
    Enter size of gif\n
    Make sure to enter a number between the following ranges!
    0.1 - 0.3 = small size
    0.4 - 0.7 = medium size 
    0.8 - 1.0 = large size
    '''))

    file_path = input('Enter path to file: ')

    # Used to rename the new file to .gif
    index= file_path.rsplit('\\', 1)[-1]  
    new_filename = index.replace('.mp4', '.gif')

    start_time = int(input('Enter start time: '))
    end_time = int(input('Enter end time: '))

    video = (mp.VideoFileClip(file_path)
            .subclip(start_time, end_time)
            .resize(gif_size)
            .fx(time_symetrize))  # Returns the clip played forward then backwards

    final_gif = mp.CompositeVideoClip([video])
    final_gif.write_gif('assets/gifs/' + new_filename)
    