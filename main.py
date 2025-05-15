from maqueen import Maqueen
import radio
from microbit import *

radio.on()
radio.config(address=0x75626977)

robot = Maqueen()

robot.rgb_front_left(247, 103, 20)
robot.rgb_rear_left(247, 103, 20)
robot.rgb_rear_right(247, 103, 20)
robot.rgb_front_right(247, 103, 20)

while True:

    if robot.ultrasound_measure() > 16:
        robot.motor_left(20, 0)
        robot.motor_right(20, 0)
        display.scroll(robot.ultrasound_measure())


    elif robot.ultrasound_measure() < 16:
        robot.motor_right(0, 0)
        robot.motor_left(0, 0)
        display.scroll(robot.ultrasound_measure())
        