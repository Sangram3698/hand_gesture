import cv2
import numpy as np

img=cv2.imread("assets/shapes.png")
imgblur=cv2.GaussianBlur(img,(7,7),1)
imgbluring=cv2.blur(img,(3,3))

cv2.imshow("image",imgbluring)


cv2.waitKey(0)
cv2.destroyAllWindows()
