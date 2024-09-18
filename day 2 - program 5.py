import cv2
import numpy as np

def add_watermark(image_path, watermark_text, output_path):
    img = cv2.imread(image_path)

    if img is None:
        print("Error: Could not load image!")
        return
    watermarked_img = img.copy()
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 1
    font_color = (255, 255, 255)  
    font_thickness = 2
    text_size, _ = cv2.getTextSize(watermark_text, font, font_scale, font_thickness)
    
    text_x = watermarked_img.shape[1] - text_size[0] - 10
    text_y = watermarked_img.shape[0] - 10

    cv2.putText(watermarked_img, watermark_text, (text_x, text_y), font, font_scale, font_color, font_thickness, cv2.LINE_AA)

    cv2.imwrite(output_path, watermarked_img)

    cv2.imshow('Original Image', img)
    cv2.imshow('Watermarked Image', watermarked_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

add_watermark("D:\Photos\WhatsApp Image 2023-07-28 at 11.15.02 PM.jpeg", 'Sample Watermark', 'watermarked_image.jpg')
