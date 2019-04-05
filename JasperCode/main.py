# import the necessary packages
from __future__ import print_function
from image_functions import *
from camera_interface import *
from vision_functions import *
from arduino_interface import *
from camera_interface import PiVideoStream
from imutils.video import FPS
from picamera.array import PiRGBArray
from picamera import PiCamera
import argparse
import imutils
import time
import cv2
import numpy as np

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-n", "--num-frames", type=int, default=100,
    help="# of frames to loop over for FPS test")
ap.add_argument("-d", "--display", type=int, default=-1,
    help="Whether or not frames should be displayed")
args = vars(ap.parse_args())

print("[INITIALIZATION] Starting Jaspr Flappy Bird Detection")
vs = PiVideoStream().start()
time.sleep(2.0)
fps = FPS().start()


last_time=time.time()
while 1 :
    image = vs.read()
    original=image
    x=processX(image)
    move_finger(int((x[0]-200)/(350-150)*255))
    y=processY(original,x)
    draw_overlay(image,x,y);
    cv2.imshow("Image", image)
    
    key = cv2.waitKey(1) & 0xFF
    
    if key == ord("q"):    # if the `q` key is pressed, break from the loop
        cv2.destroyAllWindows()
        vs.stop()
        break
    
    print("FPS: "+str(1/(time.time()-last_time)))
    last_time=time.time()
    

