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
        #DEFAULT_LDRIVE
        this.setLEDDrive(0)
        #DEFAULT_PGAIN
        this.setProximityGain(2)
        #APDS9960_PILT, DEFAULT_PILT
        this.self.write_bytes(0x89, 0)
        #APDS9960_PIHT, DEFAULT_PIHT
        this.self.write_bytes(0x8B, 50)
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
        
    def setProximityGain(this, drive):
        val = 0
        #APDS9960_CONTROL
        val = this.self.write_read(0x8F, 1)[0]
        
        drive = drive & 0b00000011
        drive = drive << 2
        val = val & 0b11110011
        val = val | drive
        
        #APDS9960_CONTROL
        this.self.write_bytes(0x8F, val)
            
        return True
        
    def setProximityIntEnable(this, enable):
        val = 0
        #APDS9960_ENABLE
        val = this.self.write_read(0x80, 1)[0]
        enable = enable & 0b00000001
        enable = enable << 5
        val = val & 0b11011111
        val = val | enable

        #APDS9960_ENABLE
        this.self.write_bytes(0x80, val)
                
        return True
        
    def enableProximitySensor(this, interrupts = False):
        if interrupts == True:
            this.setProximityIntEnable(1)
        else:
            this.setProximityIntEnable(0)
            
        this.setMode(0, 1)
        this.setMode(2, 1)
        
    def getProximity(this):
        #APDS9960_PDATA
        return  this.self.write_read(0x9C, 1)[0]
 
