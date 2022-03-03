'''
(2/3) Script for the Advanced LED Light Show
Nathan Tardy - 2.9.2022
Technology and Engineering II - Bangor High School
This script contains the program that runs the RGB Lights.
'''

# Importing libraries
import RPi.GPIO as GPIO
from time import sleep
import random
import keyboard
import os

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# RGB LED Pins
# Far left
GPIO.setup(14,GPIO.OUT) #Blue
GPIO.setup(15,GPIO.OUT) #Green
GPIO.setup(16,GPIO.OUT) #Red
farLeft = [14,15,16]

# Second from left
GPIO.setup(23,GPIO.OUT) #Red
GPIO.setup(24,GPIO.OUT) #Green
GPIO.setup(25,GPIO.OUT) #Blue
secondLeft = [23,24,25]

# Third from left
GPIO.setup(8,GPIO.OUT) #Red
GPIO.setup(7,GPIO.OUT) #Green
GPIO.setup(1,GPIO.OUT) #Blue
thirdLeft = [8,7,1]

# Fourth from left
GPIO.setup(12,GPIO.OUT) #Red
GPIO.setup(16,GPIO.OUT) #Green
GPIO.setup(20,GPIO.OUT) #Blue
fourthLeft = [12,16,20]

# Custom Functions
def RGBON(pin):
    GPIO.output(pin,False)
    
def RGBOFF(pin):
    GPIO.output(pin,True)
    
# Setting up necessary variables
redPins = [16,23,8,12]
bluePins = [14,25,1,20]
greenPins = [15,24,7,16]
allPins = [[14,15,16],[23,24,25],[8,7,1],[12,16,20]]
score = 0
delay = 1

# Turning off all LED's before the "game" begins
for pin in redPins:
    RGBOFF(pin)
for pin in bluePins:
    RGBOFF(pin)
for pin in greenPins:
    RGBOFF(pin)
    
# The loop that runs the game
while True:
    led = random.randint(0,3)
    specificLED = allPins[led]
    pin = specificLED[random.randint(0,2)]
    if (any(pin == pins for pins in redPins)):
        duration = random.uniform(1.5,2)
    elif (any(pin == pins for pins in bluePins)):
        duration = random.uniform(2,2.5)
    elif (any(pin == pins for pins in greenPins)):
        duration = random.uniform(2.5,3)
    oldScore = score
    RGBON(pin)
    # A for loop that constantly checks for key presses while the LED is illuminated 
    for elem in range(round(duration * 10)):
        # The 'esc' key is used to stop the program
        if (keyboard.is_pressed('esc')):
            for pin in redPins:
                RGBOFF(pin)
            for pin in bluePins:
                RGBOFF(pin)
            for pin in greenPins:
                RGBOFF(pin)
            print("\r",end="")
            print('Exiting')
            exit()
        print("\r",end="")
        sleep(delay/(duration * 10))
        # The larger conditional checks for the color of the illuminated LED
        if (any(pin == pins for pins in redPins)):
            # The inner conditionals check for a key press that correctly
            # corresponds to the illuminated LED
            if (keyboard.is_pressed('0') and led == 0):
                score += 10
                break
            elif (keyboard.is_pressed('1') and led == 1):
                score += 10
                break
            elif (keyboard.is_pressed('2') and led == 2):
                score += 10
                break
            elif (keyboard.is_pressed('3') and led == 3):
                score += 10
                break
        elif (any(pin == pins for pins in bluePins)):
            if (keyboard.is_pressed('0') and led == 0):
                score += 5
                break
            elif (keyboard.is_pressed('1') and led == 1):
                score += 5
                break
            elif (keyboard.is_pressed('2') and led == 2):
                score += 5
                break
            elif (keyboard.is_pressed('3') and led == 3):
                score += 5
                break
        elif (any(pin == pins for pins in greenPins)):
            if (keyboard.is_pressed('0') and led == 0):
                score += 3
                break
            elif (keyboard.is_pressed('1') and led == 1):
                score += 3
                break
            elif (keyboard.is_pressed('2') and led == 2):
                score += 3
                break
            elif (keyboard.is_pressed('3') and led == 3):
                score += 3
                break
    # Turning the LED off and printing the new score if it has changed
    RGBOFF(pin)
    newScore = score
    if (newScore > oldScore):
        print(f"\rScore: {newScore}")
