import cv2
import numpy as np

img=cv2.imread("assets/ok.jpg")
cv2.imshow("normal",img)
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("gray",gray)

#simple thresholding
threshold,thresh=cv2.threshold(gray,150,255,cv2.THRESH_BINARY)
cv2.imshow("thresh",thresh)

threshold,thresh_inv=cv2.threshold(gray,150,255,cv2.THRESH_BINARY_INV)
cv2.imshow("threshinv",thresh_inv)

#adaptive threshold
adaptive_threshold=cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,3)
cv2.imshow("adaptive",adaptive_threshold)


cv2.waitKey(0)
cv2.destroyAllWindows()