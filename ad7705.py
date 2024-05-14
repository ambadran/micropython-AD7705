from machine import Pin, SPI, const
from micropython import const

REG_CMM = const(0x0) #communication register 8 bit
REG_SETUP = const(0x1) #setup register 8 bit
REG_CLOCK = const(0x2) #clock register 8 bit
REG_DATA = const(0x3) #data register 16 bit, contains conversion result
REG_TEST = const(0x4) #test register 8 bit, POR 0x0
REG_NOP = const(0x5) #no operation
REG_OFFSET = const(0x6) #offset register 24 bit
REG_GAIN = const(0x7) # gain register 24 bit

#channel selection for AD7706 (for AD7705 use the first two channel definitions)
#CH1 CH0
CHN_AIN1 = const(0x0) #AIN1; calibration register pair 0
CHN_AIN2 = const(0x1) #AIN2; calibration register pair 1
CHN_COMM = const(0x2) #common; calibration register pair 0
CHN_AIN3 = const(0x3) #AIN3; calibration register pair 2

#output update rate
#CLK FS1 FS0
UPDATE_RATE_20 = const(0x0) # 20 Hz
UPDATE_RATE_25 = const(0x1) # 25 Hz
UPDATE_RATE_100 = const(0x2) # 100 Hz
UPDATE_RATE_200 = const(0x3) # 200 Hz
UPDATE_RATE_50 = const(0x4) # 50 Hz
UPDATE_RATE_60 = const(0x5) # 60 Hz
UPDATE_RATE_250 = const(0x6) # 250 Hz
UPDATE_RATE_500 = const(0x7) # 500 Hz

#operating mode options
#MD1 MD0
MODE_NORMAL = const(0x0) #normal mode
MODE_SELF_CAL = const(0x1) #self-calibration
MODE_ZERO_SCALE_CAL = const(0x2) #zero-scale system calibration, POR 0x1F4000, set FSYNC high before calibration, FSYNC low after calibration
MODE_FULL_SCALE_CAL = const(0x3) #full-scale system calibration, POR 0x5761AB, set FSYNC high before calibration, FSYNC low after calibration

#gain setting
GAIN_1 = const(0x0)
GAIN_2 = const(0x1)
GAIN_4 = const(0x2)
GAIN_8 = const(0x3)
GAIN_16 = const(0x4)
GAIN_32 = const(0x5)
GAIN_64 = const(0x6)
GAIN_128 = const(0x7)

UNIPOLAR = const(0x0)
BIPOLAR = const(0x1)

CLK_DIV_1 = const(0x1)
CLK_DIV_2 = const(0x2)

MODE = const(0b11) #SPI_CPHA | SPI_CPOL
BITS = const(8)
SPEED = const(50000)
DELAY = const(10)

class AD770X():
    def __init__(self,bus=0,device=0) :        
        self.spi = SPI(0, baudrate=SPEED, polarity=0, phase=0, bits=BITS, sck=Pin(6), mosi=Pin(7), miso=Pin(4))
        self.CS = Pin(32, Pin.OUT)


    def 

        


