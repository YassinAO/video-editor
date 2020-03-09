# Python Video-Editor

## About
This video-editor has many functionalities that can be used to edit/manipulate videos, 
it's making use of the [MoviePy](https://github.com/Zulko/moviepy) module to get most of the work done.

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
* Add watermark to video
* Export video frames to images
* Create gif out of video timeframes
* Split video into multiple parts (Currently only working on linux)
* Concatenate videos
* Convert video extension
* Manipulate audio volume
* Replace audio
* export audio to mp3 file

## Future functionalities
* Add text to gif
