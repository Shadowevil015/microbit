from maqueen import *
from mbrobot_plusV2 import *
import radio
from micrbit import i2c, pin15, pin20, pin19

i2c.init(freq=100000, sda=pin20, scl=pin19)

MOTOR_ADDRESS = 0x10
LINE_SENSOR_REGISTER = 0x1D
RGB_LED_PIN = pin15  
RGB_LED_COUNT = 4 

line_detected = False
no_line_counter = 0
NO_LINE_THRESHOLD = 20 

ignore_line_detection = False
ignore_line_start_time = 0
IGNORE_LINE_DURATION = 750

np = neopixel.NeoPixel(RGB_LED_PIN, RGB_LED_COUNT)

def read_line_sensors():
    i2c.write(MOTOR_ADDRESS, bytes([LINE_SENSOR_REGISTER]))
    sensor_data = i2c.read(MOTOR_ADDRESS, 2)

    data = sensor_data[0]
    L1 = (data >> 0) & 1
    L2 = (data >> 1) & 1
    M = (data >> 2) & 1
    R1 = (data >> 3) & 1
    R2 = (data >> 4) & 1

    return {"L1": L1, "L2": L2, "M": M, "R1": R1, "R2": R2}

def line_sensor_logic(sensors):

    global line_detected, no_line_counter

    if sensors["L1"] == 1 or sensors["L2"] == 1 or sensors["M"] == 1 or sensors["R1"] == 1 or sensors["R2"] == 1:
        line_detected = True
        no_line_counter = 0
    else:
        no_line_counter += 1
        if no_line_counter >= NO_LINE_THRESHOLD:
            line_detected = False

    if line_detected and not ignore_line_detection:
        for i in range(RGB_LED_COUNT):
            np[i] = (255, 0, 0) 
        np.show()
    else:
        for i in range(RGB_LED_COUNT):
            np[i] = (0, 0, 0) 
        np.show()



robot = Maqueen()
radio.on()
radio.config(address=1969383799)

while True:

    sensors = read_line_sensors() 

    line_sensor_logic(sensors)

    if instruct == "go" or instruct == 'womp' and not ignore_line_detection:
        ignore_line_detection = True
        ignore_line_start_time = running_time()

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
            setSpeed(50)
            forward()
            
