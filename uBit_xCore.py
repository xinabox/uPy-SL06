from microbit import*

class xCore():
    def __init__(self, i2c_addr):
        self.addr = i2c_addr
        i2c.init()

    def write_bytes(self, reg, val):
        i2c.write(self.addr, bytearray([reg, val]))

    def write_read(self, data, n):
        i2c.write(self.addr, bytearray([data]))

        return i2c.read(self.addr,n)
