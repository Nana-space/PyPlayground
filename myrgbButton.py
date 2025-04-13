import gpiozero as Gpio
from time import sleep
dt=.1

rPin = 37
gPin = 35
bPin = 33

rBut= 11
gBut= 13
bBut= 15

rButState = 1
rButStateOld = 1

gButState = 1
gButStateOld = 1

bButState = 1
bButStateOld = 1

rLedState = 0
gLedState = 0
bLedState = 0

#Gpio.setmode(GPIO.BOARD)

#Gpio.setup(rPin,GPIO.OUT)
#Gpio.setup(gPin,GPIO.OUT)
#Gpio.setup(bPin,GPIO.OUT)

#Gpio.setup(rBut,GPIO.IN,pull_up_down = GPIO.PUD_UP)
#Gpio.setup(gBut,GPIO.IN,pull_up_down = GPIO.PUD_UP)
#Gpio.setup(bBut,GPIO.IN,pull_up_down = GPIO.PUD_UP)
           
try:
           while True:
               rButState= rBut
               gButState= gBut
               bButState= bBut
               print('Button States',rButState, gButState, bButState)
           
except KeyboardInterrupt:
          # Gpio.cleanup()
           print ('GPIO good to go ')