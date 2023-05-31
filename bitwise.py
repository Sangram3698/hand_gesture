import cv2
import numpy as np

blank=np.ones_likeg((400,400),dtype='uint8')

rectangle=cv2.rectangle(blank.copy(),(30,30),(280,280),255,-1)
circle=cv2.circle(blank.copy(),(250, 250),100,255,-1)
imgBitwiseAnd=cv2.bitwise_and(rectangle,circle)
imgBitWiseOr=cv2.bitwise_or(rectangle,circle)
imgBitwiseXor=cv2.bitwise_xor(rectangle,circle)
cv2.imshow("rectangle",rectangle)
cv2.imshow("circle",circle)
cv2.imshow("bitwise",imgBitwiseAnd)
cv2.imshow("Bitwise Or",imgBitWiseOr)
cv2.imshow("NitwiseXor",imgBitwiseXor)
cv2.waitKey(0)
cv2.destroyAllWindows()