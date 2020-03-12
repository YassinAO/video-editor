'''
This function gives you the possibility to 
export the video audio to a mp3 file.
'''

import os


def export_audio(video_file_path):
    old_filename = video_file_path.rsplit('\\', 1)[-1]
    old_extension = os.path.splitext(video_file_path)[1]
    new_filename = old_filename.replace(old_extension, '.mp3')

    os.system(f'ffmpeg -i {video_file_path} -vn assets/audio/{new_filename}')
