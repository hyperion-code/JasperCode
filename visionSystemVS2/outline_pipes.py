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
    cv2.rectangle(image, (50, 60), (int(walls[1]),185), (255, 0,0),1,8,0)
    minX=145
    minY=70
    maxX=295
    maxY=75

    scale=1
    resize=crop_image(image,minX,minY,maxX,maxY,int((maxX-minX)*scale))
    canny=conv_image(resize,threshold_top,threshold_diff)
    blured=cv2.GaussianBlur(canny,(5,5),0)
    lines=cv2.HoughLinesP(blured,1,np.pi/180,1,1,1);
    x=lines_to_x(lines)+minX
    resize=imutils.resize(resize, width=400)
    print(x)
    draw_pipes(image, x)
    cv2.imshow("Image", image)
    canny=imutils.resize(canny, width=600)
    cv2.imshow("Canny", canny)
    key = cv2.waitKey(1) & 0xFF
    rawCapture.truncate(0)
    print("FPS: "+str(1/(time.time()-last_time)))
    # if the `q` key was pressed, break from the loop
    if key == ord("q"):
        break