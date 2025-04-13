from gpiozero import RGBLED
from time import sleep

COLORS =[(1,0,0),(0,1,0),(0,0,1),(1,1,0),(0.1,0.5,1)]

rgb_led = RGBLED(red = 17,green= 18, blue = 27)

try:
    while True:
        for color in COLORS:
            rgb_led.color = color
            print (f"Farbe auf :{color}")
            sleep(4)
            
except KeyboardInterrupt:
    pass