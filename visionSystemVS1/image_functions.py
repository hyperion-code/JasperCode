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
    canny=cv2.Canny(gray, threshold1=threshold_top-threshold_diff, threshold2=threshold_top)
    return canny

def draw_lines(img, lines):
        next_pipe_x=100000
        if not(lines is None):
            for line in lines:
                coords=line[0]
                if(np.abs(np.arctan((coords[3]-coords[1])/(coords[2]-coords[0])))>np.pi/2.05):
                    cv2.line(img, (coords[0],coords[1]),\
                             (coords[2],coords[3]),[0,255,0],1)
            #        if(coords[0]>75):
            #            next_pipe_x=np.minimum(next_pipe_x,coords[0])
           # cv2.line(img, (next_pipe_x,0),(next_pipe_x,450),[0,0,255],1)
            #cv2.line(img, (next_pipe_x+50,0),(next_pipe_x+50,450),[0,0,255],1)
           # cv2.putText(img, "Next Pipe X: "+str(next_pipe_x-75),(next_pipe_x-100,15),\
              #          cv2.FONT_HERSHEY_PLAIN, 0.75, (255, 255, 255), 1,bottomLeftOrigin=False)
def find_gap(lines):
    #for line in lines:
    rect=0;   
    return rect