import cv2
import numpy as np

image = cv2.imread("D:\Photos\WhatsApp Image 2023-07-28 at 11.15.02 PM.jpeg", cv2.IMREAD_GRAYSCALE)

equalized_image = cv2.equalizeHist(image)

cv2.imshow('Original Image', image)
cv2.imshow('Equalized Image', equalized_image)

cv2.waitKey(0)  
cv2.destroyAllWindows()  
