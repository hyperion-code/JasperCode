 #3/31/19
 #Ian Switzer, HyperIon
 #Just A Stupidly Persistent Robot
import imutils
import cv2
import numpy as np
def crop_image(img,minX,minY,maxX,maxY,w):
    cropped= img[minY:maxY, minX:maxX];
    cropped = imutils.resize(cropped, width=w)
    cv2.rectangle(img, (minX, minY), (maxX,maxY), (255, 0,0),1,8,0)
    cv2.putText(img, "Region of Interest", (minX, minY - 10),
        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
    return cropped

def conv_image(img,threshold_top,threshold_diff):    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    canny=cv2.Canny(gray, threshold1=threshold_top-threshold_diff, threshold2=threshold_top)
    return canny

def draw_lines(img, lines):
        if not(lines is None):
            for line in lines:
                coords=line[0]
                if(((coords[4]-coords[2])/(coords[3]-coords[1]))>3.14/4)
                    cv2.line(img, (coords[0],coords[1]),\
                             (coords[2],coords[3]),[255,255,255],3)
def lines_to_rect(lines):
    for line in lines:
        x1=coords[0]
        y1=coords[1]
        x2=coords[3]
        y2=coords[4]
        
    
    return rects