import cv2
import numpy as np

img=cv2.imread("assets/ok.jpg")

imgout=np.hstack((img,img))

cv2.imshow("img",imgout)
cv2.waitKey(0)
cv2.destroyAllWindows()