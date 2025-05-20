from maqueen import *
from mbrobot_plusV2 import *
import radio
from microbit import i2c, pin15, pin20, pin19

i2c.init(freq=100000, sda=pin20, scl=pin19)

robot = Maqueen()
radio.on()
# radio.config(address=1969383799)
radio.config(channel=1)

CAR_ID = "team3"
MOTOR_ADDRESS = 0x10
MOTOR_LEFT = 0x00
MOTOR_RIGHT = 0x02
DIR_CW_FORWARD = 0
DIR_CCW_BACKWARD = 1
RGB_LED_COUNT = 4
np = neopixel.NeoPixel(pin15, RGB_LED_COUNT)

stunned = False
stun_start_time = 0
has_lightning = False
boost_active = False
boost_start_time = 0
BOOST_DURATION = 3000



while True:

    instruct = radio.receive()


    if instruct:
        instruct = instruct.replace(',', '')
        
        if instruct == 'reverse':
            setSpeed(200)
            backward()
        if instruct == 'go':
            setSpeed(200)
            forward()
        if instruct == 'stop':
            stop()
        if instruct == 'left':
            setSpeed(175)
            left()
        if instruct == 'right':
            setSpeed(175)
            right()
        if instruct == 'womp':
            print('womp')

        if instruct.startswith("FAST:") and instruct.split(":")[1] == CAR_ID:
                    boost_active = True
                    boost_start_time = running_time()
                    display.show("B")
        elif instruct.startswith("STUN:") and instruct.split(":")[1] != CAR_ID and not stunned:
                    stunned = True
                    stun_start_time = running_time()
                    stop()
                    display.show("X")
            
    if stunned:
        if running_time() - stun_start_time< 5000:
            stop()
            for i in range(RGB_LED_COUNT): 
                np[i] = (255, 0, 0)
            np.show()
        else:
            stunned = False
            display.clear()
            for i in range(RGB_LED_COUNT):
                np[i] = (0, 0, 0)
            np.show()

    if boost_active:
        if running_time() - boost_start_time < BOOST_DURATION:
            setSpeed(255)
            forward()
            for i in range(RGB_LED_COUNT):  # Flash groen tijdens boost
                np[i] = (0, 255, 0)
            np.show()
        else:
            boost_active = False
            stop()
            for i in range(RGB_LED_COUNT):
                np[i] = (0, 0, 0)
            np.show()
    sleep(100)