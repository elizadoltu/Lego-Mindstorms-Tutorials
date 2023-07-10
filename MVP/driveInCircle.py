from mindstorms import MSHub, Motor, MotorPair, ColorSensor, DistanceSensor, App
from mindstorms.control import wait_for_seconds, wait_until, Timer
from mindstorms.operator import greater_than, greater_than_or_equal_to, less_than, less_than_or_equal_to, equal_to, not_equal_to
import math

# Create your objects here.
hub = MSHub()

# Write your program here.
hub.speaker.beep()

# Initiate the motors
frontWheels = Motor('A')
backWheels = Motor('B')


def initiateTheRobot():

    frontWheels.set_default_speed(30)
    backWheels.set_default_speed(90)
    hub.motion_sensor.reset_yaw_angle()
    frontWheels.run_to_position(0, 'shortest path')
    backWheels.run_to_position(0, 'shortest path')

# First Method


def runInCircle_1():

    # Maximum for front Wheels is 70 degrees
    # It depends on the speed
    frontWheels.run_to_position(70, 'shortest path')  # Will turn left
    backWheels.run_for_rotations(-12.5)
    # Even it is negative, the car will move forward
    # Negative values - the motor will run counterclockwise
    # Positive values - the motor will run clockwise
    # run_to_position = the motor will run to the desire position (for our case, at 70 degrees) in 'shortest path'
    # example : if the position of the motor is at 50 degrees and we want to go to position 0, it will turn counterclockwise; if it is at 195 degrees and we want to go to position 0, it will turn clockwise (360 degrees - our current position)

# Second Method


def runInCircle_2():

    # We saw in the previous method that we need 12.5 rotations of the motor to complete a circle
    frontWheels.run_to_position(70, 'shortest path')
    # We take 13 rotatios because we need an integer as first parameter, which is the degrees
    # 360 = 1 full rotation
    fullCircle = 13 * -360
    backWheels.run_to_degrees_counted(fullCircle)


initiateTheRobot()
runInCircle_2()
