
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
            if (event.direction == 'up' and previousVelocity == 'down'):
                None
            elif (event.direction == 'up'):
                previousVelocity = velocity
                velocity = 'up'
            elif (event.direction == 'down' and previousVelocity == 'up'):
                None
            elif (event.direction == 'down'):
                previousVelocity = velocity
                velocity = 'down'
            elif (event.direction == 'right' and previousVelocity == 'left'):
                None
            elif (event.direction == 'right'):
                previousVelocity = velocity
                velocity = 'right'
            elif (event.direction == 'left' and previousVelocity == 'right'):
                None
            elif (event.direction == 'left'):
                print('here')
                previousVelocity = velocity
                velocity = 'left'
    if (velocity == 'up' and previousVelocity == 'right'):
        for index in range(len(snake)):
            if (index < 56):
                if (snake[index] == R and snake[index + 8] != B):
                    headPosition = index
                    break
            elif (index > 56):
                if (snake[index] == R and snake[index - 63 + 7] != B):
                    headPosition = index
                    break
        for index in range(len(snake)):
            if (index < 56):
                if (snake[index] == B and snake[index - 1] == b and snake[index - 8] == b and snake[index + 8] == b):
                    tempIndex = snake.index(R)
                    snake[tempIndex - 8] = R
                    snake[tempIndex] = B
                    snake[index] = b
                    break
                elif (snake[index] == B and snake[index - 1] == b and snake[index + 1] == b and snake[index + 8] == b):
                    tempIndex = snake.index(R)
                    snake[tempIndex - 8] = R
                    snake[tempIndex] = B
                    snake[index] = b
                    break
            elif (index >= 56):
                if (snake[index] == B and snake[index - 1] == b and snake[index - 8] == b and snake[index - 63 + 7] == b):
                    tempIndex = snake.index(R)
                    snake[tempIndex - 8] = R
                    snake[tempIndex] = B
                    snake[index] = b
                    break
                elif (snake[index] == B and snake[index - 1] == b and snake[index + 1] == b and snake[index - 63 + 7] == b):
                    tempIndex = snake.index(R)
                    snake[tempIndex - 8] = R
                    snake[tempIndex] = B
                    snake[index] = b
                    break
    elif (velocity == 'left' and previousVelocity == 'up'):
        for index in range(len(snake)):
            if (index < 56):
                if (snake[index] == R and snake[index + 8] != B):
                    headPosition = index
                    break
            elif (index > 56):
                if (snake[index] == R and snake[index - 63 + 7] != B):
                    headPosition = index
                    break
        for index in range(len(snake)):
            if (index < 56):
                if (snake[index] == B and snake[index + 1] == b and snake[index - 8] == b and snake[index + 8] == b):
                    tempIndex = snake.index(R)
                    snake[tempIndex - 8] = R
                    snake[tempIndex] = B
                    snake[index] = b
                    break
                elif (snake[index] == B and snake[index - 1] == b and snake[index + 1] == b and snake[index + 8] == b):
                    tempIndex = snake.index(R)
                    snake[tempIndex - 8] = R
                    snake[tempIndex] = B
                    snake[index] = b
                    break
            elif (index >= 56):
                if (snake[index] == B and snake[index + 1] == b and snake[index - 8] == b and snake[index - 63 + 7] == b):
                    tempIndex = snake.index(R)
                    snake[tempIndex - 8] = R
                    snake[tempIndex] = B
                    snake[index] = b
                    break
                elif (snake[index] == B and snake[index - 1] == b and snake[index + 1] == b and snake[index - 63 + 7] == b):
                    tempIndex = snake.index(R)
                    snake[tempIndex - 8] = R
                    snake[tempIndex] = B
                    snake[index] = b
                    break
    elif (velocity == 'right' and previousVelocity == 'up'):
        for index in range(len(snake)):
            if (index < 56):
                if (snake[index] == R and snake[index - 1] != B):
                    headPosition = index
                    break
            elif (index > 56):
                if (snake[index] == R and snake[index - 1] != B):
                    headPosition = index
                    break
        for index in range(len(snake)):
            if (index < 56):
                # Before it takes the corner
                if (snake[index] == B and snake[index - 1] == b and snake[index + 1] == b and snake[index + 8] == b):
                    tempIndex = snake.index(R)
                    snake[tempIndex - 8] = R
                    snake[tempIndex] = B
                    snake[index] = b
                    break
                elif (snake[index] == B and snake[index - 1] == b and snake[index - 8] == b and snake[index + 8] == b):
                    tempIndex = snake.index(R)
                    snake[tempIndex - 8] = R
                    snake[tempIndex] = B
                    snake[index] = b
                    break
            elif (index >= 56):
                if (snake[index] == B and snake[index - 1] == b and snake[index - 8] == b and snake[index - 63 + 7] == b):
                    tempIndex = snake.index(R)
                    snake[tempIndex - 8] = R
                    snake[tempIndex] = B
                    snake[index] = b
                    break
                elif (snake[index] == B and snake[index - 1] == b and snake[index + 1] == b and snake[index - 63 + 7] == b):
                    tempIndex = snake.index(R)
                    snake[tempIndex - 8] = R
                    snake[tempIndex] = B
                    snake[index] = b
                    break
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

