from microbit import *
import radio

i2c.init(freq=100000, sda=pin20, scl=pin19)
radio.on()
radio.config(channel=1)

CAR_ID = "team3"
has_lightning = False
has_boost = False

MOTOR_ADDRESS = 0x10
MOTOR_LEFT = 0x00
MOTOR_RIGHT = 0x02
DIR_CW = 0  # Forward
DIR_CCW = 1  # Backward

pin15.set_pull(pin15.PULL_UP) #red
pin16.set_pull(pin16.PULL_UP) #blue
pin13.set_pull(pin13.PULL_UP) #green
pin14.set_pull(pin14.PULL_UP) #yellow

#The rest of the code goes into the while loop
while True:
    
    message = ""
    
    #yellow
    if pin14.read_digital() == 0: 
        message += ",go"

    #red btn
    if pin15.read_digital() == 0:
        message += ",stop"

    #blue btn
    # if pin16.read_digital() == 0:
    #     message += ",womp"

    #green btn
    if pin13.read_digital() == 0:
        message += ",reverse"

    if button_a.is_pressed():
        message += ",left"

    if button_b.is_pressed():
        message += ",right"

    incoming = radio.receive()

    if incoming:
        if incoming.startswith("LIGHTING:") and incoming.split(":")[1] == CAR_ID:
            has_lightning = True
            # display.show("X")
            # sleep(200)
            # print(has_lightning)
        if incoming.startswith("BOOST:") and incoming.split(":")[1] == CAR_ID:
            has_boost = True
    
    if has_lightning and pin16.read_digital() == 0:
        radio.send("STUN:team3")
        has_lightning = False
        # display.show("O")
        # sleep(200)
        # print(has_lightning)

    if has_boost and accelerometer.is_gesture('shake'):
        radio.send("FAST:team3")
        has_boost = False
        # display.show("U")
        # sleep(200)
        # print(has_boost)

    # if accelerometer.is_gesture('shake'):
    #     display.show("!")
    #     sleep(200)
    #     display.clear()

    if has_boost:
        display.show("B")
        sleep(200)
        display.clear()

    # if not pin16.read_digital() == 0 and not accelerometer.current_gesture('shake'):
    #     display.clear()

    radio.send(message)
    # display.show(encode(message))