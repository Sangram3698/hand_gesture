import cv2
import numpy as np
import matplotlib.pyplot as plt

img=cv2.imread("assets/football2.jpg")
img2=cv2.resize(img,(0,0),fx=0.25,fy=0.25)
blank=np.zeros(img2.shape[:2],dtype='uint8')
gray=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
gray_hist=cv2.calcHist([gray],[0],None,[256],[0,256])
mask=cv2.circle(blank,(img2.shape[1]//2,img2.shape[0]//2),100,255,-1)
masked=cv2.bitwise_and(img2,img2,mask=mask)


plt.figure()
plt.title('GrayStyle histogram')
plt.xlabel("Bins")
plt.ylabel('# of pixels')
plt.plot(gray_hist)
plt.xlim([0,256])
plt.show()


cv2.imshow("car",mask)
cv2.imshow("gray",masked)
cv2.waitKey(0)
cv2.destroyAllWindows()
