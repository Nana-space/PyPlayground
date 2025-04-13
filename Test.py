from gpiozero import LED
from time import sleep

led =LED(17)
try:
    while True:
        led.on()
        sleep(0.5)
        print ('LED ein ')
        
        led.off()
        print ('LED aus')
        
        sleep (0.5)

except KeyboardInterrupt:
    pass