import moviepy.editor as mp
import os

red_text  = '\033[31m'
white_text = '\033[0m'
green_text = '\033[92m'

def replace_audio():
    video_file_path = input('Enter full path to video file: ')
    old_filename = video_file_path.rsplit('\\', 1)[-1]
    old_extension = os.path.splitext(video_file_path)[1]
    new_filename = old_filename.replace(old_extension, '.mp4')

    # Make sure that the user provides a video file.
    if os.path.isfile(video_file_path):
        if video_file_path.lower().endswith(('.mp4', '.mkv', '.mov')):
            print(f'{green_text}Video file has been found!{white_text}')
        else:
            os.system('cls')
            print(f'{red_text}File isn\'t a video extension! (e.g.) .mp4 .mkv .mov{white_text}')
            replace_audio()  
    else:
        os.system('cls')
        print(f'{red_text}Video file doesn\'t exist in this directory!{white_text}')
        replace_audio() 

    audio_file_path = input('Enter full path to audio file: ')

    # Make sure that the user provides an audio file.
    if os.path.isfile(audio_file_path):
        if audio_file_path.lower().endswith(('.mp3')):
            print(f'{green_text}Audio file has been found!{white_text}')
        else:
            os.system('cls')
            print(f'{red_text}File isn\'t an audio extension! \n(e.g.) .mp3{white_text}')
            replace_audio() 
    else:
        os.system('cls')
        print(f'{red_text}Audio file doesn\'t exist in this directory!{white_text}')
        replace_audio() 

    os.system(f'ffmpeg -i {video_file_path} -i {audio_file_path} -map 0:0 -map 1:0 -c:v copy -c:a aac -b:a 256k -shortest assets/videos/{new_filename}')
