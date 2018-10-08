# Program to take a picture with the picamera and pan tilt hat control with arraw keys #

import math
import time
import curses
from time import sleep

import picamera
import pantilthat

# import cv2

# Set up
camera = picamera.PiCamera()
camera.resolution = (1024,768)
camera.start_preview()
camera.rotation = 180

screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)

pic = 1

try:
    while True:
        
        char = screen.getch()
        # Stop the program
        if char == ord('q'):
            break
        
        # Take an image
        if char == ord('p'):
            image_name = camera.capture('image%s.jpg' % pic)
            pic = pic +1
            # TODO: save in the images folder, is now in root
            # cv2.imwrite('./images', image_name)
            screen.addstr(0,0,'picture taken!')

        elif char == curses.KEY_RIGHT:
            screen.addstr(0, 0, 'right')
            pantilthat.pan(-20)

        elif char == curses.KEY_LEFT:
            screen.addstr(0, 0, 'left')
            pantilthat.pan(20)

        elif char == curses.KEY_UP:
            screen.addstr(0, 0, 'up')
            pantilthat.tilt(-20)

        elif char == curses.KEY_DOWN:
            screen.addstr(0, 0, 'down')
            pantilthat.tilt(20)
finally:
    
    # Clean everything
    curses.nocbreak()
    screen.keypad(0);
    curses.echo()
    curses.endwin()
        