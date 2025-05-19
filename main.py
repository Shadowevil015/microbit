from main import *
from maqueen import *
import random
from mbrobot_plusV2 import *
import radio
import speech
import music

robot = Maqueen()
radio.on()
radio.config(address=1969383799)

# Your code follows here.

while True:
    # r = random.randint(1, 255)
    # g = random.randint(1, 255)
    # b = random.randint(1, 255)
    
    # if accelerometer.was_gesture('shake'):
    #     speech.say('womp womp', speed=97, throat=255, pitch=85)
    # sleep(1000)

    # for freq in range(2000, 800, -100):
    #     music.pitch(freq, 30)

    # setRGB(r, g, b)
    # sleep(1000)

    # if getDistance() > 20:
    #     backward()
    # else:
    #     forward()

    setRGB(170,68,101)

    instruct = radio.receive()

    if instruct:
        instruct = instruct.replace(',', '')
        
        if instruct == 'reverse':
            setSpeed(255)
            backward()
        if instruct == 'go':
            setSpeed(255)
            forward()
        if instruct == 'stop':
            stop()
        if instruct == 'left':
            setSpeed(150)
            left()
        if instruct == 'right':
            setSpeed(150)
            right()
        if instruct == 'womp':
        #     speech.say('womp womp', speed=97, throat=255, pitch=85)#
            setSpeed(50)
            forward()
        # if getDistance() > 20:
        #     speech.say('womp womp', speed=97, throat=255, pitch=85)
            
        # try:
        #     int(instruct)
        #     if int(instruct) < -31:
        #         stop()
        #         robot.motor_right(200,0)
        #         utime.sleep_ms(200)
        #         robot.motor_right(0,0)
        #     elif int(instruct) > 31:
        #         stop()
        #         robot.motor_left(200,0)
        #         utime.sleep_ms(200)
        #         robot.motor_left(0,0)
        # except ValueError:
        #     pass
        # if instruct.isDigit() or instruct.includes('-'):
        #     if instruct < -31:
        #         leftArc(50)
        #     elif instruct > 31:
        #         rightArc(50)

    # if instruct:
    #     if instruct == 'f':
    #         forward()
    #     if instruct == 'b':
    #         backward()
    #     if instruct == 'stop':
    #         speech.say('womp womp', speed=97, throat=255, pitch=85)

    #         # speed = 50
    #     if instruct == 'l':
    #         left()
    #         # utime.sleep_ms(1000)
    #         # instruct = 'f'
    #     if instruct == 'r':
    #         right()
    #         # utime.sleep_ms(1000)
    #         # instruct = 'f'
    #     # if instruct == 's50':
    #     #     setSpeed(50)
    #     # if instruct == 's200':
    #     #     setSpeed(200)
    #     # if instruct == 'i':
    #     #     speed = speed + 1
    #     #     setSpeed(speed)
    #     #     display.show(speed)
    #     # if instruct == 'd':
    #     #     speed = speed - 1
    #     #     setSpeed(speed)

        
     