import cv2

def binary_thresholding(image_path, threshold_value, max_value, output_path):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    if img is None:
        print("Error: Could not load image!")
        return

    _, binary_img = cv2.threshold(img, threshold_value, max_value, cv2.THRESH_BINARY)

    cv2.imshow('Original Image', img)
    cv2.imshow('Binary Threshold Image', binary_img)

    cv2.imwrite(output_path, binary_img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

binary_thresholding("D:\Photos\WhatsApp Image 2023-07-28 at 11.15.02 PM.jpeg", 127, 255, 'binary_threshold_image.jpg')
