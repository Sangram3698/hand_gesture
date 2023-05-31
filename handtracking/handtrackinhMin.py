import cv2
import mediapipe as mp
import time

cap=cv2.VideoCapture(0)
mpHands=mp.solutions.hands
hands=mpHands.Hands()
mpDraw=mp.solutions.drawing_utils

pTime=0
cTime=0


while True:
  ret,frame=cap.read()
  img=cv2.flip(frame,1)
  imgRgb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
  result=hands.process(imgRgb)
  #print(result.multi_hand_landmarks)
  if result.multi_hand_landmarks:
    for handLms in result.multi_hand_landmarks:
      mpDraw.draw_landmarks(img,handLms,mpHands.HAND_CONNECTIONS)
      for id,lm in enumerate(handLms.landmark):
        #print(id,lm)
        h,w,c=img.shape
        cx,cy=int(lm.x*w),int(lm.y*h)
        print(id,cx,cy)
        if id==0:
          cv2.circle(img,(cx,cy),25,(0,255,0),cv2.FILLED)
  cTime=time.time()
  fps=1/(cTime-pTime)
  pTime=cTime
  cv2.putText(img,str(int(fps)),(20,90),cv2.FONT_HERSHEY_COMPLEX,4,(255,128,150),2)        
      
  
  cv2.imshow("camera",img)
  if cv2.waitKey(1)==ord('q'):
    break
cap.release()
cv2.destroyAllWindows()