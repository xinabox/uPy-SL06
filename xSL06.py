class xSL06():
    def __init__(this,core):

        this.self = core
        id = this.self.write_read(0x92, 1)[0]
        print(id)
        #ALL, OFF
        this.setMode(7, 0)
        #APDS9960_ATIME, DEFAULT_ATIME
        this.self.write_bytes(0x81, 219)
        #APDS9960_WTIME, DEFAULT_WTIME
        this.self.write_bytes(0x83, 246)
        #APDS9960_CONFIG1, DEFAULT_CONFIG1
        this.self.write_bytes(0x8D, 0x60)
        #DEFAULT_AILT
        this.setLightIntLowThreshold(0xFFFF)
        #DEFAULT_AIHT
        this.setLightIntHighThreshold(0)
        #APDS9960_PERS, DEFAULT_PERS
        this.self.write_bytes(0x8C, 0x11)
        #APDS9960_CONFIG2, DEFAULT_CONFIG2
        this.self.write_bytes(0x90, 0x01)
        #APDS9960_CONFIG3, DEFAULT_CONFIG3
        this.self.write_bytes(0x9F, 0)

    def getMode(this):

        enable_value = 0

        #APDS9960_ENABLE
        enable_value = this.self.write_read(0x80, 1)[0]
        return enable_value

    def setMode(this, mode, enable):

        reg_val = this.getMode()
        if (reg_val == 0xFF):
            print("Error!")
            while(True):
                pass

        enable = enable & 0x01

        if mode >= 0 and mode <= 6:
            if enable == 1:
                reg_val = reg_val | (1 << mode)
            else:
                reg_val = reg_val & ~(1 << mode)

        elif mode == 7:
            if enable == 1:
                reg_val = 0x7F
            else:
                reg_val = 0x00

        #APDS9960_ENABLE and reg_val
        this.self.write_bytes(0x80, reg_val)

        return True

    def setLEDDrive(this, drive):
        val = 0
        val = this.self.write_read(0x8F, 1)[0]

        drive = drive & 0b00000011
        drive = drive << 6
        val = val & 0b00111111
        val = val | drive

        this.self.write_bytes(0x8F, val)

        return True

    def setAmbientLightGain(this, drive):
        val = 0
        #APDS9960_CONTROL
        val = this.self.write_read(0x8f, 1)[0]

        drive = drive & 0b00000011
        val = val & 0b11111100
        val = val | drive

        #APDS9960_CONTROL
        this.self.write_bytes(0x8f, val)

        return True

    def setLightIntLowThreshold(this, threshold):

        val_low = 0
        val_high = 0
        val_low = threshold & 0x00FF
        val_high = (threshold & 0xFF00) >> 8

        #APDS9960_AILTL, val_low
        this.self.write_bytes(0x84, val_low)
        #APDS9960_AILTH, val_high
        this.self.write_bytes(0x85, val_high)

        return True

    def setLightIntHighThreshold(this, threshold):
        val_low = 0
        val_high = 0
        val_low = threshold & 0x00FF
        val_high = (threshold & 0xFF00) >> 8

        #APDS9960_AIHTL, val_low
        this.self.write_bytes(0x86, val_low)
        #APDS9960_AIHTH, val_high
        this.self.write_bytes(0x87, val_high)

        return True

    def setAmbientLightIntEnable(this, enable):
        val = 0
        #APDS9960_ENABLE
        val = this.self.write_read(0x80, 1)[0]


        enable = enable & 0b00000001
        enable = enable << 4
        val = val & 0b11101111
        val = val | enable

        #APDS9960_ENABLE
        this.self.write_bytes(0x80, val)

        return True

    def enableLightSensor(this, interrupts = False):

        this.setAmbientLightGain(1)

        if interrupts == True:
            this.setAmbientLightIntEnable(1)
        else:
            this.setAmbientLightIntEnable(0)

        this.setMode(0, 1)
        #AMBIENT_LIGHT
        this.setMode(1, 1)

    def getAmbientLight(this):

        #APDS9960_CDATAL
        val_l = this.self.write_read(0x94, 1)[0]
        #APDS9960_CDATAH
        val_h = this.self.write_read(0x95, 1)[0]

        return val_l + (val_h << 8)

    def getRedLight(this):

        #APDS9960_RDATAL
        val_l = this.self.write_read(0x96, 1)[0]
        #APDS9960_RDATAH
        val_h = this.self.write_read(0x97, 1)[0]

        return val_l + (val_h << 8)

    def getGreenLight(this):

        #APDS9960_GDATAL
        val_l = this.self.write_read(0x98, 1)[0]
        #APDS9960_GDATAH
        val_h = this.self.write_read(0x99, 1)[0]

        return val_l + (val_h << 8)

    def getBlueLight(this):

        #APDS9960_BDATAL
        val_l = this.self.write_read(0x9A, 1)[0]
        #APDS9960_BDATAH
        val_h = this.self.write_read(0x9B, 1)[0]

        return val_l + (val_h << 8)
