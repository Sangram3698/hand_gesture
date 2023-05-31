import cv2
import mediapipe as mp

mp_drawing=mp.solutions.drawing_utils
mp_drawing_style=mp.solutions.drawing_styles
mphands=mp.solutions.hands

hands=mphands.Hands()

cap=cv2.VideoCapture(0)
while True:
  ret,frame=cap.read()
  img=cv2.flip(frame,1)
  image=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
  result=hands.process(image)
  image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
  if result.multi_hand_landmarks:
    for hand_landmarks in result.multi_hand_landmarks:
      mp_drawing.draw_landmarks(
        image,
        hand_landmarks,mphands.HAND_CONNECTIONS)
  cv2.imshow("image",img)
  if cv2.waitKey(10)==ord('q'):
    break
cap.release()
cv2.destroyAllWindows()
      