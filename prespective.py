import cv2
import numpy as np

img=cv2.imread("assets/ok.jpg")

width,height=250,350

pts1=np.float32([[102,265],[167,187],[202,254],[138,327]])
pts2=np.float32([[0,0],[width,0],[0,height],[width,height]])

matrix=cv2.getPerspectiveTransform(pts1,pts2)

output=cv2.warpPerspective(img,matrix,(width,height))

cv2.imshow("image",img)
cv2.imshow("output",output)
cv2.waitKey(0)
cv2.destroyAllWindows()