import cv2
import numpy as np

# if 0 didnt work try different values. ie. 1,2,3,...
cam_id = 0

cap = cv2.VideoCapture(cam_id)

while True:
    ret, I = cap.read()
    cv2.imshow("My Camera", I)
    
    # Press 'e' to exit
    if cv2.waitKey(1) & 0xFF == ord('e'):
        break 

cap.release()
cv2.destroyAllWindows()