import pyfirmata 
import time

port = 'COM3'# Windows
#port = '/dev/ttyACM3' # Linux
#port = '/dev/tty.usbmodem11401'# Mac

initAngle = 0
currentAngle = initAngle
board = pyfirmata.Arduino(port)
digital_pin_2 = board.get_pin('d:2:s')
#digital_pin_2.write(initAngle)

def left(angle):
    global currentAngle
    if(currentAngle<180):
        if angle:
            currentAngle+=angle
            if(currentAngle>180):currentAngle=180
        else:
            currentAngle+=1
        digital_pin_2.write(currentAngle)
        time.sleep(0.2)

def right(angle):
    global currentAngle
    if(currentAngle>0):
        if angle:
            currentAngle-=angle
            if(currentAngle<0):currentAngle=0
        else:
            currentAngle-=1
        digital_pin_2.write(currentAngle)
        time.sleep(0.2)

def breakArm():
    board.exit() # Closing the communication with the Arduino card
'''
digital_pin_2.write(30)
time.sleep(0.2)
digital_pin_2.write(60)
time.sleep(0.2)
digital_pin_2.write(90)
time.sleep(0.2)
digital_pin_2.write(120)
time.sleep(0.2)
digital_pin_2.write(150)
time.sleep(0.2)
'''

'''
for i in range(3): # Loop to blink the micro-led dix times
    digital_pin_2.write(30)
    time.sleep(1)
    LED_pin.write(LOW) # Turn off the led
    time.sleep(1)
'''