from microbit import *
import radio

radio.on()
radio.config(address=1969383799)

pin_logo.set_touch_mode(pin_logo.CAPACITIVE)

while True:
    if button_a.is_pressed():
        radio.send('f')
        display.show('f')
    if button_b.is_pressed():
        radio.send('b')
        display.show('b')
    if pin_logo.is_touched():
        radio.send('stop')
        display.show('s')
    # if pin0.is_touched():
    #     radio.send('i')
    #     # display.show('i')
    # if pin2.is_touched():
    #     radio.send('d')
    #     display.show('d')
    if accelerometer.is_gesture('left'):
        radio.send('l')
        display.show('l')
    if accelerometer.is_gesture('right'):
        radio.send('r')
        display.show('r')
    # if accelerometer.is_gesture('up'):
    #     radio.send('s50')
    # if accelerometer.is_gesture('face up'):
    #     radio.send('s200')
    #     display.show('u')

    # message = radio.receive()
    # if message:
    #     display.show(message) 