
from sense_hat import SenseHat
from time import sleep
import os
from random import randint

os.system('clear')

sense = SenseHat()

# Setting variables
R = [255,0,0]
G = [0,255,0]
B = [0,0,255]
b = [0,0,0]
P = [255, 192, 203]
applePossibilities = []
score = 0

indices = []
snake = []
blank = []
headPosition = 27
previousVelocity = 'right'
velocity = 'right'

for elem in range(64):
    if (elem == 25 or elem == 26):
        snake.append(B)
    elif (elem == 27):
        snake.append(R)
    elif (elem == 29):
        snake.append(G)
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
            if (event.direction == 'up' and velocity == 'down'):
                None
            elif (event.direction == 'up'):
                print(previousVelocity, 'pressed')
                previousVelocity = velocity
                velocity = 'up'
            elif (event.direction == 'down' and velocity == 'up'):
                None
            elif (event.direction == 'down'):
                previousVelocity = velocity
                velocity = 'down'
            elif (event.direction == 'right' and velocity == 'left'):
                None
            elif (event.direction == 'right'):
                previousVelocity = velocity
                velocity = 'right'
            elif (event.direction == 'left' and velocity == 'right'):
                print(previousVelocity, 'pressed')
                None
            elif (event.direction == 'left'):
                print('here')
                previousVelocity = velocity
                velocity = 'left'
    # Begin code for walls == bad
    if (velocity == 'up' and any(snake.index(R) == num for num in range(9))):
        for elem in snake:
            if (elem == R or elem == B):
                snake[snake.index(elem)] = P
        break
    elif (velocity == 'down' and any(snake.index(R) == num for num in range(56, 64))):
        for elem in snake:
            if (elem == R or elem == B):
                snake[snake.index(elem)] = P
        break
    elif (velocity == 'left' and any(snake.index(R) == num for num in range(0, 56, 8))):
        for elem in snake:
            if (elem == R or elem == B):
                snake[snake.index(elem)] = P
        break
    elif (velocity == 'right' and any(snake.index(R) == num for num in range(7, 63, 8))):
        for elem in snake:
            if (elem == R or elem == B):
                snake[snake.index(elem)] = P
        break
    
    # Begin code for 'apple physics'
    if (velocity == 'up'):
        if (snake.index(R) - 8 == snake.index(G)):
            score += 1;
            print('passed')
            tempIndex = snake.index(R)
            snake[tempIndex - 8] = R
            snake[tempIndex] = B
            for index in range(len(snake)):
                if (snake[index] == b):
                    applePossibilities.append(index)
            appleIndex = randint(0, 64)
            print(applePossibilities)
            while True:
                if any(appleIndex == elem for elem in applePossibilities):
                    snake[appleIndex] = G
                    break
                elif all(appleIndex != elem for elem in applePossibilities):
                    appleIndex = randint(0, 64)
    elif (velocity == 'down'):
        if (snake.index(R) + 8 == snake.index(G)):
            score += 1;
            print('passed')
            tempIndex = snake.index(R)
            snake[tempIndex + 8] = R
            snake[tempIndex] = B
            for index in range(len(snake)):
                if (snake[index] == b):
                    applePossibilities.append(index)
            appleIndex = randint(0, 64)
            print(applePossibilities)
            while True:
                if any(appleIndex == elem for elem in applePossibilities):
                    snake[appleIndex] = G
                    break
                elif all(appleIndex != elem for elem in applePossibilities):
                    appleIndex = randint(0, 64)
    elif (velocity == 'left'):
        if (snake.index(R) - 1 == snake.index(G)):
            score += 1;
            print('passed')
            tempIndex = snake.index(R)
            snake[tempIndex - 1] = R
            snake[tempIndex] = B
            for index in range(len(snake)):
                if (snake[index] == b):
                    applePossibilities.append(index)
            appleIndex = randint(0, 64)
            print(applePossibilities)
            while True:
                if any(appleIndex == elem for elem in applePossibilities):
                    snake[appleIndex] = G
                    break
                elif all(appleIndex != elem for elem in applePossibilities):
                    appleIndex = randint(0, 64)
    elif (velocity == 'right'):
        if (snake.index(R) + 1 == snake.index(G)):
            score += 1;
            print('passed')
            tempIndex = snake.index(R)
            snake[tempIndex + 1] = R
            snake[tempIndex] = B
            for index in range(len(snake)):
                if (snake[index] == b):
                    applePossibilities.append(index)
            appleIndex = randint(0, 64)
            print(applePossibilities)
            while True:
                if any(appleIndex == elem for elem in applePossibilities):
                    snake[appleIndex] = G
                    break
                elif all(appleIndex != elem for elem in applePossibilities):
                    appleIndex = randint(0, 64)
    
    # Begin code for normal snake movement
    # (Done)
    if (velocity == 'up' and previousVelocity == 'right'):
        for index in range(len(snake)):
            if (index < 56):
                if (snake[index] == R and snake[index + 8] != B):
                    headPosition = index
                    break
            elif (index >= 56):
                if (snake[index] == R and snake[index - 63 + 7] != B):
                    headPosition = index
                    break
        for index in range(len(snake)):
            if (index < 56):
                if (snake[index] == B and snake[index - 1] !=B and snake[index - 8] !=B and snake[index + 8] !=B):
                    tempIndex = snake.index(R)
                    snake[tempIndex - 8] = R
                    snake[tempIndex] = B
                    snake[index] = b
                    break
                elif (snake[index] == B and snake[index - 1] !=B and snake[index + 1] !=B and snake[index + 8] !=B):
                    tempIndex = snake.index(R)
                    snake[tempIndex - 8] = R
                    snake[tempIndex] = B
                    snake[index] = b
                    break
            elif (index >= 56):
                if (snake[index] == B and snake[index - 1] !=B and snake[index - 8] !=B and snake[index - 63 + 7] !=B):
                    tempIndex = snake.index(R)
                    snake[tempIndex - 8] = R
                    snake[tempIndex] = B
                    snake[index] = b
                    break
                elif (snake[index] == B and snake[index - 1] !=B and snake[index + 1] !=B and snake[index - 63 + 7] !=B):
                    tempIndex = snake.index(R)
                    snake[tempIndex - 8] = R
                    snake[tempIndex] = B
                    snake[index] = b
                    break
    # Done
    elif (velocity == 'up' and previousVelocity == 'left'):
        for index in range(len(snake)):
            if (index < 56):
                if (snake[index] == R and snake[index + 8] != B):
                    headPosition = index
                    break
            elif (index >= 56):
                if (snake[index] == R and snake[index - 63 + 7] != B):
                    headPosition = index
                    break
        for index in range(len(snake)):
            if (index < 56):
                # Before it takes the turn
                if (snake[index] == B and snake[index + 1] != B and snake[index - 8] != B and snake[index + 8] != B):
                    tempIndex = snake.index(R)
                    snake[tempIndex - 8] = R
                    snake[tempIndex] = B
                    snake[index] = b
                    break
                # After it takes the corner
                elif (snake[index] == B and snake[index - 1] != B and snake[index + 1] != B and snake[index + 8] != B):
                    tempIndex = snake.index(R)
                    snake[tempIndex - 8] = R
                    snake[tempIndex] = B
                    snake[index] = b
                    break
            elif (index >= 56):
                if (snake[index] == B and snake[index + 1] != B and snake[index - 8] != B and snake[index - 63 + 7] != B):
                    tempIndex = snake.index(R)
                    snake[tempIndex - 8] = R
                    snake[tempIndex] = B
                    snake[index] = b
                    break
                elif (snake[index] == B and snake[index - 1] != B and snake[index + 1] != B and snake[index - 63 + 7] != B):
                    tempIndex = snake.index(R)
                    snake[tempIndex - 8] = R
                    snake[tempIndex] = B
                    snake[index] = b
                    break
    # Done
    elif (velocity == 'left' and previousVelocity == 'up'):
        for index in range(len(snake)):
            if (index < 56):
                if (snake[index] == R and snake[index + 1] != B):
                    headPosition = index
                    break
            elif (index >= 56):
                if (snake[index] == R and snake[index + 1] != B):
                    headPosition = index
                    break
        for index in range(len(snake)):
            if (index < 56):
                # Before it takes the corner
                if (snake[index] == B and snake[index + 1] != B and snake[index - 1] != B and snake[index + 8] != B):
                    tempIndex = snake.index(R)
                    snake[tempIndex - 1] = R
                    snake[tempIndex] = B
                    snake[index] = b
                    break
                # After it takes the corner
                elif (snake[index] == B and snake[index + 1] != B and snake[index + 8] != B and snake[index - 8] != B):
                    tempIndex = snake.index(R)
                    snake[tempIndex - 1] = R
                    snake[tempIndex] = B
                    snake[index] = b
                    break
            elif (index >= 56):
                if (snake[index] == B and snake[index + 1] != B and snake[index - 1] != B and snake[index - 63 + 7] != B):
                    tempIndex = snake.index(R)
                    snake[tempIndex - 1] = R
                    snake[tempIndex] = B
                    snake[index] = b
                    break
                elif (snake[index] == B and snake[index - 1] != B and snake[index - 63 + 7] != B and snake[index - 8] != B):
                    tempIndex = snake.index(R)
                    snake[tempIndex - 1] = R
                    snake[tempIndex] = B
                    snake[index] = b
                    break
    # DOne
    elif (velocity == 'left' and previousVelocity == 'down'):
        for index in range(len(snake)):
            if (index < 56):
                if (snake[index] == R and snake[index + 1] != B):
                    headPosition = index
                    break
            elif (index >= 56):
                if (snake[index] == R and snake[index + 1] != B):
                    headPosition = index
                    break
        for index in range(len(snake)):
            if (index < 56):
                # Before it takes the corner
                if (snake[index] == B and snake[index + 1] != B and snake[index - 1] != B and snake[index - 8] != B):
                    tempIndex = snake.index(R)
                    snake[tempIndex - 1] = R
                    snake[tempIndex] = B
                    snake[index] = b
                    break
                # After it takes the corner
                elif (snake[index] == B and snake[index + 1] != B and snake[index + 8] != B and snake[index - 8] != B):
                    tempIndex = snake.index(R)
                    snake[tempIndex - 1] = R
                    snake[tempIndex] = B
                    snake[index] = b
                    break
            elif (index >= 56):
                if (snake[index] == B and snake[index + 1] != B and snake[index - 1] != B and snake[index - 63 + 7] != B):
                    tempIndex = snake.index(R)
                    snake[tempIndex - 8] = R
                    snake[tempIndex] = B
                    snake[index] = b
                    break
                elif (snake[index] == B and snake[index - 1] != B and snake[index - 63 + 7] != B and snake[index - 8] != B):
                    tempIndex = snake.index(R)
                    snake[tempIndex - 8] = R
                    snake[tempIndex] = B
                    snake[index] = b
                    break
    # (Done)
    elif (velocity == 'right' and previousVelocity == 'up'):
        for index in range(len(snake)):
            if (index < 56):
                if (snake[index] == R and snake[index - 1] != B):
                    headPosition = index
                    break
            elif (index >= 56):
                if (snake[index] == R and snake[index - 1] != B):
                    headPosition = index
                    break
        for index in range(len(snake)):
            if (index < 56):
                # Before it takes the corner
                if (snake[index] == B and snake[index - 1] != B and snake[index + 1] != B and snake[index + 8] != B):
                    tempIndex = snake.index(R)
                    snake[tempIndex + 1] = R
                    snake[tempIndex] = B
                    snake[index] = b
                    break
                elif (snake[index] == B and snake[index - 1] != B and snake[index - 8] != B and snake[index + 8] != B):
                    tempIndex = snake.index(R)
                    snake[tempIndex + 1] = R
                    snake[tempIndex] = B
                    snake[index] = b
                    break
            elif (index >= 56):
                if (snake[index] == B and snake[index - 1] != B and snake[index - 8] != B and snake[index - 63 + 7] != B):
                    tempIndex = snake.index(R)
                    snake[tempIndex + 1] = R
                    snake[tempIndex] = B
                    snake[index] = b
                    break
                elif (snake[index] == B and snake[index - 1] != B and snake[index + 1] != B and snake[index - 63 + 7] != B):
                    tempIndex = snake.index(R)
                    snake[tempIndex + 1] = R
                    snake[tempIndex] = B
                    snake[index] = b
                    break
    # Done
    elif (velocity == 'right' and previousVelocity == 'down'):
        for index in range(len(snake)):
            if (index < 56):
                if (snake[index] == R and snake[index - 1] != B):
                    headPosition = index
                    break
            elif (index >= 56):
                if (snake[index] == R and snake[index - 1] != B):
                    headPosition = index
                    break
        for index in range(len(snake)):
            if (index < 56):
                # Before it takes the corner
                if (snake[index] == B and snake[index - 1] != B and snake[index + 1] != B and snake[index - 8] != B):
                    tempIndex = snake.index(R)
                    snake[tempIndex + 1] = R
                    snake[tempIndex] = B
                    snake[index] = b
                    break
                # After it takes the corner
                elif (snake[index] == B and snake[index - 1] != B and snake[index - 8] != B and snake[index + 8] != B):
                    tempIndex = snake.index(R)
                    snake[tempIndex + 1] = R
                    snake[tempIndex] = B
                    snake[index] = b
                    break
            elif (index >= 56):
                if (snake[index] == B and snake[index - 1] != B and snake[index - 8] != B and snake[index - 8] != B):
                    tempIndex = snake.index(R)
                    snake[tempIndex + 1] = R
                    snake[tempIndex] = B
                    snake[index] = b
                    break
                elif (snake[index] == B and snake[index - 1] != B and snake[index + 1] != B and snake[index - 63 + 7] != B):
                    tempIndex = snake.index(R)
                    snake[tempIndex + 1] = R
                    snake[tempIndex] = B
                    snake[index] = b
                    break
    # Done
    elif (velocity == 'down' and previousVelocity == 'right'):
        for index in range(len(snake)):
            if (index < 56):
                if (snake[index] == R and snake[index - 8] != B):
                    headPosition = index
                    break
            elif (index >= 56):
                if (snake[index] == R and snake[index - 8] != B):
                    headPosition = index
                    break
        for index in range(len(snake)):
            if (index < 56):
                # Before it takes the corner
                if (snake[index] == B and snake[index - 1] != B and snake[index + 8] != B and snake[index - 8] != B):
                    tempIndex = snake.index(R)
                    snake[tempIndex + 8] = R
                    snake[tempIndex] = B
                    snake[index] = b
                    break
                # After it takes the corner
                elif (snake[index] == B and snake[index - 1] != B and snake[index - 8] != B and snake[index + 1] != B):
                    tempIndex = snake.index(R)
                    print(tempIndex)
                    if (tempIndex >= 56):
                        snake[tempIndex - 63 + 7] = R
                        snake[tempIndex] = B
                        snake[index] = b
                        break
                    else:
                        snake[tempIndex + 8] = R
                        snake[tempIndex] = B
                        snake[index] = b
                        break
            elif (index >= 56):
                if (snake[index] == B and snake[index - 1] != B and snake[index - 63 + 7] != B and snake[index - 8] != B):
                    tempIndex = snake.index(R)
                    snake[tempIndex - 63 + 7] = R
                    snake[tempIndex] = B
                    snake[index] = b
                    break
                elif (snake[index] == B and snake[index - 1] != B and snake[index - 8] != B and snake[index + 1] != B):
                    tempIndex = snake.index(R)
                    snake[tempIndex - 63+ 7] = R
                    snake[tempIndex] = B
                    snake[index] = b
                    break
    # DOne
    elif (velocity == 'down' and previousVelocity == 'left'):
        for index in range(len(snake)):
            if (index < 56):
                if (snake[index] == R and snake[index - 8] != B):
                    headPosition = index
                    break
            elif (index >= 56):
                if (snake[index] == R and snake[index - 8] != B):
                    headPosition = index
                    break
        for index in range(len(snake)):
            if (index < 56):
                # Before it takes the corner
                if (snake[index] == B and snake[index + 1] != B and snake[index + 8] != B and snake[index - 8] != B):
                    tempIndex = snake.index(R)
                    snake[tempIndex + 8] = R
                    snake[tempIndex] = B
                    snake[index] = b
                    break
                # After it takes the corner
                elif (snake[index] == B and snake[index - 1] != B and snake[index - 8] != B and snake[index + 1] != B):
                    tempIndex = snake.index(R)
                    print(tempIndex)
                    if (tempIndex >= 56):
                        snake[tempIndex - 63 + 7] = R
                        snake[tempIndex] = B
                        snake[index] = b
                        break
                    else:
                        snake[tempIndex + 8] = R
                        snake[tempIndex] = B
                        snake[index] = b
                        break
            elif (index >= 56):
                if (snake[index] == B and snake[index - 1] != B and snake[index - 63 + 7] != B and snake[index - 8] != B):
                    tempIndex = snake.index(R)
                    snake[tempIndex - 63 + 7] = R
                    snake[tempIndex] = B
                    snake[index] = b
                    break
                elif (snake[index] == B and snake[index - 1] != B and snake[index - 8] != B and snake[index + 1] != B):
                    tempIndex = snake.index(R)
                    snake[tempIndex - 63+ 7] = R
                    snake[tempIndex] = B
                    snake[index] = b
                    break
    # Done
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

    sense.set_pixels(snake)
sense.show_message(f'Score: {score}')
