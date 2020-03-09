'''
This function gives you the possibility to 
create a gif from a video, by giving a start and end time.
'''

import moviepy.editor as mp
import os

def time_symetrize(video_clip):
    return mp.concatenate([video_clip, video_clip.fx(mp.vfx.time_mirror)])

def create_gif():
    video_file_path = input('Enter full path to video file: ')
    old_filename = video_file_path.rsplit('\\', 1)[-1]
    old_extension = os.path.splitext(video_file_path)[1]
    new_filename = old_filename.replace(old_extension, '.gif')
    size_support = ['small', 'medium', 'large']
    type_support = ['normal', 'loop']
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
            create_gif()   
    else:
        os.system('cls')
        print(f'{red_text}Video file doesn\'t exist in this directory!{white_text}')
        create_gif()
    
    while True: 
        gif_size = input('''
currently supported sizes
small
medium
large
Enter preferred size: ''')

        if gif_size in size_support:
            if gif_size == 'small':
                gif_size = 0.3
            elif gif_size == 'medium':
                gif_size = 0.5
            elif gif_size == 'large':
                gif_size = 0.7
            break
        else:
            os.system('cls')
            print(f'{red_text}Choose one of the supported sizes!{white_text}')

    while True:
        try:
            start_time = int(input('Enter start time: '))
            end_time = int(input('Enter end time: '))
            break
        except ValueError:
            os.system('cls')
            print(f'{red_text}Start or end time is invalid!{white_text}')

    while True:
        gif_type = input('''
currently supported types
normal
loop
Enter preferred type: ''')

        if gif_type in type_support:
            if gif_type == 'normal':
                video = (mp.VideoFileClip(video_file_path)
                        .subclip(start_time, end_time)
                        .resize(gif_size))

            elif gif_type == 'loop':
                video = (mp.VideoFileClip(video_file_path)
                        .subclip(start_time, end_time)
                        .resize(gif_size)
                        .fx(time_symetrize))
            break
        else:
            os.system('cls')
            print(f'{red_text}Choose one of the supported types!{white_text}')

    final_gif = mp.CompositeVideoClip([video])
    final_gif.write_gif(f'assets/gifs/{new_filename}')
