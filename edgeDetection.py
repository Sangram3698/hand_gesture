import cv2
import numpy as np

img=cv2.imread("assets/shapes.png")
cv2.imshow("original",img)
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


#laplacian edge detection
lap1=cv2.Laplacian(gray,cv2.CV_64F)
lap=np.uint8(np.absolute(lap1))
cv2.imshow("lap",lap)

#sobel gradient magnitude representation
sobelX=cv2.Sobel(gray,cv2.CV_64F,1,0)
sobelY=cv2.Sobel(gray,cv2.CV_64F,0,1) 
combined=cv2.bitwise_not(sobelX,sobelY)
cv2.imshow("sobelX",sobelX)
cv2.imshow("sobelY",sobelY)
cv2.imshow("combined",combined)

cv2.waitKey(0)
cv2.destroyAllWindows()