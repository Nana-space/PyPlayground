from gpiozero import LED
from time import sleep

led_pins=[18,23,24,25,8,7,12,16,20,21]

leds =[LED(pin) for pin in led_pins]

def odd_led_bar_graph():
    for i in range(5):
        j = i * 2
        leds[j].on()
        sleep(0.3)
        leds[j].off()
            
def even_led_bar_graph():
    for i in range(5):
        j = i*2 + 1
        leds[j].on()
        sleep(0.3)
        leds[j].off()
        
def all_led_bar_graph():
    for led in leds:
        led.on()
        sleep(0.3)
        led.off()
    
def turn_off_all_leds():
    for led in leds:
        led.off()
        
try:
    while True:
        odd_led_bar_graph()
        sleep(0.3)
        even_led_bar_graph()
        sleep(0.3)
        all_led_bar_graph()
        sleep(0.3)
        
except KeyboardInterrupt:
    turn_off_all_leds()
    pass