import moviepy.editor as mp
import os

red_text  = '\033[31m'
white_text = '\033[0m'
green_text = '\033[92m'

def manipulate_audio():
    video_file_path = input('Enter full path to video file: ')
    volume_support = list(range(1, 101))
    type_support = ['increase', 'decrease']
    base_volume = 1

    # Make sure that the user provides a video file.
    if os.path.isfile(video_file_path):
        if video_file_path.lower().endswith(('.mp4', '.mkv', '.mov')):
            print(f'{green_text}Video file has been found!{white_text}')
        else:
            os.system('cls')
            print(f'{red_text}File isn\'t a video extension! (e.g.) .mp4 .mkv .mov{white_text}')
            manipulate_audio()   
    else:
        os.system('cls')
        print(f'{red_text}Video file doesn\'t exist in this directory!{white_text}')
        manipulate_audio()

    while True:
        audio_type = input('''
currently supported audio options
increase
decrease
Enter preferred audio option: ''')

        if audio_type in type_support:
            break
        else:
            os.system('cls')
            print(f'{red_text}Choose one of the supported audio types!{white_text}')

    while True:
        audio_volume = input('''
Enter a volume percentage number between 1 and 100
Enter preferred increase/decrease volume percentage: ''')

        if audio_volume in str(volume_support):
            if audio_type == 'increase':
                new_volume = base_volume + int(audio_volume) / 100
                os.system(f'ffmpeg -i {video_file_path} -filter:a "volume={new_volume}" output.mp4')
            elif audio_type == 'decrease':
                new_volume = base_volume - int(audio_volume) / 100
                os.system(f'ffmpeg -i {video_file_path} -filter:a "volume=-{new_volume}" output.mp4')
            break
        else:
            os.system('cls')
            print(f'{red_text}Choose a volume percentage between 1 and 100!{white_text}')
