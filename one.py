import pyfirmata
import time

pin=13
port="COM3"
board=pyfirmata.Arduino(port)

repeat=input("how many times do you want to blink the led:")

for x in range (int(repeat)):
  board.digital[pin].write(1)
  time.sleep(0.3)
  print("on")
  board.digital[pin].write(0)
  time.sleep(3)
  print("off")

