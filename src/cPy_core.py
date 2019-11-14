import board
import busio

i2c = busio.I2C(board.SCL, board.SDA)

while not i2c.try_lock():
    pass

class xCore():
    def __init__(self, i2c_addr):
        self.addr = i2c_addr

    def write_bytes(self, reg, val):
        i2c.writeto(self.addr, bytearray([reg, val]))

    def write_read(self, data, n):
        buff = bytearray()
        temp_buff = bytearray([0])
        
        i2c.writeto(self.addr, bytearray([data]))

        for i in range(n):
            i2c.readfrom_into(self.addr, temp_buff)
            buff += temp_buff

        return buff
