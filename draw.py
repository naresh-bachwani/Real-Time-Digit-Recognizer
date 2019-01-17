import cv2
import numpy as np
from evaluate import *
global img_path 
img_path ='Image.png'

windowName = 'Drawing Demo'
img = np.zeros((256, 256, 3), np.uint8)
img=cv2.bitwise_not(img)

cv2.namedWindow(windowName)

# true if mouse is pressed
drawing = False

# if True, draw rectangle. Press 'm' to toggle to curve
mode = False
(ix, iy) = (-1, -1)

# mouse callback function
def draw_shape(event, x, y, flags, param):
    global ix, iy, drawing, mode

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        (ix, iy) = x, y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            cv2.circle(img, (x, y), 5, (0, 0, 0), -1)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.circle(img, (x, y), 5, (0, 0, 0), -1)

cv2.setMouseCallback(windowName, draw_shape)

def main():
    global mode
    print (img.shape)
    while(True):
        cv2.imshow(windowName, img)
        
        k = cv2.waitKey(1)
        if k == 13:
            cv2.imwrite('Image.png',img)
            break

    cv2.destroyAllWindows()
    process(img_path)

if __name__ == "__main__":
    main()