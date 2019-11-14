from uBit_core import*

from xSL06_proximity import*



core = xCore(0x39)  #SL06 I2C adddress
SL06 = xSL06(core)  #Sending I2C object to SL06 lib

SL06.enableProximitySensor()

while True:
    
    prox = SL06.getProximity()
    print("Proximity")
    print(prox)
    
    sleep(500)

