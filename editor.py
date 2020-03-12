'''
TODO Make use of multi processing to speed up the process.
'''
from scripts import validate, style
import os


def menu_option():
    menu_numbers = list(range(1, 10))
    color = style.bcolors()

    select_option = input('''
 ------------------------------------------------
|   MENU                                         |
|                                                |
|   1 = Create a gif out of the video            |
|   2 = Add a watermark to the video             |
|   3 = Export video frames to images            |
|   4 = Split video into multiple parts          |
|   5 = Concatenate videos                       |
|   6 = Convert video extension                  |
|   7 = Increase or decrease audio volume        |
|   8 = Replace audio                            |
|   9 = Export audio to mp3                      |
 ------------------------------------------------                  
Enter preferred option: ''')

    if select_option in str(menu_numbers):
        validate.check_path(select_option)
    else:
        os.system('cls')
        print(f'{color.FAIL}Select one of the options from the menu!{color.ENDC}')
        menu_option()


menu_option()
