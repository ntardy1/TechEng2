# Snake V1
The file snakeV1.py was the first version of the game. The snake's movement was incredibly overcomplicated and the head of the snake could not take a new 
turn if the tail of the snake had not finished the last turn. So the maximum length that the snake could be before the game crashed was 8.
# Snake V2
This is the current version of the game. The snake movement portion of the program was significantly condensed down from V1. Addtionally, V2 allows the
head of the snake to take a new turn, even if its tail hasn't completed the last turn. This version still has problems, however. Occasionally, when the 
head of the snake and the tail of the snake are on opposite sides of the board but in the same row, the game will crash. There is also an 
occasional problem with the spawning of the apple, where it will spawn in such a place that the program thinks either the apple or the head of the snake
is no longer in the main 'snake' list, which crashed the game.
