import cv2  
import numpy as np 
kernel = np.ones((5, 5), np.uint8)
print(kernel)
path = "D:\Photos\WhatsApp Image 2023-07-28 at 11.15.02 PM.jpeg"
img = cv2.imread(path)
if img is None:
    print("Error: Could not read the image.")
else:
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow("GrayScale", imgGray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
