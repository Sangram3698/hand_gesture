import cv2
import numpy as np

cap=cv2.VideoCapture(0)
while True:
  ret,frame=cap.read()
  frame1=cv2.flip(frame,1)
  cv2.imshow("image",frame1)
  if cv2.waitKey(1)==ord('q'):
    break
cap.release()
cv2.destroyAllWindows()