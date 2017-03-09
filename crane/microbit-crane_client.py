# Add your Python code here. E.g.
from microbit import *
import radio

radio.on()

threshold1 = 400
threshold2 = 800

while True:
    acc_x = accelerometer.get_x()
    acc_y = accelerometer.get_y()
    
    display.clear()
    
    if acc_x > threshold2:
        x = 4
    elif acc_x > threshold1:
        x = 3
    elif acc_x < -threshold2:
        x = 0
    elif acc_x < -threshold1:
        x = 1
    else:
        x = 2

    if acc_y > threshold2:
        y = 4
    elif acc_y > threshold1:
        y = 3
    elif acc_y < -threshold2:
        y = 0
    elif acc_y < -threshold1:
        y = 1
    else:
        y = 2
        
    display.set_pixel(x, y, 9)
    
    send_string = str(x) + str(y)
    radio.send(send_string)
    
    sleep(500)
