from cPy_core import*

from xSL06_gesture import*

from time import sleep

core = xCore(0x39)  #SL06 I2C adddress
SL06 = xSL06(core)  #Sending I2C object to SL06 lib

SL06.enableGestureSensor()

while True:
    
    if SL06.isGestureAvailable():   # check for gesture
        print("gesture")
        dir = SL06.getGesture()  # read direction
        print(dir)                  # print direction on console
        
        
    sleep(0.1)
