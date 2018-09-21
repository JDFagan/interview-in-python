#!/bin/python3

import math
import os
import random
import re
import sys


"""
Blue Voyant Question by Adam Fletcher:
You’re making a video game in which a character explores a cave. The cave is a grid, and each turn the character can 
move up to 5 steps in any cardinal direction represented by an integer (0 for NORTH, 1 for SOUTH, 2 for EAST or 3 for 
WEST). The character can always use a potion to return to the entrance of the cave, provided the potion is strong enough 
to fly the character directly (eg, as the bird flies) back to the starting point. The potion’s strength is in number of 
grid squares the character must travel over to get back to the entrance, including the entrance square, rounded up to 
the nearest integer.


Given a 2D array of integers, containing rows of movements and distances, determine how strong the potion needs to be 
to get the character back to the starting point.

The array will look like the below, and will never have negative numbers in the distances:
[
  [0, 1],
  [1, 4],
  [0, 2]
]

And the expected return value from the function given the above array as an argument would be 1.

A note on HackerRank's "stdin":

If you look at the "stdin" tab on the editor, you'll see an input like:
1
2
0 3

HackerRank reads in lists-of-lists by first reading in the number of rows, then the number of columns, then finally the actual values. 

For example, the list of lists:
[
  [0, 1],
  [1, 4],
  [0, 2]
]

Would be written as:
3
2
0 1
1 4
0 2

Because there is 3 rows and 2 columns of values.
"""

# Complete the calculatePotionStrength function below.
def calculatePotionStrength(direction_and_distance):
    moves = {
        0: 0,  # North
        1: 0,  # South
        2: 0,  # East
        3: 0,  # West
        }
    for movement in direction_and_distance:
        direction = movement[0]
        steps = movement[1]
        moves[direction] += steps

    ns = abs(moves[0] - moves[1])
    ew = abs(moves[2] - moves[3])

    print("ns = {}".format(ns))
    print("ew = {}".format(ew))

    # c^2 = a^2 + b^2
    crow_flies = math.ceil(math.sqrt(ns**2 + ew**2))
    print("crow_flies = {}".format(crow_flies))
    return crow_flies


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    direction_and_distance_rows = int(input().strip())
    direction_and_distance_columns = int(input().strip())

    direction_and_distance = []

    for _ in range(direction_and_distance_rows):
        direction_and_distance.append(list(map(int, input().rstrip().split())))

    res = calculatePotionStrength(direction_and_distance)
    print(res)

    # fptr.write(str(res) + '\n')
    #
    # fptr.close()
