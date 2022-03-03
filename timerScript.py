'''
(1/3) Script for the Advanced LED Light Show
Nathan Tardy - 2.9.2022
Technology and Engineering II - Bangor High School
This script contains the program that runs the timer.
'''

# Importing libraries
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Red timer pins
GPIO.setup(2,GPIO.OUT)
GPIO.setup(3,GPIO.OUT)
GPIO.setup(4,GPIO.OUT)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)

# Yellow timer pins
GPIO.setup(0,GPIO.OUT)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(9,GPIO.OUT)
GPIO.setup(10,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)

# Green timer pins
GPIO.setup(5,GPIO.OUT)
GPIO.setup(6,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(19,GPIO.OUT)
GPIO.setup(26,GPIO.OUT)

allTimerPins = [26, 19, 13, 6, 5, 22, 10, 9, 11, 0, 27, 17, 4, 3, 2]
        
# RGB LED Pins
# Far left
GPIO.setup(14,GPIO.OUT) #Blue
GPIO.setup(15,GPIO.OUT) #Green
GPIO.setup(16,GPIO.OUT) #Red
# Second from left
GPIO.setup(23,GPIO.OUT) #Red
GPIO.setup(24,GPIO.OUT) #Green
GPIO.setup(25,GPIO.OUT) #Blue
# Third from left
GPIO.setup(8,GPIO.OUT) #Red
GPIO.setup(7,GPIO.OUT) #Green
GPIO.setup(1,GPIO.OUT) #Blue
# Fourth from left
GPIO.setup(12,GPIO.OUT) #Red
GPIO.setup(16,GPIO.OUT) #Green
GPIO.setup(20,GPIO.OUT) #Blue

# Custom functions
def pinOff(pin):
    GPIO.output(pin, False)
    
def pinOn(pin, duration):
    GPIO.output(pin, True)
    sleep(duration)
    GPIO.output(pin, False)

# This is to turn on all the Red LED's
def redOn():
    GPIO.output(2,True)
    GPIO.output(3,True)
    GPIO.output(4,True)
    GPIO.output(17,True)
    GPIO.output(27,True)

# Turns on all the Yellow LED's
def yellowOn():
    GPIO.output(0,True)
    GPIO.output(11,True)
    GPIO.output(9,True)
    GPIO.output(10,True)
    GPIO.output(22,True)

# Turns on all the Green LED's
def greenOn():
    GPIO.output(5,True)
    GPIO.output(6,True)
    GPIO.output(13,True)
    GPIO.output(19,True)
    GPIO.output(26,True)

def redOff():
    GPIO.output(2,False)
    GPIO.output(3,False)
    GPIO.output(4,False)
    GPIO.output(17,False)
    GPIO.output(27,False)
    
def yellowOff():
    GPIO.output(0,False)
    GPIO.output(11,False)
    GPIO.output(9,False)
    GPIO.output(10,False)
    GPIO.output(22,False)
    
def greenOff():
    GPIO.output(5,False)
    GPIO.output(6,False)
    GPIO.output(13,False)
    GPIO.output(19,False)
    GPIO.output(26,False)
    
# Timer variable
gameDuration = 15 #seconds

redOn()
yellowOn()
greenOn()
for elem in allTimerPins:
    sleep(gameDuration/15)
    pinOff(elem)
