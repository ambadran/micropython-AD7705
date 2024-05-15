import machine
import time
spi = machine.SPI(0,
                  baudrate=1000000,
                  polarity=1,
                  phase=1,
                  bits=8,
                  firstbit=machine.SPI.MSB,
                  sck=machine.Pin(18),
                  mosi=machine.Pin(19),
                  miso=machine.Pin(16))

reset= machine.Pin(20, machine.Pin.OUT)
reset.value(0)        #RESET
dr = machine.Pin(13, machine.Pin.IN)
cs = machine.Pin(17, machine.Pin.OUT)
cs.value(1)

reset.value(1)       #end reset
cs.value(0)
spi.write(b'\x20')   #WRITE TO COMMUNICATIONS REGISTER
cs.value(1)
cs.value(0)
spi.write(b'\x0c')   #WRITE TO CLOCK REGISTER
cs.value(1)
cs.value(0)
spi.write(b'\x10')   #WRITE TO COMMUNICATIONS REGISTER
cs.value(1)
cs.value(0)
spi.write(b'\x40')   #WRITE TO SETUP REGISTER
cs.value(1)


while True:

    if (dr.value() == 0):
        cs.value(0)
        spi.write(b'\x38')   #NEXT OPERATION READ FROM THE DATAREGISTER
        cs.value(1)
            
        cs.value(0)
        data = spi.read(2)   #READ FROM COMMUNICATIONS REGISTER
        cs.value(1)
        print(data) 
