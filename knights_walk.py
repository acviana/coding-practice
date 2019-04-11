'''
The is an interview question I was asked, I enjoyed working on it and
wanted to clean up the solution and write some tests to help me
understand the solution a little better.

_ O _ O _
O _ _ _ O
_ _ X _ _
O _ _ _ O
_ O _ O _

Given width and height of an arbitrarily sized chessboard, write a
function that returns true if a knight placed at the top-left corner
can be moved in a single path such that it touches every square exactly
once.

Examples:

1x1 => True
1

2x2 => False
10
00

2x3 => False
100
001

3x3 => False
100
000
000

3x4 => True
1400
0025
3000
'''

# From any position these are the possible position deltas for the
# knight's movement.
position_deltas = [
    [2, 1],
    [2, -1],
    [-2, 1],
    [-2, -1],
    [1, 2],
    [1, -2],
    [-1, 2],
    [-1, -2],
]


def get_legal_moves(knight_position, board):
    '''
    For each possible delta check to see if the move is 1) on the board
    and 2) moves to a square that has not been touched before

    Args:
        knight_position (list): A two-item list containing the current
            knight's position as integers.
        board (list): A list containing n lists of length m containing
            Boolean elements, True if the square has already been
            visited, False if not.

    Returns
        legal_moves (list): A list of all the legal moves as 2-item
            lists of deltas.
    '''
    legal_moves= []
    for move in position_deltas:
        next_row = knight_position[0] + move[0]
        if not 0 <= next_row < len(board):
            continue
        next_col = knight_position[1] + move[1]
        if not 0 <= next_col < len(board[0]):
            continue
        if board[next_row][next_col] is True:
            continue
        legal_moves += [move]
    return legal_moves


def move_knight(knight_position, board):
    '''
    A recursive function that attempts all the possible walks on the
    board. Recursion is chosen here because it prevents us from having
    to store and save all the possible paths as we evaluate the tree of
    possible moves.

    Args:
        knight_position (list): A two-item list containing the current
            knight's position as integers.
        board (list): A list containing n lists of length m containing
            Boolean elements, True if the square has already been
            visited, False if not.

    Returns:
        result (bool): True if there is a possible knights walk that
            touches each square once. Otherwise False.
    '''
    legal_moves = get_legal_moves(knight_position, board)

    # If there are no more legal moves we check to see if we have
    # touched every square.
    if legal_moves == []:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] is False:
                    return False
        return True

    # If there are still legal moves we continue recursing. For each
    # move we update the board position but then reset it no solutions
    # are found.
    else:
        for move in legal_moves:
            next_pos = [
                knight_position[0] + move[0], knight_position[1] + move[1]
            ]
            board[next_pos[0]][next_pos[1]] = True
            solution_found = move_knight(next_pos, board)
            if not solution_found:
                board[next_pos[0]][next_pos[1]] = False
            else:
                return True

    return False


def build_board(n, m):
    '''
    Returns a "chessboard" represented an n-element list of m-element
    lists of False objects. Broken out here to facilitate generating
    test fixtures.

    Args:
        n (int): The width of the board.
        m (int): The length of the board.

    Returns:
        board (list): an n-element list of m-element lists of False
            objects
    '''
    board = []
    for i in range(n):
        board.append([False for item in range(m)])
    return board


def knights_walk(n, m):
    '''
    For a chessboard of size n x m determines if a "knight's walk"
    beginning at the upper left-hand corner is possible.

    Args:
        n (int): The width of the board.
        m (int): The length of the board.

    Returns:
        solution (bool): True is the walk is possible, False if not.
    '''
    board = build_board(n, m)
    knight_position = [0, 0]
    board[0][0] = True

    return move_knight(knight_position, board)


if __name__ == '__main__':

    board = build_board(5, 5)
    assert get_legal_moves([0, 0], board) == [[2, 1], [1, 2]]
    assert get_legal_moves([2, 2], board) == (
        [[2, 1], [2, -1], [-2, 1], [-2, -1], [1, 2], [1, -2], [-1, 2], [-1, -2]]
    )
    assert get_legal_moves([4, 4], board) == [[-2, -1], [-1, -2]]

    # Test the main function
    assert knights_walk(1, 1) is True
    assert knights_walk(2, 2) is False
    assert knights_walk(3, 3) is False
    assert knights_walk(3, 4) is True
    assert knights_walk(4, 3) is True
