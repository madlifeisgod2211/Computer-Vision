import cv2
import numpy as np
from matplotlib import pyplot as plt
from numpy.core.fromnumeric import size

#SOURCE IMAGE
img = cv2.imread('lena.jpg',0)
row,col = img.shape
cv2.imshow('Source Image',img)


#BINARY IMAGE USING OTSU
ret,binary = cv2.threshold(img,0,255,cv2.THRESH_OTSU)
cv2.imshow('Binary Image',binary)
c = cv2.waitKey(0)

#CREATE STRUCTURING ELEMENT
def Str_Elmt():
    n = int(input("Enter structuring element: "))
    str_elmt = np.ones((n,n),np.uint8)*255
    center = n // 2
    return str_elmt,center,n

#DILATION
def Dilation(img, center):
    d_img = np.copy(img)*0
    for i in range(center,row - center + 1):
        for j in range(center,col - center + 1):
            if img[i][j] == 255:
                d_img[i - center:i+center+1, j - center: j + center + 1] = 255
    return d_img

#EROSION
def Erosion(img, center, n):
    e_img = img.copy()
    for i in range(center, row - center + 1 ):
        for j in range(center, col - center + 1):
            if img[i,j] == 255:
                if np.any(img[i - center: i+center+1,j - center:j+center +1] == 0):
                    e_img[i][j] = 0
    return e_img

def Opening(img,center,n):
    o_img = np.copy(img)
    o_img = Erosion(img,center,n)
    o_img = Dilation(img,center)
    return o_img

if c == ord('x'):
    cv2.destroyAllWindows()

#DILATION
if c == ord('d'):
    kernel,center,size = Str_Elmt()
    dilation = Dilation(binary, center)
    cv2.imshow('Dilating Image', dilation)
    c = cv2.waitKey(0)
    if c == ord('d'):
        cv2.destroyWindow('Dilating Image')
    cv2.waitKey(0)

#EROSION
if c == ord('e'):
    kernel, center, size = Str_Elmt()
    erosion = Erosion(binary, center, size)
    cv2.imshow('Erosion Image',erosion)
    cv2.waitKey(0)
    c = cv2.waitKey(0)
    if c == ord('e'):
        cv2.destroyWindow('Erosion Image')
    cv2.waitKey(0)

#OPENING
if c == ord('o'):
    kernel, center, size = Str_Elmt()
    opening = Opening(binary, center, size )
    cv2.imshow('Opening Image', opening)
    cv2.waitKey(0)
    if c == ord('o'):
        cv2.destroyWindow('Opening Image')
cv2.waitKey(0)
