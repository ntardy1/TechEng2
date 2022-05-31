
from ast import And
from sense_hat import SenseHat
from time import sleep
import os

os.system('clear')

sense = SenseHat()

# Setting colors
R = [255,0,0]
G = [0,255,0]
B = [0,0,255]
b = [0,0,0]

indices = []
snake = []
blank = []
headPosition = 27
previousVelocity = 'none'
velocity = 'right'

for elem in range(64):
    if (elem == 25 or elem == 26):
        snake.append(B)
    elif (elem == 27):
        snake.append(R)
    else:
        snake.append(b)
for elem in range(64):
    blank.append(b)
sense.set_pixels(snake)

# sense.set_pixels() sets the pixels on the LED matrix
# sense.get_pixels() gets the current image on the LED matrix

while True:
    sleep(0.4)
    for event in sense.stick.get_events():
        if (event.action == 'pressed'):
            if (event.direction == 'up'):
                previousVelocity = velocity
                velocity = 'up'
            elif (event.direction == 'down'):
                previousVelocity = velocity
                velocity = 'down'
            elif (event.direction == 'right'):
                previousVelocity = velocity
                velocity = 'right'
            elif (event.direction == 'left'):
                previousVelocity = velocity
                velocity = 'left'
    if (velocity == 'up' and previousVelocity == 'right'):
        for index in range(len(snake)):
            if (index < 56):
                if (snake[index] == R and snake[index + 8] != B):
                    headPosition = index
                    break
            elif (index > 56):
                if (snake[index] == R and snake[index - 63 + 8] != B):
                    headPosition = index
                    break
        for index in range(len(snake)):
            # current problem is that the end of the snake will turn black, but then this affects the next link of the
            # snake because of how for loops works
            if (index <= 7):
                if (snake[index] == R):
                    print(index, 'COndition 0')
                    snake[63 - (7 - index)] = R
                    snake[index] = B
                elif (snake[index] == B and index == headPosition and snake[index - 1] == b):
                    print(index, "Condition 1")
                    snake[63 - (7 - index)] = B
                    snake[index] = b
                elif (snake[index + 8] == b and snake[index] == B and snake[index - 1] == b):
                    print(index, "Condition 2")
                    snake[index] = b
            elif (index > 7 and index < 56):
                if (snake[index] == R):
                    print(index, 'COndition 0')
                    snake[index - 8] = R
                    snake[index] = B
                elif (snake[index] == B and index == headPosition and snake[index - 1] == b):
                    print(index, "Condition 1")
                    snake[index - 8] = B
                    snake[index] = b
                elif (snake[index + 8] == b and snake[index] == B and snake[index - 1] == b):
                    print(index, "Condition 2")
                    snake[index] = b
            elif (index >= 56):
                if (snake[index] == R):
                    snake[index - 8] = R
                    snake[index] = B
                elif (snake[index - 63 + 8] == b and snake[index] == B):
                    snake[index] = b
    elif (velocity == 'up' and previousVelocity == 'down'):
        velocity = 'up'
    elif (velocity == 'right'):
        for index in range(len(snake)):
            if (snake[index] == R):
                snake[index + 1] = R
                snake[index] = B
                break
        for index in range(len(snake)):
            if (snake[index] == B and snake[index - 1] == b):
                snake[index] = b
                break
    print('update')
    sense.set_pixels(snake)
