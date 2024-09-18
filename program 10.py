import cv2
import numpy as np

def translate_image(image_path, tx, ty):
    
    image = cv2.imread(image_path)
    
    height, width = image.shape[:2]
    
    translation_matrix = np.float32([[1, 0, tx], [0, 1, ty]])
    
    translated_image = cv2.warpAffine(image, translation_matrix, (width, height))
    
    cv2.imshow('Original Image', image)
    cv2.imshow('Translated Image', translated_image)
    
    cv2.waitKey(0)  
    cv2.destroyAllWindows() 

translate_image("D:\Photos\WhatsApp Image 2023-07-28 at 11.15.02 PM.jpeg", 50, 30)
