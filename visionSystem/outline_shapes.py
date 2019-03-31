# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import imutils
# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.rotation = 270
camera.resolution = (480, 640)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(480, 640))
 
# allow the camera to warmup
time.sleep(0.1)
 
# capture frames from the camera
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    # grab the raw NumPy array representing the image, then initialize the timestamp
    # and occupied/unoccupied text
    
    image = frame.array
    resized = image[45:600, 60:400]
    resized = imutils.resize(resized, width=300)
    gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    thresh = cv2.adaptiveThreshold(blurred,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv2.THRESH_BINARY,5,2)
    cann=cv2.Canny(blurred, threshold1=200, threshold2=400)


    cv2.imshow("Image", resized)
    # show the frame
    #cv2.imshow("Frame", thresh)
    key = cv2.waitKey(1) & 0xFF
 
    # clear the stream in preparation for the next frame
    rawCapture.truncate(0)
 
    # if the `q` key was pressed, break from the loop
    if key == ord("q"):
        break
