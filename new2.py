# import numpy as np
# import cv2

# BGR_color=np.array([[[255,0,0]]],dtype=np.uint8)
# x=cv2.cvtColor(BGR_color,cv2.COLOR_BGR2HSV)
# print(x[0][0])

import cv2
img=cv2.imread("assets/cardss.jpg")
img1=cv2.resize(img,(0,0),fx=0.125,fy=0.125)
cv2.imwrite("ok.jpg",img1)

cv2.imshow("pic",img1)
cv2.waitKey(0)
cv2.destroyAllWindows()






