import cv2

image = cv2.imread("D:\Photos\WhatsApp Image 2023-07-28 at 11.15.02 PM.jpeg")
rotated_image = cv2.flip(image, 1) 

cv2.imshow('Original Image', image)
cv2.imshow('180-Degree Rotated Image', rotated_image)
cv2.waitKey(0) 
cv2.destroyAllWindows()
