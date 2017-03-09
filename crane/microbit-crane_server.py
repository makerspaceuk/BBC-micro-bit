# Add your Python code here. E.g.
from microbit import *
import radio

speed_off = 0
speed_rotate_slow = 128
speed_rotate_fast = 256
speed_hook_slow = 128
speed_hook_fast = 256

radio.on()

x = 2
y = 2

pin0.write_analog(speed_off)
pin8.write_analog(speed_off)
pin12.write_analog(speed_off)
pin16.write_analog(speed_off)

while True:
    display.clear()
    
    recv_string = radio.receive()
    
    if recv_string != None:

        recv_int = int(recv_string)
        x = recv_int // 10
        y = recv_int % 10

    display.set_pixel(x, y, 9)

    # Rotation
    if x > 3:
        pin0.write_analog(speed_rotate_fast)
        pin16.write_analog(speed_off)
    elif x > 2:
        pin0.write_analog(speed_rotate_slow)
        pin16.write_analog(speed_off)
    elif x < 1:
        pin0.write_analog(speed_off)
        pin16.write_analog(speed_rotate_fast)
    elif x < 2:
        pin0.write_analog(speed_off)
        pin16.write_analog(speed_rotate_slow)
    else:
        pin0.write_analog(speed_off)
        pin16.write_analog(speed_off)
    # Hook
    if y > 3:
        pin8.write_analog(speed_hook_fast)
        pin12.write_analog(speed_off)
    elif y > 2:
        pin8.write_analog(speed_hook_slow)
        pin12.write_analog(speed_off)
    elif y < 1:
        pin8.write_analog(speed_off)
        pin12.write_analog(speed_hook_fast)
    elif y < 2:
        pin8.write_analog(speed_off)
        pin12.write_analog(speed_hook_slow)
    else:
        pin8.write_analog(speed_off)
        pin12.write_analog(speed_off)
    
    sleep(250)
