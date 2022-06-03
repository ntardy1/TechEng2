
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
P = [255, 255, 255]
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
                None
            elif (event.direction == 'left'):
                previousVelocity = velocity
                velocity = 'left'
                
    # Begin code for walls == bad
    if (velocity == 'up' and any(snake.index(R) == num for num in range(8))):
        for index in range(len(snake)):
            if (snake[index] == R or snake[index] == B):
                snake[index] = P
            elif (snake[index] == G):
                snake[index] = b
        break
    elif (velocity == 'down' and any(snake.index(R) == num for num in range(56, 64))):
        for index in range(len(snake)):
            if (snake[index] == R or snake[index] == B):
                snake[index] = P
            elif (snake[index] == G):
                snake[index] = b
        break
    elif (velocity == 'left' and any(snake.index(R) == num for num in range(0, 57, 8))):
        for index in range(len(snake)):
            if (snake[index] == R or snake[index] == B):
                snake[index] = P
            elif (snake[index] == G):
                snake[index] = b
        break
    elif (velocity == 'right' and any(snake.index(R) == num for num in range(7, 64, 8))):
        for index in range(len(snake)):
            if (snake[index] == R or snake[index] == B):
                snake[index] = P
            elif (snake[index] == G):
                snake[index] = b
        break
    
    # Begin code for 'apple physics'
    if (velocity == 'up'):
        if (snake.index(R) - 8 == snake.index(G)):
            score += 1;
            tempIndex = snake.index(R)
            snake[tempIndex - 8] = R
            snake[tempIndex] = B
            for index in range(len(snake)):
                if (snake[index] == b):
                    applePossibilities.append(index)
            appleIndex = randint(0, 64)
            while True:
                if any(appleIndex == elem for elem in applePossibilities):
                    snake[appleIndex] = G
                    break
                elif all(appleIndex != elem for elem in applePossibilities):
                    appleIndex = randint(0, 64)
    elif (velocity == 'down'):
        if (snake.index(R) + 8 == snake.index(G)):
            score += 1;
            tempIndex = snake.index(R)
            snake[tempIndex + 8] = R
            snake[tempIndex] = B
            for index in range(len(snake)):
                if (snake[index] == b):
                    applePossibilities.append(index)
            appleIndex = randint(0, 64)
            while True:
                if any(appleIndex == elem for elem in applePossibilities):
                    snake[appleIndex] = G
                    break
                elif all(appleIndex != elem for elem in applePossibilities):
                    appleIndex = randint(0, 64)
    elif (velocity == 'left'):
        if (snake.index(R) - 1 == snake.index(G)):
            score += 1;
            tempIndex = snake.index(R)
            snake[tempIndex - 1] = R
            snake[tempIndex] = B
            for index in range(len(snake)):
                if (snake[index] == b):
                    applePossibilities.append(index)
            appleIndex = randint(0, 64)
            while True:
                if any(appleIndex == elem for elem in applePossibilities):
                    snake[appleIndex] = G
                    break
                elif all(appleIndex != elem for elem in applePossibilities):
                    appleIndex = randint(0, 64)
    elif (velocity == 'right'):
        if (snake.index(R) + 1 == snake.index(G)):
            score += 1;
            tempIndex = snake.index(R)
            snake[tempIndex + 1] = R
            snake[tempIndex] = B
            for index in range(len(snake)):
                if (snake[index] == b):
                    applePossibilities.append(index)
            appleIndex = randint(0, 64)
            while True:
                if any(appleIndex == elem for elem in applePossibilities):
                    snake[appleIndex] = G
                    break
                elif all(appleIndex != elem for elem in applePossibilities):
                    appleIndex = randint(0, 64)
                    
    # Begin code for normal snake movement
    for index in range(len(snake)):
        firstList = [-1, 1, -8, 8]
        topFirstList = [-1, 1, 8]
        rightFirstList = [-1, -8, 8]
        leftFirstList = [1, -8, 8]
        bottomFirstList = [-1, 1, -8]
        bottomLeftFirstList = [1, -8]
        bottomRightFirstList = [-1, -8]
        secondList = [-1, 1, -8, 8]
        topSecondList = [-1, 1, 8]
        leftSecondList = [1, -8, 8]
        rightSecondList = [-1, 8, -8]
        bottomSecondList = [-1, 1, -8]
        bottomLeftSecondList = [1, 8]
        bottomRightSecondList = [-1, -8]
        tempRedIndex = snake.index(R)
        tempBlueIndex = -1
        num = 0
        # Checking if the index is the bottom right corner
        if (index == 63):
            if (snake[index] == B):
                while num < len(bottomRightFirstList):
                    if (snake[index + bottomRightFirstList[num]] == b or snake[index + bottomRightFirstList[num]] == G):
                        bottomRightFirstList.remove(bottomRightFirstList[num])
                        if (len(bottomRightFirstList) == 1):
                            tempBlueIndex = index
                            break
                        else:
                            num = 0
                    else:
                        num += 1
            if (snake[index] == R):
                for num in range(4):
                    if (len(bottomRightSecondList) == 1):
                        break
                    elif any(snake[index + bottomRightSecondList[elem]] != B for elem in range(len(bottomRightSecondList))):
                        None
        # Checking if the index is the bottom left corner
        elif (index == 56):
            if (snake[index] == B):
                while num < len(bottomLeftFirstList):
                    if (snake[index + bottomLeftFirstList[num]] == b or snake[index + bottomLeftFirstList[num]] == G):
                        bottomLeftFirstList.remove(bottomLeftFirstList[num])
                        if (len(bottomLeftFirstList) == 1):
                            tempBlueIndex = index
                            break
                        else:
                            num = 0
                    else:
                        num += 1
            if (snake[index] == R):
                for num in range(4):
                    if (len(bottomLeftSecondList) == 1):
                        break
                    elif any(snake[index + bottomLeftSecondList[elem]] != B for elem in range(len(bottomLeftSecondList))):
                        None
        # Checking if the index is along the right side of the LED matrix
        elif (index + 1 % 8 == 0):
            if (snake[index] == B):
                while num < len(rightFirstList):
                    if (snake[index + rightFirstList[num]] == b or snake[index + rightFirstList[num]] == G):
                        rightFirstList.remove(rightFirstList[num])
                        if (len(rightFirstList) == 1):
                            tempBlueIndex = index
                            break
                        else:
                            num = 0
                    else:
                        num += 1
            if (snake[index] == R):
                for num in range(4):
                    if (len(rightSecondList) == 1):
                        break
                    elif any(snake[index + rightSecondList[elem]] != B for elem in range(len(rightSecondList))):
                        None
        # Checking if the index is along the left side of the LED matrix
        elif (index % 8 == 0):
            if (snake[index] == B):
                while num < len(leftFirstList):
                    if (snake[index + leftFirstList[num]] == b or snake[index + leftFirstList[num]] == G):
                        leftFirstList.remove(leftFirstList[num])
                        if (len(leftFirstList) == 1):
                            tempBlueIndex = index
                            break
                        else:
                            num = 0
                    else:
                        num += 1
            if (snake[index] == R):
                for num in range(4):
                    if (len(leftSecondList) == 1):
                        break
                    elif any(snake[index + leftSecondList[elem]] != B for elem in range(len(leftSecondList))):
                        None
        # Checking if the index is in the bottom row
        elif (index >= 57 and index <= 62):
            if (snake[index] == B):
                while num < len(bottomFirstList):
                    if (snake[index + bottomFirstList[num]] == b or snake[index + bottomFirstList[num]] == G):
                        bottomFirstList.remove(bottomFirstList[num])
                        if (len(bottomFirstList) == 1):
                            tempBlueIndex = index
                            break
                        else:
                            num = 0
                    else:
                        num += 1
            if (snake[index] == R):
                for num in range(4):
                    if (len(bottomSecondList) == 1):
                        break
                    elif any(snake[index + bottomSecondList[elem]] != B for elem in range(len(bottomSecondList))):
                        None
        # Checking if the index is in the top row
        elif (index >= 1 and index <= 6):
            if (snake[index] == B):
                while num < len(topFirstList):
                    if (snake[index + topFirstList[num]] == b or snake[index + topFirstList[num]] == G):
                        topFirstList.remove(topFirstList[num])
                        if (len(topFirstList) == 1):
                            tempBlueIndex = index
                            break
                        else:
                            num = 0
                    else:
                        num += 1
            if (snake[index] == R):
                for num in range(4):
                    if (len(topSecondList) == 1):
                        break
                    elif any(snake[index + topSecondList[elem]] != B for elem in range(len(topSecondList))):
                        None
                        
        else:
            if (snake[index] == B):
                while num < len(firstList):
                    if (snake[index + firstList[num]] == b or snake[index + firstList[num]] == G):
                        firstList.remove(firstList[num])
                        if (len(firstList) == 1):
                            tempBlueIndex = index
                            break
                        else:
                            num = 0
                    else:
                        num += 1
            if (snake[index] == R):
                for num in range(4):
                    if (len(secondList) == 1):
                        break
                    elif any(snake[index + secondList[elem]] != B for elem in range(len(secondList))):
                        None
            
        if (tempBlueIndex == -1):
            None
        else:
            if (velocity == 'up'):
                snake[tempRedIndex - 8] = R
                snake[tempRedIndex] = B
                snake[tempBlueIndex] = b
            elif (velocity == 'down'):
                snake[tempRedIndex + 8] = R
                snake[tempRedIndex] = B
                snake[tempBlueIndex] = b
            elif (velocity == 'left'):
                snake[tempRedIndex - 1] = R
                snake[tempRedIndex] = B
                snake[tempBlueIndex] = b
            elif (velocity == 'right'):
                snake[tempRedIndex + 1] = R
                snake[tempRedIndex] = B
                snake[tempBlueIndex] = b
            break
    sense.set_pixels(snake)
sense.show_message(f'Score: {score}')
