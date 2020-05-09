# Python Video-Editor

## About
This video-editor has many functionalities that can be used to edit/manipulate your videos.
Libraries/modules such as [MoviePy](https://github.com/Zulko/moviepy) and [FFMPEG](https://github.com/FFmpeg/FFmpeg) are being used to get most of the work done.

Feel free to make use of this project!

## prerequisite
* MoviePy
* FFMPEG
* PyGame (If you want to see previews)
* ImageMagick (If you want to add text to gifs)

    ### Notes
    Imagemagick is automaticly detected by MoviePy except on Windows systems.
    Navigate to `moviepy/config_defaults.py` and provide the path to the IMAGEMAGICK_BINARY named convert. See example below!

    IMAGEMAGICK_BINARY = `"C:\\Program Files\\ImageMagick_VERSION\\convert.exe"`

## Install & usage
```
$ git clone https://github.com/Y4SSIN/video-editor
$ cd video-editor  
$ pip install moviepy ffmpeg pygame
$ python editor.py
```

## Current functionalities
* Add watermark to video (choose size and position)
* Export video frames to images
* Create gif from video (choose size and specify timeframes)
* Split video into multiple parts (choose amount of split parts)
* Concatenate videos (choose amount of merged videos)
* Convert video extension (choose preffered extension e.g. mp3, mkv, mov)
* Manipulate video audio (choose increase or decrease volume percentage)
* Replace video audio (choose new audio file)
* Export video audio to mp3 file

## Future functionalities
* Add text to gif (choose size, position, font and color)
* Many more!
