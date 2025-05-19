from microbit import *
import radio

i2c.init(freq=100000, sda=pin20, scl=pin19)
radio.on()
radio.config(address=1969383799)

MOTOR_ADDRESS = 0x10
MOTOR_LEFT = 0x00
MOTOR_RIGHT = 0x02
DIR_CW = 0  # Forward
DIR_CCW = 1  # Backward

pin15.set_pull(pin15.PULL_UP) #red
pin16.set_pull(pin16.PULL_UP) #blue
pin13.set_pull(pin13.PULL_UP) #green
pin14.set_pull(pin14.PULL_UP) #yellow


def encode(password):
    enc = str(password)
    return enc.strip()

#The rest of the code goes into the while loop
while True:
    message = ""
    display.clear()
    joystick_x = pin1.read_analog() - 512

   #turn
    turn_speed = (joystick_x * 255) // 512

    if pin_logo.is_touched():
        message += ",auto"

    #yellow
    if pin14.read_digital() == 0: 
        message += ",go"

    #red btn
    if pin15.read_digital() == 0:
        message += ",stop"

    #blue btn
    if pin16.read_digital() == 0:
        message += ",womp"

    #green btn
    if pin13.read_digital() == 0:
        message += ",reverse"

    #turn
    if turn_speed >30 or turn_speed < -30:
        print(turn_speed)
        message += "," + str(turn_speed)

    if button_a.is_pressed():
        message += ",left"

    if button_b.is_pressed():
        message += ",right"

    radio.send(message)
    # display.show(encode(message))