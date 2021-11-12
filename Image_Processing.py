#Import OpenCV library
import cv2
import numpy as np
from matplotlib import pyplot as plt


#Convert into gray image
def gray_scale(img):
    for i in range(img.shape[1]):
        for j in range(img.shape[0]):
            (B, G, R) = img[i][j]
            img[i][j] = [R*0.229 + B*0.114 + G*0.587]
    return img

#Crop image
def crop_img(img):
    while(True):
        x = input("Enter the first coordinate: ").split()
        y = input("Enter the second coordinate: ").split()
        if (int(x[0])  < int(x[1]) <= int(img.shape[1]) ) and ( int(y[0]) < int(y[1]) <= img.shape[0]):
            break
        else:
            print("Enter coordinates again !! ")
    return img[int(x[0]):int(x[1]), int(y[0]):int(y[1])]

#Thresholding mode
def thresholding_mode(modes):
    mode = {
                1: cv2.THRESH_BINARY,
                2: cv2.THRESH_BINARY_INV,
                3: cv2.THRESH_MASK,
                4: cv2.THRESH_OTSU,
                5: cv2.THRESH_TOZERO,
                6: cv2.THRESH_TOZERO_INV,
                7: cv2.THRESH_TRIANGLE,
                8: cv2.THRESH_TRUNC
            }
    return mode.get(modes, "Enter mode again")

#Thresholding Histogram
def threshold_histogram(img, mode, thresh):

    images = [img, 0, thresh]
    titles = ['Histogram']
    plt.subplot(images)
    plt.title(titles)
    plt.show()


#--------------------------- MAIN PROGRAM --------------------------------
while (True):

    source = 'Church.jpg'

    img = cv2.imread(source,1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Image',img)
    c = cv2.waitKey(0)
    if c == ord('x'):
        break
    
    #CONVERT GRAYSCALE IMAGE
    elif c == ord('g'):
        gray_img = gray_scale(img)
        cv2.imshow('Gray image', gray_img)
        c = cv2.waitKey(0)
        if c == ord('g'):
            cv2.destroyWindow('Gray image')
        
    #CROP IMAGE
    elif c == ord('c'):
        cropped_img = crop_img(img)
        cv2.imshow('Cropped image', cropped_img)
        cv2.waitKey(0)
        if c == ord('c'):
            cv2.destroyWindow('Cropped image')
    
    #SIMPLE THRESHOLDING
    elif c == ord('t'):
        
        while True: 
            #Enter the value range
            x = int(input("Enter the first value: "))
            y = int(input("Enter the second value: "))

            #Enter thresholding mode
            print("Note that \n Mode 1: BINARY \n Mode 2: BINARY_INV \n Mode 3: TRUNC \n Mode 4: TOZERO \n Mode 5: TOZERO_INV")
            mode = int(input("Enter the thresholding mode: "))

            #Condition
            if (mode >= 0) and (mode <= 8):
                break
            else: 
                print("Enter mode again !! ")
        #MODE
        T_mean, binary_img = cv2.threshold(gray, x, y, thresholding_mode(mode))
        print("T mean value is: ", T_mean)
        cv2.imshow('Binary image', binary_img)

        print("PRESS H TO SHOW THRESHOLD HISTOGRAM !! ")
        cv2.waitKey(0)
        if c == ord('t'):
            cv2.destroyWindow('Binary image')

    #ADAPTIVE THRESHOLDING
    elif c == ord('a'):
        adaptive_mean = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 199,3)
        adaptive_gaussian = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,199, 3)
        cv2.imshow('Adaptive Mean Thresholding',adaptive_mean)
        cv2.imshow('Adaptive Gaussian Thresholding',adaptive_gaussian)
        cv2.waitKey(0)
        if c == ord('a'):
            cv2.destroyWindow('Adaptive Mean Thresholding')
            cv2.destroyWindow('Adaptive Gaussian Thresholding')

    #MORPHOLOGICAL OPERATIONS: EROSION
    elif c == ord('e'):
        n = int(input("Enter the size of kernel matrix: "))
        kernel = np.ones((n,n), np.uint8)
        img_erosion = cv2.erode(gray, kernel, iterations= 1)
        cv2.imshow('Erosion Image', img_erosion)
        cv2.waitKey(0)
        if c == ord('e'):
            cv2.destroyWindow('Erosion Image')
        
    #MORPHOLOGICAL OPERATIONS: DILATION
    elif c == ord('d'):
        n = int(input("Enter the size of kernel matrix: "))
        kernel = np.ones((n,n), np.uint8)
        img_dilation = cv2.dilate(gray, kernel, iterations= 1)
        cv2.imshow('Dilation Image', img_dilation)
        cv2.waitKey(0)
        if c == ord('d'):
            cv2.destroyWindow('Dilation Image')
    

#cv2.destroyAllWindows()
            


