# import the necessary packages
from image_functions import *
from hardware_init import *

import cv2
import numpy as np

camera,rawCapture=initialize_camera()
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    last_time=time.time()
    threshold_diff=50
    threshold_top=100
    image = frame.array
    minX=80
    minY=50
    maxX=390
    maxY=500
    scale=.8
    resize=crop_image(image,minX,minY,maxX,maxY,int((maxX-minX)*scale))
    canny=conv_image(resize,threshold_top,threshold_diff)
    blured=cv2.GaussianBlur(canny,(5,5),0)
    lines=cv2.HoughLinesP(blured,1,np.pi,75,np.array([]),20,20);
    draw_lines(resize, lines);
    #resize=imutils.resize(resize, width=400)
    cv2.imshow("Image", resize)
    #canny=imutils.resize(canny, width=600)
    #cv2.imshow("Canny", canny)
    key = cv2.waitKey(1) & 0xFF
    rawCapture.truncate(0)
    print("FPS: "+str(1/(time.time()-last_time)))
    # if the `q` key was pressed, break from the loop
    if key == ord("q"):
        break