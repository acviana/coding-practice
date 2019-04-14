'''
WORK IN PROGRESS

This is a maze navigation problem taken directly from Ch. 2 of "Classic
computer science problems in Python" used to demonstrate various search
algorithms.

This example is closely related to `knights_walk.py`.

Example Maze:

[ ][ ][ ][ ][ ][ ][ ][ ][G]
[X][ ][ ][ ][ ][ ][ ][ ][ ]
[ ][X][ ][ ][ ][ ][ ][ ][ ]
[ ][ ][ ][ ][ ][X][ ][ ][ ]
[ ][ ][ ][ ][ ][ ][ ][ ][X]
[ ][ ][ ][ ][ ][ ][ ][ ][ ]
[ ][ ][ ][ ][X][ ][ ][ ][ ]
[ ][ ][ ][ ][ ][X][ ][ ][ ]
[S][ ][ ][ ][ ][ ][X][ ][ ]

S = Start
G = Goal
'''

def build_maze():
    maze = [
        [True for item in range(9)] for item in range(9)
    ]

    blocked_squares = [
        [7, 0],
        [6, 1],
        [2, 4],
        [1, 5],
        [5, 5],
        [0, 6],
        [4, 8]

    ]

    for blocked_square in blocked_squares:
        x_position = blocked_square[0]
        y_position = blocked_square[1]
        maze[x_position][y_position] = False
    return maze


test_maze = build_maze()
assert sum([sum(row) for row in test_maze]) == 74


def get_possible_moves(maze, current_position, path):
    next_moves = []
    movement_options = [
        [0, 1],
        [1, 0],
        [0, -1],
        [-1, 0],
    ]
    for option in movement_options:
        x_position = current_position[0] + option[0]
        y_position = current_position[1] + option[1]
        if x_position < 0 or x_position >= len(maze[0]):
            continue
        if y_position < 0 or y_position >= len(maze):
            continue
        if maze[x_position][y_position] is False:
            continue
        if [x_position, y_position] in path:
            continue
        next_moves += [[option[0], option[1]]]
    return next_moves


assert get_possible_moves(test_maze, [0, 0], []) == [[0, 1], [1, 0]]
assert get_possible_moves(test_maze, [8, 8], []) == [[0, -1], [-1, 0]]

import pprint
for row in test_maze[::-1]:
    print(''.join(['[ ]' if item is True else '[X]' for item in row]))


def solve_maze(maze, start_position, goal_position):
    current_x_position = start_position[0]
    current_y_position = start_position[1]
    path = [start_position]
    possible_moves = []
    while True:
        if current_x_position == goal_position[0]:
            if current_y_position == goal_position[1]:
                return path
        possible_moves += get_possible_moves(
            maze, [current_x_position, current_y_position], path
        )
        if possible_moves == []:
            return False
        next_move = possible_moves.pop()
        current_x_position += next_move[0]
        current_y_position += next_move[1]
        path += [[current_x_position, current_y_position]]


if __name__ == '__main__':
    maze = build_maze()
    start_position = [0, 0]
    goal_position = [8, 8]
    print(solve_maze(maze, start_position, goal_position))

