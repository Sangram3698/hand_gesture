import pyfirmata
import time

pin1=[9,10,11,12,13]
port="COM3"

board=pyfirmata.Arduino(port)

for i in pin1:
  board.digital[i].mode=pyfirmata.SERVO

board.digital[9].write(0)
def rotateServo(pin,angle):
  board.digital[pin].write(angle)
  # time.sleep(0.015)
  




  
  

# while True:
#   print('1 for 90 derees')
#   print('2 for 180 derees')
#   print('3 for 270 derees')
#   x=input('Enter the digits for rotation:')
#   if x=='1':
#    for i in range(0,90):
#      rotateServo(9,i)
    
#   if x=='2':
#    for i in range(0,180):
#      rotateServo(9,i)
    
#   if x=='3':
#    for i in range(0,270):
#      rotateServo(9,i)

while True:
  x=input('enter:')
  if x=="1":
    
    board.digital[9].write(90)
    time.sleep(0.01)
  if x=='2':
    board.digital[9].write(0)  
  
    



  


