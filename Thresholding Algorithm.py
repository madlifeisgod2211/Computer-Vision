import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('Church.jpg', 0)
cv2.imshow('Source Image', img)
c = cv2.waitKey(0)

def Thresholding_Manual(gray_img, K_value):
    row,col = gray_img.shape
    y = np.zeros((row,col))
    for i in range(row):
        for j in range(col):
            if gray_img[i][j] >=  K_value:
                y[i][j] = 255
            else: 
                y[i][j] = 0
    return y

def Hist(img):
   row, col = img.shape 
   y = np.zeros(256)
   for i in range(0,row):
      for j in range(0,col):
         y[img[i,j]] += 1
   x = np.arange(0,256)
   plt.bar(x, y, color='b', width=5, align='center', alpha=0.25)
   plt.show()
   return y

def countPixels(img):
    row, col = img.shape
    count = 0
    for i in range(row):
        for j in range(col):
            count += 1
    return count

def weight(s,e):
    w = 0 
    for i in range(s,e):
        w += 1
    return w


if c == ord('x') or c == 0xff:
    cv2.destroyAllWindows()

elif c == ord('t'):
    binary_img = Thresholding_Manual(img, K_value = 109)
    cv2.imshow('Thesholding Image', binary_img)
    cv2.waitKey(0)

elif c == ord('r'):
    T_mean, thresh = cv2.threshold(img, 100, 200, cv2.THRESH_OTSU)
    print("T mean value is: ", T_mean)
    cv2.imshow('aaa',thresh)
    cv2.waitKey(0)

elif c == ord('h'):
    plt.hist(img,256)

cv2.destroyAllWindows()
        

    
