import cv2 as cv
import numpy as np
cap = cv.VideoCapture(0)
while(1):
    # Take each frame
    _, frame = cap.read()
    # Convert BGR to HSV
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    # define range of blue color in HSV
    lower_blue = np.array([0,50,50])  #red
    upper_blue = np.array([10,255,255]) #red
    # Threshold the HSV image to get only blue colors
    mask = cv.inRange(hsv, lower_blue, upper_blue)
    # print(mask)

    # Bitwise-AND mask and original image
    res = cv.bitwise_and(frame,frame, mask= mask)
    x = str(res)
    #display tempreture
    window_name = 'Image'
  
    # font
    font = cv.FONT_HERSHEY_SIMPLEX
    
    # org
    org = (50, 50)
    
    # fontScale
    fontScale = 1
    
    # Blue color in BGR
    color = (255, 0, 0)
    
    # Line thickness of 2 px
    thickness = 2
    
    # Using cv.putText() method
    image = cv.putText(frame, x, org, font, 
                    fontScale, color, thickness, cv.LINE_AA)
    


    cv.imshow('frame',image)
    # cv.imshow('mask',mask)
    cv.imshow('res',hsv)
    k = cv.waitKey(5) & 0xFF
    if k == 27:
        break
cv.destroyAllWindows()