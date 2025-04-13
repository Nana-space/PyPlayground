import datetime
import time
import os

def alarm_clock(alarm_time):
    print(f"Wecker für {alarm_time} gestellt...")
    
    while True:
        current_time = datetime.datetime.now().strftime("%H:%M")
        
        if current_time == alarm_time:
            print("Wecker klingelt")
            break
        time.sleep(1)
        
wecker_zeit = input("Bitte stell eine Alarmzeit ein: ")
alarm_clock(wecker_zeit)
