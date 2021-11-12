import cv2
import random

img = cv2.imread('Images/Church.jpg',-1)

# cv2.imshow('Image', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#Check the shape of image: high width channel
# print(img.shape)

#Check the pixel of image
print(img[0][0])

#Changing pixel colors
# for i in range(50):
#     for j in range(img.shape[1]): #(rows, columns, channels)
#         img[i][j] = [random.randint(0, 255),random.randint(0,255),random.randint(0,255) ]

#Copy a part of image
img[100:300,600:900] = 255

#Display image
cv2.imshow('Image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()



