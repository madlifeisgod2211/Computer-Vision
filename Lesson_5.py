import cv2
import numpy as np

#Resize
while True:

        #Display an image with color mode
        img = cv2.imread('Images/Church.jpg', 1)
        cv2.imshow('Image', img)

        #Keyboard interrupt
        c = cv2.waitKey(0)

        #Press X to exist the loop
        if c == ord('x'):
            break

        if c == ord('c'):
            img_resize= cv2.resize(img,None, fx = 0.6, fy = 0.6, interpolation=cv2.INTER_LINEAR)
            cv2.imshow('Resized Image', img_resize)
            c = cv2.waitKey(0)

cv2.destroyAllWindows()
