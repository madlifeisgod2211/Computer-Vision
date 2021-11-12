import numpy as np
import cv2

#CAMERAS AND VIDEOCAPTURE IN OPENCV2
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    #To get the image property, 3 mean property width
    width = int(cap.get(3)) 
    height = int(cap.get(4))

    #Draw line (source image, starting position, color, line thickness)
    img = cv2.line(frame, (0,0), (width,height), (0,0,0), 10)
    img = cv2.line(frame, (width,0), (0,height), (0,0,0), 10)

    #Draw the equation
    def equation(x):
        y = x**2 + 2*x
        return y
    for i in range(0,10,0.1):
        results = equation(i)
        img = cv2.line(img, (i, results), (i,results), (0,0,0), 10)


    #Draw rectangle (source image, center position, radius, color, thickness)
    img = cv2.rectangle(img, (100,100), (200,200), (128,128,128), 5)
    
    cv2.imshow("MINH TAI'S CAMERA", img)
    #To exit the program
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()