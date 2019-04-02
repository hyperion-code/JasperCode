 #3/31/19
 #Ian Switzer, HyperIon
 #Just A Stupidly Persistent Robot
import imutils
import cv2
import numpy as np
def crop_image(img,minX,minY,maxX,maxY,w):
    cropped= img[minY:maxY, minX:maxX];
#    cropped = imutils.resize(cropped, width=w)
    return cropped

def processX(image):
    threshold_diff=50
    threshold_top=100
    minX=145
    minY=70
    maxX=minX+150
    maxY=75
    scale=1
    resizeX=crop_image(image,minX,minY,maxX,maxY,int((maxX-minX)*scale))
    cannyX=conv_image(resizeX,threshold_top,threshold_diff)
    bluredX=cv2.GaussianBlur(cannyX,(5,5),0)
    lines=cv2.HoughLinesP(bluredX,1,np.pi/180,1,1,1);
    x=lines_to_x(lines)+minX
    return x
#    cv2.rectangle(img, (minX, minY), (maxX,maxY), (255, 0,0),2,8,0)
#    cv2.putText(img, "Region of Interest X", (minX, minY + 20),
#        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
def processY(image,x):
    if(x.size>=2 and (x[1]-x[0])>2):
        x_mid=(x[1]-x[0])/2+x[0]
        threshold_diff=10
        threshold_top=100
        minX=int(x_mid-6)
        minY=70
        maxX=int(x_mid+6)
        maxY=500
        scale=1
        resizeY=crop_image(image,minX,minY,maxX,maxY,int((maxX-minX)*scale))
        cannyY=conv_image(resizeY,threshold_top,threshold_diff)
        bluredY=cv2.GaussianBlur(cannyY,(5,5),0)
        lines=cv2.HoughLinesP(bluredY,rho=1,theta=np.pi/180,threshold=1,minLineLength=5,maxLineGap=5)
        y=lines_to_y(lines)+minY
        cv2.imshow("Canny", cannyY)
        y=np.array([y[0],y[0]+95])
        y=y+30
        return y
    
    
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

def lines_to_y(lines):
    if not(lines is None):
        rawY=np.array([])
        processedY=np.array([])
        for line in lines:
            coords=line[0]
            if(np.abs(np.arctan((coords[3]-coords[1])/(coords[2]-coords[0])))<np.pi/2.5 or 1==1):
                    rawY=np.append(rawY,coords[3])
        rawY=np.sort(rawY, axis=None)
        last_coord=-50
        for coord in rawY:
            if coord>(last_coord+50)and processedY.size<2:
                processedY=np.append(processedY,coord)
                last_coord=coord
        return processedY
    else:
        return np.array([250,250+60])

def draw_overlay(image,x,y):
    cv2.rectangle(image, (65, 60), (395,520), (255, 0,0),1,8,0)
    draw_pipes(image, x,y)

def draw_pipes(img, x, y):
    if(x.size>=2 and y.size>=1):
        cv2.rectangle(img, (int(x[0]), 60), (int(x[1]),int(y[0])), (0, 255,00),2,8,0)
        cv2.rectangle(img, (int(x[0]), 520), (int(x[1]),int(y[1])), (0, 255,0),2,8,0)

