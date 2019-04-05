#3/31/19
#Ian Switzer, HyperIon
#Just A Stupidly Persistent Robot
#
#Vision functions for Flappy Bird game
#Converts an image into game information
import imutils
import cv2
import numpy as np
from image_functions import *

def processX(image):
    #Find the X Coordinates of the pipe walls
    threshold_diff=1
    threshold_top=100
    minX=145
    minY=55
    maxX=minX+150
    maxY=60
    scale=1
    resizeX=crop_image(image,minX,minY,maxX,maxY,int((maxX-minX)*scale))
    gray = cv2.cvtColor(resizeX, cv2.COLOR_BGR2GRAY)
    bluredX=cv2.GaussianBlur(gray,(5,5),0)
    cannyX=cv2.Canny(bluredX, threshold1=threshold_top-threshold_diff, threshold2=threshold_top)
    cannyr=imutils.resize(cannyX, width=600)
    cv2.imshow("cannyX", cannyr)
    lines=cv2.HoughLinesP(bluredX,rho=1,theta=np.pi/180,threshold=1,minLineLength=1,maxLineGap=1)
    x=lines_to_x(lines)+minX
    return x


def processY(image,x):
        #Find the Y Coordinates of the pipe mouthes
    if(x.size>=2 and (x[1]-x[0])>2):
        x_mid=x[0]+25
        threshold_diff=10
        threshold_top=100
        minX=int(x_mid-6)
        minY=75
        maxX=int(x_mid+6)
        maxY=500
        scale=1
        resizeY=crop_image(image,minX,minY,maxX,maxY,int((maxX-minX)*scale))
        cannyY=conv_image(resizeY,threshold_top,threshold_diff)
        bluredY=cv2.GaussianBlur(cannyY,(5,5),0)
        lines=cv2.HoughLinesP(bluredY,rho=1,theta=np.pi/180,threshold=1,minLineLength=5,maxLineGap=5)
        y=lines_to_y(lines)+minY
        #cv2.imshow("Canny", cannyY)
        y=np.array([y[0]-95,y[0]])
        y=y-30
        return y
    
   
def find_bird():
    #find the Y coordinate of the bird
    return 0

def bird_vel():
    #Finds the bird's velocity
    return 0

