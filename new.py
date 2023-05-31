import numpy as np
import cv2

img=cv2.imread("assets/chess.jpg",1)
img0=cv2.resize(img,(0,0),fx=0.5,fy=0.5)
img2=cv2.cvtColor(img0,cv2.COLOR_BGR2GRAY)
corners=cv2.goodFeaturesToTrack(img2,100,0.2,100)
corners=np.int0(corners)
for corner in corners:
  x,y=corner.ravel()
  cv2.circle(img0,(x,y),5,(0,255,0),-1)

cv2.imshow("image",img0)
cv2.waitKey(0)
cv2.destroyAllWindows()