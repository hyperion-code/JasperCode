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
import webcolors 
def processX(image):
    #Find the X Coordinates of the pipe walls
    minX=77
    minY=20
    maxX=minX+100
    maxY=minY+1
    resizedX=image[minY:maxY, minX:maxX];
    for layer in (resizedX):
        for i,pixel in enumerate(layer):
            #print(pixel)
            r=pixel[0]
            b=pixel[1]
            g=pixel[2]
            R=70
            G=112
            B=120
            T=40
            if(r>R-T and r<R+T):
                if( b>B-T and b<B+T):
                    if(g>G-T and g<G+T):
                        return i+minX
    return 1

def processY(image,x,last):
    #Find the X Coordinates of the pipe walls
    minX=x+15
    minY=25
    maxX=minX+1
    maxY=250
    resizedX=image[minY:maxY, minX:maxX];
    for layer in (resizedX):
        for i,pixel in enumerate(layer):
            print(pixel)
            b=pixel[0]
            g=pixel[1]
            r=pixel[2]
            print(closest_colour((r,g,b)))
            B=170
            G=177
            R=70
            T=15
            if(r>R-T and r<R+T):
                if( b>B-T and b<B+T):
                    if(g>G-T and g<G+T):
                        print(i)
                        return i+minX+8
    return last


def processX_openCV(image):
    #Find the X Coordinates of the pipe walls
    threshold_diff=10
    threshold_top=100

    xminX=77
    xminY=242
    xmaxX=xminX+78
    xmaxY=xminY+3
    scale=1
    resizeX=crop_image(image,xminX,xminY,xmaxX,xmaxY,int((xmaxX-xminX)*scale))
    gray = cv2.cvtColor(resizeX, cv2.COLOR_BGR2GRAY)
    bluredX=cv2.GaussianBlur(gray,(5,5),0)
    cannyX=cv2.Canny(gray, threshold1=threshold_top-threshold_diff, threshold2=threshold_top)
    lines=cv2.HoughLinesP(cannyX,rho=1,theta=np.pi/180,threshold=1,minLineLength=1,maxLineGap=1)
    x=lines_to_x(lines)+xminX
    return x


def processY_openCV(image,x):
        #Find the Y Coordinates of the pipe mouthes
    if(x!=-1):
        x_mid=x+12
        threshold_diff=10
        threshold_top=100
        minX=int(x_mid-3)
        minY=50
        maxX=int(x_mid+3)
        maxY=225
        resizeY= image[minY:maxY, minX:maxX];
        gray = cv2.cvtColor(resizeY, cv2.COLOR_BGR2GRAY)
        bluredY=cv2.GaussianBlur(gray,(5,5),0)
        cannyY=cv2.Canny(bluredY, threshold1=threshold_top-threshold_diff, threshold2=threshold_top)
        bluredY=cv2.GaussianBlur(cannyY,(5,5),0)
        lines=cv2.HoughLinesP(bluredY,rho=1,theta=np.pi/180,threshold=1,minLineLength=3,maxLineGap=3)
        y=lines_to_y(lines)+minY
        y=np.array([y[0]-48,y[0]])
        y=y-15
        return y
    
def findBird(img,last):
    minX=74
    minY=35
    maxX=81
    maxY=225
    resizeY=img[minY:maxY, minX:maxX]
    miny=500
    maxy=0
    pos=285
    for i,layer in enumerate(resizeY):
        for pixel in (layer):
            
            b=pixel[0]
            g=pixel[1]
            r=pixel[2]
            #print(pixel)
            #print(closest_colour((r,g,b)))
            B1=150
            G1=170
            R1=180.
            
            B2=165
            G2=210
            R2=210
            T=0
            if(r>R1-T and r<R2+T):
                if( b>B1-T and b<B2+T):
                    if(g>G1-T and g<G2+T):
                        #print(pixel)
                        #print(closest_colour((r,g,b)))
                        if(i<miny):
                            miny=i
                        if(i>maxy):
                            maxy=i                        
    if(miny<=maxy):
        pos=miny
    else:
        print("lost bird")
        return last
    return pos+minY+2


def closest_colour(requested_colour):
    min_colours = {}
    for key, name in webcolors.css3_hex_to_names.items():
        r_c, g_c, b_c = webcolors.hex_to_rgb(key)
        rd = (r_c - requested_colour[0]) ** 2
        gd = (g_c - requested_colour[1]) ** 2
        bd = (b_c - requested_colour[2]) ** 2
        min_colours[(rd + gd + bd)] = name
    return min_colours[min(min_colours.keys())]
