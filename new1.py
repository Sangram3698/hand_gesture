import cv2
import numpy as np

cap=cv2.VideoCapture(0)
while True:
  ret,frame=cap.read()
  width=int(cap.get(3))
  height=int(cap.get(4))
  img=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
  lower_col=np.array([90,50,50])
  upper_col=np.array([130,255,255])
  
  mask=cv2.inRange(img,lower_col,upper_col)
  result=cv2.bitwise_and(frame,frame,mask=mask)
  
  cv2.imshow("image",result)
  if cv2.waitKey(1)==ord('q'):
    break
cap.release()
cv2.destroyAllWindows()
