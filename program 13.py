import cv2

def show_coordinates(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:  
        print(f"Clicked at: ({x}, {y})")
        
        cv2.circle(image, (x, y), 3, (255, 0, 0), -1)
        cv2.putText(image, f"({x}, {y})", (x + 10, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1)
        cv2.imshow('Image', image)

image = cv2.imread("D:\Photos\WhatsApp Image 2023-07-28 at 11.15.02 PM.jpeg")

cv2.imshow('Image', image)

cv2.setMouseCallback('Image', show_coordinates)

cv2.waitKey(0)  
cv2.destroyAllWindows()  
