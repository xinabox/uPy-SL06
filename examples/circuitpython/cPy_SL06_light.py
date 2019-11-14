from cPy_core import*

from xSL06_light import*

from time import sleep



core = xCore(0x39)  #SL06 I2C adddress
SL06 = xSL06(core)  #Sending I2C object to SL06 lib

SL06.enableLightSensor()

while True:
    
    light = SL06.getAmbientLight()
    red = SL06.getRedLight()
    green = SL06.getGreenLight()
    blue = SL06.getBlueLight()
    print("Red")
    print(red)
    print("Blue")
    print(blue)
    print("Green")
    print(green)
    print("Light")
    print(light)
    
    sleep(1)

