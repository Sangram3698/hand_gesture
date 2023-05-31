import cv2

img=cv2.imread("assets/IMG_0102.jpg")
img1=cv2.resize(img,(0,0),fx=0.125,fy=0.125)
blur=cv2.GaussianBlur(img1,(7,7),0)
canny=cv2.Canny(img1,100,100)

cv2.imshow("blur",blur)
cv2.imshow("canny",canny)
cv2.imshow("img",img1)
cv2.waitKey(0)
cv2.destroyAllWindows()