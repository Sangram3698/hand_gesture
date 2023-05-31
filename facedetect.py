import cv2
import numpy as np

cap=cv2.VideoCapture(0)
while True:
  ret,frame=cap.read()
  width=int(cap.get(3))
  height=int(cap.get(4))
  
  img=cv2.flip(frame,1)
  gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
  haarcascade=cv2.CascadeClassifier('haarcascade_face.xml')
  faces_react=haarcascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=3)
  for (x,y,w,h) in faces_react:
    rect=cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),thickness=3)
    cv2.imshow("frame",rect) 
  if cv2.waitKey(1)==ord('q'):
    break
cap.release()
cv2.destroyAllWindows()