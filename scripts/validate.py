import os
from scripts.video import gif, split, watermark, frame, concatenate, convert
from scripts.audio import export, manipulate, replace
from scripts import style, selected


def check_path(select_option):
    color = style.bcolors()
    option = selected.moptions()

    # Make sure that the user provides a video file.
    while True:
        # The concatenate function shouln't run this validation.
        if select_option != option.concatenate_video:
            video_file_path = input(f'Enter full path to video file {color.OKBLUE}(e.g. C:/Users/JohnDoe/Videos/example.mp4){color.ENDC}: ')

            if os.path.isfile(video_file_path):
                if video_file_path.lower().endswith(('.mp4', '.mkv', '.mov')):
                    print(f'{color.OKGREEN}Video file has been found!{color.ENDC}\n')
                    break
                else:
                    os.system('cls')
                    print(f'{color.FAIL}File isn\'t a video extension! (e.g. mp4 mkv mov){color.ENDC}')
                    continue
            else:
                os.system('cls')
                print(f'{color.FAIL}Video file doesn\'t exist in this directory!{color.ENDC}')
                continue
        else:
            break

    # Make sure that the user provides an image file.
    if select_option == option.add_watermark:
        while True:
            watermark_file_path = input(f'Enter full path to watermark file {color.OKBLUE}(e.g. C:/Users/JohnDoe/Images/example.jpg){color.ENDC}: ')
            if os.path.isfile(watermark_file_path):
                if watermark_file_path.lower().endswith(('.jpg', '.png', 'jpeg')):
                    print(f'{color.OKGREEN}Watermark file has been found!{color.ENDC}\n')
                    break
                else:
                    os.system('cls')
                    print(f'{color.FAIL}File isn\'t an image extension! (e.g. jpg png jpeg){color.ENDC}')
                    continue
            else:
                os.system('cls')
                print(f'{color.FAIL}Watermark file doesn\'t exist in this directory!{color.ENDC}')
                continue

    # Make sure that the user provides an audio file.
    elif select_option == option.replace_audio:
        while True:
            audio_file_path = input(f'Enter full path to audio file {color.OKBLUE}(e.g. C:/Users/JohnDoe/Audio/example.mp3){color.ENDC}: ')
            
            if os.path.isfile(audio_file_path):
                if audio_file_path.lower().endswith(('.mp3')):
                    print(f'{color.OKGREEN}Audio file has been found!{color.ENDC}\n')
                    break
                else:
                    os.system('cls')
                    print(f'{color.FAIL}File isn\'t an audio extension! (e.g. mp3){color.ENDC}')
                    continue
            else:
                os.system('cls')
                print(f'{color.FAIL}Audio file doesn\'t exist in this directory!{color.ENDC}')
                continue

    if select_option == option.create_gif:
        gif.create_gif(video_file_path)

    elif select_option == option.add_watermark:
        watermark.create_watermark(video_file_path, watermark_file_path)

    elif select_option == option.export_audio:
        frame.create_frames(video_file_path)

    elif select_option == option.split_video:
        split.create_split(video_file_path)

    elif select_option == option.concatenate_video:
        concatenate.create_concatenation()

    elif select_option == option.convert_video:
        convert.create_convertion(video_file_path)

    elif select_option == option.manipulate_video:
        manipulate.manipulate_audio(video_file_path)

    elif select_option == option.replace_audio:
        replace.replace_audio(video_file_path, audio_file_path)

    elif select_option == option.export_audio:
        export.export_audio(video_file_path)
