import math
from copy import deepcopy

EMPTY = " "
O = 'O'
X = 'X'
BOARD_STATE = [[EMPTY, EMPTY, EMPTY],
               [EMPTY, EMPTY, EMPTY],
               [EMPTY, EMPTY, EMPTY]]

def winner(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != EMPTY:
            return 1 if board[i][0] == X else -1
        if board[0][i] == board[1][i] == board[2][i] != EMPTY:
            return 1 if board[0][i] == X else -1

    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return 1 if board[0][0] == X else -1
    if board[2][0] == board[1][1] == board[0][2] != EMPTY:
        return 1 if board[2][0] == X else -1
    
    if terminal(board):
        return 0

    return

def validate_move(board, move):
    if board[move[0]][move[1]] != EMPTY:
        return False

    else:
        return True

def terminal(board):
    for row in board:
        for val in row:
            #print(val)
            if val == EMPTY:
                return False
    return True

def actions(board):
    if terminal(board):
        return
    
    actions = []

    for i, row in enumerate(board):
        for j, val in enumerate(row):
            if val == EMPTY:
                actions.append((i, j))

    return actions

def turn(board):
    if terminal(board):
        return

    count = 0
    for row in board:
        for val in row:
            if val != EMPTY:
                count += 1

    if count % 2 == 0:
        return X
    else:
        return O

def move(board, action):
    board[action[0]][action[1]] = turn(board)
    return board

def ai(board):
    if terminal(board):
        return

    move = ()
    board_copy = deepcopy(board)

    if turn(board_copy) == X:
        _, move = maximize(board_copy)
    else:
        _, move = minimize(board_copy)

    return chr(move[0]+97)+f'{move[1]+1}'

def maximize(board):
    win = winner(board)
    if win != None:
        return (win, None)

    t_actions = actions(board)
    val = -math.inf
    a = ()
    for action in t_actions:
        board_copy = deepcopy(board)
        new_board = move(board_copy, action)
        move_val, _ = minimize(new_board)
        if move_val > val:
            val = move_val
            a = action

    return (val, a)

def minimize(board):
    win = winner(board)
    if win != None:
        return (win, None)

    t_actions = actions(board)
    val = math.inf
    a = ()
    for action in t_actions:
        board_copy = deepcopy(board)
        new_board = move(board_copy, action)
        move_val, _ = maximize(new_board)
        if move_val < val:
            val = move_val
            a = action

    return (val, a)
