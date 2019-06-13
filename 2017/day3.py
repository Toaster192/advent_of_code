import numpy as np

with open('day3-input') as f:
    input_data = f.read()

size = 600
matrix = np.empty([size, size], dtype=int)
starting_pos = size//2
curX = starting_pos
curY = starting_pos
square = 1
direction = [0, 1]
turns_to_turn = 0
moves_to_turn = 0


def turn():
    global direction
    direction = [-direction[1], direction[0]]

#    if   direction == [ 0,  1]:
#         direction =  [-1,  0]
#    elif direction == [-1,  0]:
#         direction =  [ 0, -1]
#    elif direction == [ 0, -1]:
#         direction =  [ 1,  0]
#    else:
#         direction =  [ 0,  1]


def move():
    global curX, curY, direction
    new_pos = [curX + direction[0], curY + direction[1]]
    curX, curY = new_pos


while square != int(input_data):
    matrix[curX, curY] = square
    square += 1
    move()
    if turns_to_turn == 0:
        turn()
        moves_to_turn += 1
        turns_to_turn = moves_to_turn // 2
    else:
        turns_to_turn -= 1


print("Pos: " + str(curX) + ", " + str(curY))

print("Answer: " + str(abs(starting_pos - curX) + abs(starting_pos - curY)))

# Part 2:

size = 100
matrix = np.zeros((size, size), dtype=int)
starting_pos = size//2
curX = starting_pos
curY = starting_pos
square = 1
direction = [0, 1]
turns_to_turn = 0
moves_to_turn = 0

while square <= int(input_data):
    matrix[curX, curY] = square
    move()
    if turns_to_turn == 0:
        turn()
        moves_to_turn += 1
        turns_to_turn = moves_to_turn // 2
    else:
        turns_to_turn -= 1

    square = (matrix[curX + 1,  1 + curY] +
              matrix[curX,      1 + curY] +
              matrix[curX + 1,      curY] +
              matrix[curX + 1, -1 + curY] +
              matrix[curX - 1,  1 + curY] +
              matrix[curX - 1,      curY] +
              matrix[curX,     -1 + curY] +
              matrix[curX - 1, -1 + curY])


print("Answer 2: " + str(square))
