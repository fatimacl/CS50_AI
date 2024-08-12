"""
Tic Tac Toe Player
"""

import math
import copy

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
    """
    Returns player who has the next turn on a board.
    """
    count = sum(1 for row in board for item in row if item is not None)
    if count == 9:
        return None #End of game
    if count%2==0:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    {(0, 0), (0,1)}
    """
    possible_actions = set()
    for row_index, row in enumerate(board):
        for item_index, item in enumerate(row):
            if item == None:
                possible_actions.add((row_index, item_index))
    return possible_actions

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    row, col = action

    # Check if the action index is within bounds
    if not (0 <= row < len(board)) and 0 <= col < len(board[0]):
        raise Exception("Action is out of bounds.")

    
    # Check if the cell is already occupied
    if board[row][col] is not None:
        raise Exception("Cell is already occupied.")
    
    new_board = copy.deepcopy(board)
    current_player = player(board)
    
    # Apply the move
    new_board[row][col] = current_player
    
    return new_board

def winner(board):
    """
    Returns the winner of the game, if there is one. To do this i will check if theres a three in line verticalt, horizontally or diagonally
    """
    for row in board:
        if row[0] != None and row[0] == row[1] == row[2]:
            return row[0]

    for col in range(len(board)):
        if board[0][col] != None and board[0][col] == board[1][col]== board[2][col]:
            return board[0][col]
   
    # Check diagonals theres only two ways so I will check explicitily
    if board[0][0] != None and board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]
    if board[0][2] != None and board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]
    
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    if winner(board) != None:
        return True
    
    for row in board:
        if EMPTY in row:
            return False
    
    return True



def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    game_winner = winner(board)
    if game_winner == X:
        return 1
    elif game_winner == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    def max_value(board, alpha, beta):
        if terminal(board):
            return utility(board)
        v = float('-inf')
        for action in actions(board):
            v = max(v, min_value(result(board, action), alpha, beta))
            if v >= beta:
                return v
            alpha = max(alpha, v)
        return v

    def min_value(board, alpha, beta):
        if terminal(board):
            return utility(board)
        v = float('inf')
        for action in actions(board):
            v = min(v, max_value(result(board, action), alpha, beta))
            if v <= alpha:
                return v
            beta = min(beta, v)
        return v
    

    if terminal(board):
        return None

    current_player = player(board)
    best_action = None
    possible_actions = actions(board)
    alpha = float('-inf')
    beta = float('inf')
    

    if current_player == X:
        best_value = float('-inf')
        for action in possible_actions:
            action_value = min_value(result(board, action), alpha, beta)
            if action_value > best_value:
                best_value = action_value
                best_action = action
            alpha = max(alpha, best_value)
            
    else:
        best_value = float('inf')
        for action in possible_actions:
            action_value = max_value(result(board, action), alpha, beta)
            if action_value < best_value:
                best_value = action_value
                best_action = action
            beta = min(beta, best_value)
    
    return best_action




