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

def lines_to_x(lines):
    if not(lines is None):
        rawX=np.array([])
        processedX=np.array([])
        for line in lines:
            coords=line[0]
            if(np.abs(np.arctan((coords[3]-coords[1])/(coords[2]-coords[0])))>np.pi/2.15):
                    rawX=np.append(rawX,coords[0])
        rawX=np.sort(rawX, axis=None)
        last_coord=-100
        for coord in rawX:
            if coord>(last_coord+30)and processedX.size<4:
                processedX=np.append(processedX,coord)
            last_coord=coord
        if processedX.size==1:
            if processedX[0]>75:
                processedX=np.append(processedX,processedX[0]+55)
            else:
                processedX=np.insert(processedX,0,processedX[0]-55)
        return processedX
    else:
        return np.array([150,150+55])
                    
def draw_pipes(img, walls):
    if(walls.size>=2):
        cv2.rectangle(img, (int(walls[0]), 60), (int(walls[1]),185), (255, 0,0),1,8,0)
        #cv2.rectangle(img, (int(walls[2]), 520), (int(walls[3]),375), (255, 0,0),1,8,0)

def find_gap(lines):
    #for line in lines:
    rect=0;   
    return rect