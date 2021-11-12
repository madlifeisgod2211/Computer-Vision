import numpy as np
import cv2

#CAMERAS AND VIDEOCAPTURE IN OPENCV2
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    #To get the image property, 3 mean property width
    width = int(cap.get(3)) 
    height = int(cap.get(4))

    #Create a black image
    image = np.zeros(frame.shape, np.uint8)

    #Resize the image
    smaller_frame = cv2.resize(frame, (0,0), fx = 0.33333, fy = 0.33333)
    
    #To show the 9 cameras display
    image[:height//3 ,:width//3] = cv2.rotate(smaller_frame, cv2.ROTATE_180)                           #Top left
    image[height//3:height*2//3: ,:width //3] = smaller_frame              #Middle left
    image[height*2//3: ,:width //3] = smaller_frame                        #Bottome left
    image[:height//3: ,width//3 : width*2 //3] = smaller_frame             #Middle top
    image[height//3:height*2//3: ,width//3 : width*2 //3] = smaller_frame  #Center
    image[height*2//3: ,width//3 : width*2 //3] = smaller_frame            #Middle bottom
    image[:height//3 , width*2//3 + 1 : width] = smaller_frame             #Top right
    image[height//3:height*2//3: , width*2//3 + 1 :width] = smaller_frame  #Middle right
    image[height*2//3: height , width*2//3 + 1 :width] = smaller_frame     #Bottom right


    cv2.imshow("MINH TAI'S CAMERA", image)
    #To exit the program
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()