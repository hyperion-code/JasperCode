#3/31/19
#Ian Switzer, HyperIon
#Just A Stupidly Persistent Robot
#
#Useful custom functions for converting from/to
#CV2 function inputs/outputs and useful data

import imutils
import cv2
import numpy as np

def crop_image(img,minX,minY,maxX,maxY,w):
    cropped= img[minY:maxY, minX:maxX];
#    cropped = imutils.resize(cropped, width=w)
    return cropped
    
def lines_to_x(lines):
    #Converts a set of lines into one set of filtered X coords
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

def lines_to_y(lines):
    #Converts a set of lines into one set of filtered Y coords
    if not(lines is None):
        rawY=np.array([])
        processedY=np.array([])
        for line in lines:
            coords=line[0]
            if(np.abs(np.arctan((coords[3]-coords[1])/(coords[2]-coords[0])))<np.pi/2.5 or 1==1):
                    rawY=np.append(rawY,coords[3])
        rawY=np.sort(rawY, axis=None)
        rawY=np.flip(rawY)
        last_coord=600
        for coord in rawY:
            if coord<(last_coord-50)and processedY.size<2:
                processedY=np.append(processedY,coord)
                last_coord=coord
        return processedY
    else:
        return np.array([250,250+60])

def draw_overlay(image,x,y,bird):
    #Draws what Jasper can detect
    cv2.rectangle(image, (32, 30), (198,265), (255, 0,0),1,8,0)
    minX=77
    minY=35
    maxX=minX+100
    maxY=minY+1
    cv2.rectangle(image, (minX, minY), (maxX,maxY), (255, 0,0),1,8,0)
    cv2.rectangle(image, (x+15, 35), (x+16,260), (255, 0,0),1,8,0)
    draw_pipes(image, x,y)
    
    cv2.rectangle(image, (74, 35), (81,225), (255, 0,0),1,8,0)
    cv2.circle(image,(77,bird),7,(0, 255,255),1,8,0)


def draw_pipes(img, x, y):
    #Draws the pipes
    if(x!=-1 and y!=-1):
        cv2.rectangle(img, (x, 30), (x+30,y), (0, 255,00),2,8,0)
        cv2.rectangle(img, (x, 275), (x+30,y+46), (0, 255,0),2,8,0)
        #cv2.putText(img, "Next Pipe: (" +str(x)+","+str(y)+")", (x, y+5),
         #           cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

