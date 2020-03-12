'''
This function gives you the possibility to 
replace the video audio.
'''

import os


def replace_audio(video_file_path, audio_file_path):
    old_filename = video_file_path.rsplit('\\', 1)[-1]
    old_extension = os.path.splitext(video_file_path)[1]
    new_filename = old_filename.replace(old_extension, '.mp4')

    os.system(f'ffmpeg -i {video_file_path} -i {audio_file_path} -map 0:0 -map 1:0 -c:v copy -c:a aac -b:a 256k -shortest assets/videos/{new_filename}')
