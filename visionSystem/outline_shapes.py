# import the necessary packages
from image_functions import *
from hardware_init import *

import cv2
import numpy as np

camera,rawCapture=initialize_camera()
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    threshold_diff=200
    threshold_top=100
    image = frame.array
    minX=70
    minY=50
    maxX=390
    maxY=500
    resize=crop_image(image,minX,minY,maxX,maxY,300)
    canny=conv_image(resize,threshold_top,threshold_diff)
    blured=cv2.GaussianBlur(canny,(5,5),0)
    lines=cv2.HoughLinesP(blured,1,np.pi/180,100,50,50);
    draw_lines(resize, lines);
    cv2.imshow("Image", resize)
    cv2.imshow("Canny", canny)
    key = cv2.waitKey(1) & 0xFF
    rawCapture.truncate(0)
 
    # if the `q` key was pressed, break from the loop
    if key == ord("q"):
        break