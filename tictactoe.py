"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    x_count = sum(row.count(X) for row in board)
    o_count = sum(row.count(O) for row in board)
    return O if x_count > o_count else X


def actions(board):
    return {(i, j) for i in range(3) for j in range(3) if board[i][j] == EMPTY}



def result(board, action):
    if board[action[0]][action[1]] is not EMPTY:
        raise Exception("Invalid action")
    
    new_board = [row[:] for row in board]
    new_board[action[0]][action[1]] = player(board)
    return new_board


def winner(board):
    for player in [X, O]:
        # Check rows, columns, and diagonals
        if any(all(cell == player for cell in row) for row in board) or \
           any(all(board[i][j] == player for i in range(3)) for j in range(3)) or \
           all(board[i][i] == player for i in range(3)) or \
           all(board[i][2 - i] == player for i in range(3)):
            return player
    return None


def terminal(board):
    return winner(board) is not None or all(all(cell is not EMPTY for cell in row) for row in board)


def utility(board):
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    if terminal(board):
        return None

    if player(board) == X:
        value, move = max_value(board)
        return move
    else:
        value, move = min_value(board)
        return move

def max_value(board):
    if terminal(board):
        return utility(board), None
    
    v = float('-inf')
    move = None
    for action in actions(board):
        mv, _ = min_value(result(board, action))
        if mv > v:
            v, move = mv, action
    return v, move

def min_value(board):
    if terminal(board):
        return utility(board), None
    
    v = float('inf')
    move = None
    for action in actions(board):
        mv, _ = max_value(result(board, action))
        if mv < v:
            v, move = mv, action
    return v, move
