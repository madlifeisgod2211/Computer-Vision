import cv2
import numpy as np

img = cv2.imread("D:\Python_Learning\Computer Vision\Images\Images\lena.jpg", 0)
_, th1 = cv2.threshold(img, 0, 255, cv2.THRESH_OTSU)
_, th2 = cv2.threshold(img, 100, 255, cv2.THRESH_OTSU)
_, th3 = cv2.threshold(img, 200, 255, cv2.THRESH_OTSU)


cv2.imshow("Image", img)
cv2.imshow("th1", th1)
cv2.imshow("th2", th2)
cv2.imshow("th3", th3)



cv2.waitKey(0)
cv2.destroyAllWindows()
