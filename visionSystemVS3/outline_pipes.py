# import the necessary packages
from image_functions import *
from hardware_init import *

import cv2
import numpy as np

camera,rawCapture=initialize_camera()
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    last_time=time.time()
    
    image = frame.array
    original=image
    x=processX(image)
    y=processY(original,x)
    draw_overlay(image,x,y);
    cv2.imshow("Image", image)
    key = cv2.waitKey(1) & 0xFF
    rawCapture.truncate(0)
    print("FPS: "+str(1/(time.time()-last_time)))
    # if the `q` key was pressed, break from the loop
    if key == ord("q"):
        break