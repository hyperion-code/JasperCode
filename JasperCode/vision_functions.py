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
    threshold_diff=10
    threshold_top=100

    xminX=155
    xminY=485
    xmaxX=xminX+155
    xmaxY=xminY+5
    scale=1
    resizeX=crop_image(image,xminX,xminY,xmaxX,xmaxY,int((xmaxX-xminX)*scale))
    gray = cv2.cvtColor(resizeX, cv2.COLOR_BGR2GRAY)
    bluredX=cv2.GaussianBlur(gray,(5,5),0)
    cannyX=cv2.Canny(gray, threshold1=threshold_top-threshold_diff, threshold2=threshold_top)
    cannyr=imutils.resize(cannyX, width=600)
    lines=cv2.HoughLinesP(cannyX,rho=1,theta=np.pi/180,threshold=1,minLineLength=1,maxLineGap=1)
    x=lines_to_x(lines)+xminX
    return x


def processY(image,x):
        #Find the Y Coordinates of the pipe mouthes
    if(x.size>=2 and (x[1]-x[0])>2):
        x_mid=x[0]+25
        threshold_diff=10
        threshold_top=100
        minX=int(x_mid-6)
        minY=100
        maxX=int(x_mid+6)
        maxY=450
        scale=1
        resizeY=crop_image(image,minX,minY,maxX,maxY,int((maxX-minX)*scale))
        gray = cv2.cvtColor(resizeY, cv2.COLOR_BGR2GRAY)
        bluredY=cv2.GaussianBlur(gray,(5,5),0)
        cannyY=cv2.Canny(bluredY, threshold1=threshold_top-threshold_diff, threshold2=threshold_top)
        bluredY=cv2.GaussianBlur(cannyY,(5,5),0)
        lines=cv2.HoughLinesP(bluredY,rho=1,theta=np.pi/180,threshold=1,minLineLength=5,maxLineGap=5)
        y=lines_to_y(lines)+minY
        #cv2.imshow("Canny", cannyY)
        y=np.array([y[0]-95,y[0]])
        y=y-30
        return y
    
def findBird(img):
    minX=152
    minY=70
    maxX=153
    maxY=450
    scale=1
    resizeY=img[minY:maxY, minX:maxX]
    miny=500
    maxy=0
    pos=285
    for i,layer in enumerate(resizeY):
        for pixel in (layer):
            r=pixel[0]
            b=pixel[1]
            g=pixel[2]
            R=130
            G=175
            B=115
            T=40
            if(r>R-T and r<R+T):
                if( b>B-T and b<B+T):
                    if(g>G-T and g<G+T):
                        if(i<miny):
                            miny=i
                        if(i>maxy):
                            maxy=i
    if(miny<maxy):
        pos=int((maxy-miny)/2+miny)
    else:
        print("lost bird")
    return pos+minY-10



