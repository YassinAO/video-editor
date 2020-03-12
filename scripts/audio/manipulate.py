'''
This function gives you the possibility to 
increase or decrease the audio volume.
'''

import os


def manipulate_audio(video_file_path):
    volume_support = list(range(1, 101))
    type_support = ['increase', 'decrease']
    base_volume = 1

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
            print(f'{color.FAIL}Choose one of the supported audio types!{color.ENDC}')
            continue

    while True:
        audio_volume = input('''
Enter a volume percentage number between 1 and 100
Enter preferred increase/decrease volume percentage: ''')

        if audio_volume in str(volume_support):
            if audio_type == 'increase':
                new_volume = base_volume + int(audio_volume) / 100
                os.system(f'ffmpeg -i {video_file_path} -filter:a "volume={new_volume}" assets/videos/audio-{audio_type}-{str(audio_volume)}-output.mp4')
            elif audio_type == 'decrease':
                new_volume = base_volume - int(audio_volume) / 100
                os.system(f'ffmpeg -i {video_file_path} -filter:a "volume=-{new_volume}" assets/videos/audio-{audio_type}-{str(audio_volume)}-output.mp4')
            break
        else:
            os.system('cls')
            print(f'{color.FAIL}Choose a volume percentage between 1 and 100!{color.ENDC}')
            continue
