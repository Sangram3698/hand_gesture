import cv2
import numpy as np

def empty(a):
  pass

cv2.namedWindow("Trackbar")
cv2.resizeWindow("Trackbar",640,240)
cv2.createTrackbar("Hue Min","Trackbar",0,179,empty)
cv2.createTrackbar("Hue Max","Trackbar",95,179,empty)
cv2.createTrackbar("Sat Min","Trackbar",78,255,empty)
cv2.createTrackbar("Sat Max","Trackbar",255,255,empty)
cv2.createTrackbar("Val Min","Trackbar",171,255,empty)
cv2.createTrackbar("Val Max","Trackbar",250,255,empty)

while True:
  img=cv2.imread("assets/car.jpg")
  img1=cv2.resize(img,(0,0),fx=0.125,fy=0.125)
  imgsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
  imgHsv=cv2.resize(imgsv,(0,0),fx=0.125,fy=0.125)
  h_min=cv2.getTrackbarPos("Hue Min","Trackbar")
  h_max=cv2.getTrackbarPos("Hue Max","Trackbar")
  s_min=cv2.getTrackbarPos("Sat Min","Trackbar")
  s_max=cv2.getTrackbarPos("Sat Max","Trackbar")
  v_min=cv2.getTrackbarPos("Val Min","Trackbar")
  v_max=cv2.getTrackbarPos("Val Max","Trackbar")
  print(h_min,h_max,s_min,s_max,v_min,v_max)
  lower=np.array([h_min,s_min,v_min])
  upper=np.array([h_max,s_max,v_max])
  mask=cv2.inRange(imgHsv,lower,upper)
  imgres=cv2.bitwise_and(img1,img1,mask=mask)
  

 # cv2.imshow("output",img1)
  cv2.imshow("outputHsv",imgres)
  cv2.imshow("mask",mask)
  cv2.waitKey(1)


cv2.destroyAllWindows()