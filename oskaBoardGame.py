import copy

"""
This function prints your board.
This function was given from Piazza (solution of hw3).
"""
def print_board(state):
    output_str = "\n"
    j=1
    output_str += '--' * len(state)
    output_str += "\n"
    for i,row in enumerate(state):
        if i<=len(state)//2 and i>0: j+=1
        else: j-=1
        output_str+= ' '*j
        for c in row:
            output_str+='|'+c
        output_str+='|\n'
        output_str+='--' * len(state)
        output_str+= "\n"
    print(output_str)
    return output_str

"""
This function generates all possible next move of a given white piece.
arguments: game board, row index, column index
return: list of all possible next move of a given white piece
"""
def move_white(board, row, col):
    # print("move_white called") # Need comment out
    possible_move = []
    row_centerLine = (len(board) - 1) / 2 # row index of the center line of a game board

    # When the given white piece is at the bottom row of the game board, there is no possible move.
    if (len(board) == row + 1):
        return []

    # When the given white piece is at the above center line.
    elif (row < row_centerLine - 1):
        # The given white piece moves one step downward if possible.
        if (col == 0): # When the given white piece is at the left edge of the game board.
            if (board[row+1][col] == '-'):
                new_board = copy.deepcopy(board)
                tmp_curr_row = list(new_board[row])
                tmp_next_row = list(new_board[row+1])
                tmp_curr_row[col], tmp_next_row[col] = tmp_next_row[col], tmp_curr_row[col]
                new_board[row] = ''.join(tmp_curr_row)
                new_board[row+1] = ''.join(tmp_next_row)
                possible_move.append(new_board)

        if (col == (len(board[row]) - 1)): # when the given white piece is at the right edge of the game board
            if (board[row+1][len(board[row+1]) - 1] == '-'):
                new_board = copy.deepcopy(board)
                tmp_curr_row = list(new_board[row])
                tmp_next_row = list(new_board[row+1])
                tmp_curr_row[col], tmp_next_row[len(board[row+1]) - 1] = tmp_next_row[len(board[row+1]) - 1], tmp_curr_row[col]
                new_board[row] = ''.join(tmp_curr_row)
                new_board[row+1] = ''.join(tmp_next_row)
                possible_move.append(new_board)

        if (col != 0 and col != (len(board[row]) - 1)): # when the given piece is neither at left edge nor right edge
            if (board[row+1][col] == '-'):
                new_board = copy.deepcopy(board)
                tmp_curr_row = list(new_board[row])
                tmp_next_row = list(new_board[row+1])
                tmp_curr_row[col], tmp_next_row[col] = tmp_next_row[col], tmp_curr_row[col]
                new_board[row] = ''.join(tmp_curr_row)
                new_board[row+1] = ''.join(tmp_next_row)
                possible_move.append(new_board)
            if (board[row+1][col-1] == '-'):
                new_board = copy.deepcopy(board)
                tmp_curr_row = list(new_board[row])
                tmp_next_row = list(new_board[row+1])
                tmp_curr_row[col], tmp_next_row[col-1] = tmp_next_row[col-1], tmp_curr_row[col]
                new_board[row] = ''.join(tmp_curr_row)
                new_board[row+1] = ''.join(tmp_next_row)
                possible_move.append(new_board)

        # The given white piece jumps a black piece and capture the black piece.
        if (col == 0 or col == 1): # When the given white piece is at either the two most left edges of the game board, there is only 1 jump direction.
            if (board[row+1][col] == 'b' and board[row+2][col] == '-'):
                new_board = copy.deepcopy(board)
                tmp_curr_row = list(new_board[row])
                tmp_next_row = list(new_board[row+1])
                tmp_next_next_row = list(new_board[row+2])
                tmp_curr_row[col], tmp_next_next_row[col] = tmp_next_next_row[col], tmp_curr_row[col]
                tmp_next_row[col] = '-'
                new_board[row] = ''.join(tmp_curr_row)
                new_board[row+1] = ''.join(tmp_next_row)
                new_board[row+2] = ''.join(tmp_next_next_row)
                possible_move.append(new_board)

        if (col == (len(board[row]) - 1) or col == (len(board[row]) - 2)): # When the given white piece is at either the two most right edges of the game board, there is only one jump direction.
            if (board[row+1][col-1] == 'b' and board[row+2][col-2] == '-'):
                new_board = copy.deepcopy(board)
                tmp_curr_row = list(new_board[row])
                tmp_next_row = list(new_board[row+1])
                tmp_next_next_row = list(new_board[row+2])
                tmp_curr_row[col], tmp_next_next_row[col-2] = tmp_next_next_row[col-2], tmp_curr_row[col]
                tmp_next_row[col-1] = '-'
                new_board[row] = ''.join(tmp_curr_row)
                new_board[row+1] = ''.join(tmp_next_row)
                new_board[row+2] = ''.join(tmp_next_next_row)
                possible_move.append(new_board)

        if (1 < col and col < (len(board[row]) - 2)): # When the given white piece is at neither the two most left edges nor two most right edges of the game board, there are two jump directions.
            if (board[row+1][col] == 'b' and board[row+2][col] == '-'):
                new_board = copy.deepcopy(board)
                tmp_curr_row = list(new_board[row])
                tmp_next_row = list(new_board[row+1])
                tmp_next_next_row = list(new_board[row+2])
                tmp_curr_row[col], tmp_next_next_row[col] = tmp_next_next_row[col], tmp_curr_row[col]
                tmp_next_row[col] = '-'
                new_board[row] = ''.join(tmp_curr_row)
                new_board[row+1] = ''.join(tmp_next_row)
                new_board[row+2] = ''.join(tmp_next_next_row)
                possible_move.append(new_board)
            if (board[row+1][col-1] == 'b' and board[row+2][col-2] == '-'):
                new_board = copy.deepcopy(board)
                tmp_curr_row = list(new_board[row])
                tmp_next_row = list(new_board[row+1])
                tmp_next_next_row = list(new_board[row+2])
                tmp_curr_row[col], tmp_next_next_row[col-2] = tmp_next_next_row[col-2], tmp_curr_row[col]
                tmp_next_row[col-1] = '-'
                new_board[row] = ''.join(tmp_curr_row)
                new_board[row+1] = ''.join(tmp_next_row)
                new_board[row+2] = ''.join(tmp_next_next_row)
                possible_move.append(new_board)

    # When the given white piece is at the one row above from the center line og the game board.
    elif (row == row_centerLine - 1):
        # The given white piece moves one step downward if possible.
        if (col == 0): # When the given white piece is at the left edge of the game board.
            if (board[row+1][col] == '-'):
                new_board = copy.deepcopy(board)
                tmp_curr_row = list(new_board[row])
                tmp_next_row = list(new_board[row+1])
                tmp_curr_row[col], tmp_next_row[col] = tmp_next_row[col], tmp_curr_row[col]
                new_board[row] = ''.join(tmp_curr_row)
                new_board[row+1] = ''.join(tmp_next_row)
                possible_move.append(new_board)

        if (col == (len(board[row]) - 1)): # when the given white piece is at the right edge of the game board
            if (board[row+1][len(board[row+1]) - 1] == '-'):
                new_board = copy.deepcopy(board)
                tmp_curr_row = list(new_board[row])
                tmp_next_row = list(new_board[row+1])
                tmp_curr_row[col], tmp_next_row[len(board[row+1]) - 1] = tmp_next_row[len(board[row+1]) - 1], tmp_curr_row[col]
                new_board[row] = ''.join(tmp_curr_row)
                new_board[row+1] = ''.join(tmp_next_row)
                possible_move.append(new_board)

        if (col != 0 and col != (len(board[row]) - 1)): # when the given piece is neither at left edge nor right edge
            if (board[row+1][col] == '-'):
                new_board = copy.deepcopy(board)
                tmp_curr_row = list(new_board[row])
                tmp_next_row = list(new_board[row+1])
                tmp_curr_row[col], tmp_next_row[col] = tmp_next_row[col], tmp_curr_row[col]
                new_board[row] = ''.join(tmp_curr_row)
                new_board[row+1] = ''.join(tmp_next_row)
                possible_move.append(new_board)
            if (board[row+1][col-1] == '-'):
                new_board = copy.deepcopy(board)
                tmp_curr_row = list(new_board[row])
                tmp_next_row = list(new_board[row+1])
                tmp_curr_row[col], tmp_next_row[col-1] = tmp_next_row[col-1], tmp_curr_row[col]
                new_board[row] = ''.join(tmp_curr_row)
                new_board[row+1] = ''.join(tmp_next_row)
                possible_move.append(new_board)

        # The given white piece jumps a black piece and capture the black piece.
        if (col == 0): # When the given white piece is at the most left edge of the game board, there is only 1 jump direction.
            if (board[row+1][col] == 'b' and board[row+2][col+1] == '-'):
                new_board = copy.deepcopy(board)
                tmp_curr_row = list(new_board[row])
                tmp_next_row = list(new_board[row+1])
                tmp_next_next_row = list(new_board[row+2])
                tmp_curr_row[col], tmp_next_next_row[col+1] = tmp_next_next_row[col+1], tmp_curr_row[col]
                tmp_next_row[col] = '-'
                new_board[row] = ''.join(tmp_curr_row)
                new_board[row+1] = ''.join(tmp_next_row)
                new_board[row+2] = ''.join(tmp_next_next_row)
                possible_move.append(new_board)

        elif (col == (len(board[row]) - 1)): # When the given white piece is at the most right edge of the game board, there is only one jump direction.
            if (board[row+1][col-1] == 'b' and board[row+2][col-1] == '-'):
                new_board = copy.deepcopy(board)
                tmp_curr_row = list(new_board[row])
                tmp_next_row = list(new_board[row+1])
                tmp_next_next_row = list(new_board[row+2])
                tmp_curr_row[col], tmp_next_next_row[col-1] = tmp_next_next_row[col-1], tmp_curr_row[col]
                tmp_next_row[col-1] = '-'
                new_board[row] = ''.join(tmp_curr_row)
                new_board[row+1] = ''.join(tmp_next_row)
                new_board[row+2] = ''.join(tmp_next_next_row)
                possible_move.append(new_board)

        else : # When the given white piece is at the middle of the row.
            if (board[row+1][col] == 'b' and board[row+2][col+1] == '-'):
                new_board = copy.deepcopy(board)
                tmp_curr_row = list(new_board[row])
                tmp_next_row = list(new_board[row+1])
                tmp_next_next_row = list(new_board[row+2])
                tmp_curr_row[col], tmp_next_next_row[col+1] = tmp_next_next_row[col+1], tmp_curr_row[col]
                tmp_next_row[col] = '-'
                new_board[row] = ''.join(tmp_curr_row)
                new_board[row+1] = ''.join(tmp_next_row)
                new_board[row+2] = ''.join(tmp_next_next_row)
                possible_move.append(new_board)
            if (board[row+1][col-1] == 'b' and board[row+2][col-1] == '-'):
                new_board = copy.deepcopy(board)
                tmp_curr_row = list(new_board[row])
                tmp_next_row = list(new_board[row+1])
                tmp_next_next_row = list(new_board[row+2])
                tmp_curr_row[col], tmp_next_next_row[col-1] = tmp_next_next_row[col-1], tmp_curr_row[col]
                tmp_next_row[col-1] = '-'
                new_board[row] = ''.join(tmp_curr_row)
                new_board[row+1] = ''.join(tmp_next_row)
                new_board[row+2] = ''.join(tmp_next_next_row)
                possible_move.append(new_board)

    # When the given white piece is at the center line or below and not at the two rows from the bottom.
    elif (row_centerLine <= row and row < (len(board) - 2)):
        # The given white piece moves one step downward if possible
        if (board[row+1][col] == '-'): # move left downward
            new_board = copy.deepcopy(board)
            tmp_curr_row = list(new_board[row])
            tmp_next_row = list(new_board[row+1])
            tmp_curr_row[col], tmp_next_row[col] = tmp_next_row[col], tmp_curr_row[col]
            new_board[row] = ''.join(tmp_curr_row)
            new_board[row+1] = ''.join(tmp_next_row)
            possible_move.append(new_board)

        if (board[row+1][col+1] == '-'): # move right downward
            new_board = copy.deepcopy(board)
            tmp_curr_row = list(new_board[row])
            tmp_next_row = list(new_board[row+1])
            tmp_curr_row[col], tmp_next_row[col+1] = tmp_next_row[col+1], tmp_curr_row[col]
            new_board[row] = ''.join(tmp_curr_row)
            new_board[row+1] = ''.join(tmp_next_row)
            possible_move.append(new_board)

        # The given white piece jumps a black piece and capture the piece.
        if (board[row+1][col] == 'b' and board[row+2][col] == '-'):
            new_board = copy.deepcopy(board)
            tmp_curr_row = list(new_board[row])
            tmp_next_row = list(new_board[row+1])
            tmp_next_next_row = list(new_board[row+2])
            tmp_curr_row[col], tmp_next_next_row[col] = tmp_next_next_row[col], tmp_curr_row[col]
            tmp_next_row[col] = '-'
            new_board[row] = ''.join(tmp_curr_row)
            new_board[row+1] = ''.join(tmp_next_row)
            new_board[row+2] = ''.join(tmp_next_next_row)
            possible_move.append(new_board)
        if (board[row+1][col+1] == 'b' and board[row+2][col+2] == '-'):
            new_board = copy.deepcopy(board)
            tmp_curr_row = list(new_board[row])
            tmp_next_row = list(new_board[row+1])
            tmp_next_next_row = list(new_board[row+2])
            tmp_curr_row[col], tmp_next_next_row[col+2] = tmp_next_next_row[col+2], tmp_curr_row[col]
            tmp_next_row[col+1] = '-'
            new_board[row] = ''.join(tmp_curr_row)
            new_board[row+1] = ''.join(tmp_next_row)
            new_board[row+2] = ''.join(tmp_next_next_row)
            possible_move.append(new_board)

    else: # when the given white piece row is at the second row from the bottom, only move actions are possible. (cannot jump)
        # The given white piece moves one step downward if possible
        if (board[row+1][col] == '-'): # move left downward
            new_board = copy.deepcopy(board)
            tmp_curr_row = list(new_board[row])
            tmp_next_row = list(new_board[row+1])
            tmp_curr_row[col], tmp_next_row[col] = tmp_next_row[col], tmp_curr_row[col]
            new_board[row] = ''.join(tmp_curr_row)
            new_board[row+1] = ''.join(tmp_next_row)
            possible_move.append(new_board)

        if (board[row+1][col+1] == '-'): # move right downward
            new_board = copy.deepcopy(board)
            tmp_curr_row = list(new_board[row])
            tmp_next_row = list(new_board[row+1])
            tmp_curr_row[col], tmp_next_row[col+1] = tmp_next_row[col+1], tmp_curr_row[col]
            new_board[row] = ''.join(tmp_curr_row)
            new_board[row+1] = ''.join(tmp_next_row)
            possible_move.append(new_board)

    # print(possible_move) # Need comment out
    return possible_move


"""
This function generates all possible next move of a given black piece.
arguments: game board, row index, column index
return: list of all possible next move of a given white piece
"""
def move_black(board, row, col):
    possible_move = []
    row_centerLine = (len(board) - 1) / 2 # row index of the center line of a game board

    # When the given black piece is at the top row of the game board, there is no possible move.
    if (row == 0):
        return []

    # When the given black piece is at the second row from the top, only move actions are possible. (cannot jump).
    elif (row == 1):
        if (board[row-1][col] == '-'):
            new_board = copy.deepcopy(board)
            tmp_curr_row = list(new_board[row])
            tmp_next_row = list(new_board[row-1])
            tmp_curr_row[col], tmp_next_row[col] = tmp_next_row[col], tmp_curr_row[col]
            new_board[row] = ''.join(tmp_curr_row)
            new_board[row-1] = ''.join(tmp_next_row)
            possible_move.append(new_board)
        if (board[row-1][col+1] == '-'):
            new_board = copy.deepcopy(board)
            tmp_curr_row = list(new_board[row])
            tmp_next_row = list(new_board[row-1])
            tmp_curr_row[col], tmp_next_row[col+1] = tmp_next_row[col+1], tmp_curr_row[col]
            new_board[row] = ''.join(tmp_curr_row)
            new_board[row-1] = ''.join(tmp_next_row)
            possible_move.append(new_board)

    # When the given black piece is at the center line of the game board or above. (exclude top two rows)
    elif (row <= row_centerLine):

        # The given black piece moves one step upward if possible
        if (board[row-1][col] == '-'): # move left direction
            new_board = copy.deepcopy(board)
            tmp_curr_row = list(new_board[row])
            tmp_next_row = list(new_board[row-1])
            tmp_curr_row[col], tmp_next_row[col] = tmp_next_row[col], tmp_curr_row[col]
            new_board[row] = ''.join(tmp_curr_row)
            new_board[row-1] = ''.join(tmp_next_row)
            possible_move.append(new_board)
        if (board[row-1][col+1] == '-'): # move right direction
            new_board = copy.deepcopy(board)
            tmp_curr_row = list(new_board[row])
            tmp_next_row = list(new_board[row-1])
            tmp_curr_row[col], tmp_next_row[col+1] = tmp_next_row[col+1], tmp_curr_row[col]
            new_board[row] = ''.join(tmp_curr_row)
            new_board[row-1] = ''.join(tmp_next_row)
            possible_move.append(new_board)

        # The given black piece jumps a white piece and captures the black piece.
        if (board[row-1][col] == 'w' and board[row-2][col] == '-'):
            new_board = copy.deepcopy(board)
            tmp_curr_row = list(new_board[row])
            tmp_next_row = list(new_board[row-1])
            tmp_next_next_row = list(new_board[row-2])
            tmp_curr_row[col], tmp_next_next_row[col] = tmp_next_next_row[col], tmp_curr_row[col]
            tmp_next_row[col] = '-'
            new_board[row] = ''.join(tmp_curr_row)
            new_board[row-1] = ''.join(tmp_next_row)
            new_board[row-2] = ''.join(tmp_next_next_row)
            possible_move.append(new_board)
        if (board[row-1][col+1] == 'w' and board[row-2][col+2] == '-'):
            new_board = copy.deepcopy(board)
            tmp_curr_row = list(new_board[row])
            tmp_next_row = list(new_board[row-1])
            tmp_next_next_row = list(new_board[row-2])
            tmp_curr_row[col], tmp_next_next_row[col+2] = tmp_next_next_row[col+2], tmp_curr_row[col]
            tmp_next_row[col+1] = '-'
            new_board[row] = ''.join(tmp_curr_row)
            new_board[row-1] = ''.join(tmp_next_row)
            new_board[row-2] = ''.join(tmp_next_next_row)
            possible_move.append(new_board)

    # When the given black piece is at one row below from the center line of the game board.
    elif (row == row_centerLine + 1):
        # The given black piece moves one step upward if possible.
        if (col == 0): # When the given black piece is at the left edge of the game board.
            if (board[row-1][col] == '-'): # right move
                new_board = copy.deepcopy(board)
                tmp_curr_row = list(new_board[row])
                tmp_next_row = list(new_board[row-1])
                tmp_curr_row[col], tmp_next_row[col] = tmp_next_row[col], tmp_curr_row[col]
                new_board[row] = ''.join(tmp_curr_row)
                new_board[row-1] = ''.join(tmp_next_row)
                possible_move.append(new_board)

        elif (col == (len(board[row]) - 1)): # When the given black piece is at the right edge of the game board.
            if (board[row-1][col-1] == '-'): # left move
                new_board = copy.deepcopy(board)
                tmp_curr_row = list(new_board[row])
                tmp_next_row = list(new_board[row-1])
                tmp_curr_row[col], tmp_next_row[col-1] = tmp_next_row[col-1], tmp_curr_row[col]
                new_board[row] = ''.join(tmp_curr_row)
                new_board[row-1] = ''.join(tmp_next_row)
                possible_move.append(new_board)

        else: # When the given black piece is neither at the left edge nor the right edge of the game board.
            if (board[row-1][col] == '-'): # right move
                new_board = copy.deepcopy(board)
                tmp_curr_row = list(new_board[row])
                tmp_next_row = list(new_board[row-1])
                tmp_curr_row[col], tmp_next_row[col] = tmp_next_row[col], tmp_curr_row[col]
                new_board[row] = ''.join(tmp_curr_row)
                new_board[row-1] = ''.join(tmp_next_row)
                possible_move.append(new_board)
            if (board[row-1][col-1] == '-'): # left move
                new_board = copy.deepcopy(board)
                tmp_curr_row = list(new_board[row])
                tmp_next_row = list(new_board[row-1])
                tmp_curr_row[col], tmp_next_row[col-1] = tmp_next_row[col-1], tmp_curr_row[col]
                new_board[row] = ''.join(tmp_curr_row)
                new_board[row-1] = ''.join(tmp_next_row)
                possible_move.append(new_board)

        # The given black piece jumps a white piece and capture the white piece if possible.
        if (col == 0): # When the given black piece is at the left edge of the game board.
            if (board[row-1][col] == 'w' and board[row-2][col+1] == '-'): # right jump
                new_board = copy.deepcopy(board)
                tmp_curr_row = list(new_board[row])
                tmp_next_row = list(new_board[row-1])
                tmp_next_next_row = list(new_board[row-2])
                tmp_curr_row[col], tmp_next_next_row[col+1] = tmp_next_next_row[col+1], tmp_curr_row[col]
                tmp_next_row[col] = '-'
                new_board[row] = ''.join(tmp_curr_row)
                new_board[row-1] = ''.join(tmp_next_row)
                new_board[row-2] = ''.join(tmp_next_next_row)
                possible_move.append(new_board)

        elif (col == (len(board[row]) - 1)): # When the given black piece is at the right edge of the game board.
            if (board[row-1][col-1] == 'w' and board[row-2][col-1] == '-'):
                new_board = copy.deepcopy(board)
                tmp_curr_row = list(new_board[row])
                tmp_next_row = list(new_board[row-1])
                tmp_next_next_row = list(new_board[row-2])
                tmp_curr_row[col], tmp_next_next_row[col-1] = tmp_next_next_row[col-1], tmp_curr_row[col]
                tmp_next_row[col-1] = '-'
                new_board[row] = ''.join(tmp_curr_row)
                new_board[row-1] = ''.join(tmp_next_row)
                new_board[row-2] = ''.join(tmp_next_next_row)
                possible_move.append(new_board)

        else: # When the given black piece is neither at the two most left edges nor at the two right edges of the game board.
            if (board[row-1][col] == 'w' and board[row-2][col+1] == '-'): # right jump
                new_board = copy.deepcopy(board)
                tmp_curr_row = list(new_board[row])
                tmp_next_row = list(new_board[row-1])
                tmp_next_next_row = list(new_board[row-2])
                tmp_curr_row[col], tmp_next_next_row[col+1] = tmp_next_next_row[col+1], tmp_curr_row[col]
                tmp_next_row[col] = '-'
                new_board[row] = ''.join(tmp_curr_row)
                new_board[row-1] = ''.join(tmp_next_row)
                new_board[row-2] = ''.join(tmp_next_next_row)
                possible_move.append(new_board)
            if (board[row-1][col-1] == 'w' and board[row-2][col-1] == '-'):
                new_board = copy.deepcopy(board)
                tmp_curr_row = list(new_board[row])
                tmp_next_row = list(new_board[row-1])
                tmp_next_next_row = list(new_board[row-2])
                tmp_curr_row[col], tmp_next_next_row[col-1] = tmp_next_next_row[col-1], tmp_curr_row[col]
                tmp_next_row[col-1] = '-'
                new_board[row] = ''.join(tmp_curr_row)
                new_board[row-1] = ''.join(tmp_next_row)
                new_board[row-2] = ''.join(tmp_next_next_row)
                possible_move.append(new_board)

    # When the given black piece is at the two or more rows below from center line of the game board.
    else:
        # The given black piece moves one step upward if possible.
        if (col == 0): # When the given black piece is at the left edge of the game board.
            if (board[row-1][col] == '-'): # right move
                new_board = copy.deepcopy(board)
                tmp_curr_row = list(new_board[row])
                tmp_next_row = list(new_board[row-1])
                tmp_curr_row[col], tmp_next_row[col] = tmp_next_row[col], tmp_curr_row[col]
                new_board[row] = ''.join(tmp_curr_row)
                new_board[row-1] = ''.join(tmp_next_row)
                possible_move.append(new_board)

        elif (col == (len(board[row]) - 1)): # When the given black piece is at the right edge of the game board.
            if (board[row-1][col-1] == '-'): # left move
                new_board = copy.deepcopy(board)
                tmp_curr_row = list(new_board[row])
                tmp_next_row = list(new_board[row-1])
                tmp_curr_row[col], tmp_next_row[col - 1] = tmp_next_row[col - 1], tmp_curr_row[col]
                new_board[row] = ''.join(tmp_curr_row)
                new_board[row-1] = ''.join(tmp_next_row)
                possible_move.append(new_board)

        else: # When the given black piece is neither at the left edge nor the right edge of the game board.
            if (board[row-1][col] == '-'): # right move
                new_board = copy.deepcopy(board)
                tmp_curr_row = list(new_board[row])
                tmp_next_row = list(new_board[row-1])
                tmp_curr_row[col], tmp_next_row[col] = tmp_next_row[col], tmp_curr_row[col]
                new_board[row] = ''.join(tmp_curr_row)
                new_board[row-1] = ''.join(tmp_next_row)
                possible_move.append(new_board)
            if (board[row-1][col-1] == '-'): # left move
                new_board = copy.deepcopy(board)
                tmp_curr_row = list(new_board[row])
                tmp_next_row = list(new_board[row-1])
                tmp_curr_row[col], tmp_next_row[col-1] = tmp_next_row[col-1], tmp_curr_row[col]
                new_board[row] = ''.join(tmp_curr_row)
                new_board[row-1] = ''.join(tmp_next_row)
                possible_move.append(new_board)

        # The given black piece jumps a white piece and capture the white piece if possible.
        if (col == 0 or col == 1): # When the given black piece is at either the two most left edge of the game board.
            if (board[row-1][col] == 'w' and board[row-2][col] == '-'):
                new_board = copy.deepcopy(board)
                tmp_curr_row = list(new_board[row])
                tmp_next_row = list(new_board[row-1])
                tmp_next_next_row = list(new_board[row-2])
                tmp_curr_row[col], tmp_next_next_row[col] = tmp_next_next_row[col], tmp_curr_row[col]
                tmp_next_row[col] = '-'
                new_board[row] = ''.join(tmp_curr_row)
                new_board[row-1] = ''.join(tmp_next_row)
                new_board[row-2] = ''.join(tmp_next_next_row)
                possible_move.append(new_board)

        elif (col == (len(board[row]) - 1) or col == (len(board[row]) - 2)): # When the given black piece is at either the two most right edge of the game board.
            if (board[row-1][col-1] == 'w' and board[row-2][col-2] == '-'):
                new_board = copy.deepcopy(board)
                tmp_curr_row = list(new_board[row])
                tmp_next_row = list(new_board[row-1])
                tmp_next_next_row = list(new_board[row-2])
                tmp_curr_row[col], tmp_next_next_row[col-2] = tmp_next_next_row[col-2], tmp_curr_row[col]
                tmp_next_row[col-1] = '-'
                new_board[row] = ''.join(tmp_curr_row)
                new_board[row-1] = ''.join(tmp_next_row)
                new_board[row-2] = ''.join(tmp_next_next_row)
                possible_move.append(new_board)

        else: # When the given black piece is neither at the two most left edges nor at the two right edges of the game board.
            if (board[row-1][col] == 'w' and board[row-2][col] == '-'):
                new_board = copy.deepcopy(board)
                tmp_curr_row = list(new_board[row])
                tmp_next_row = list(new_board[row-1])
                tmp_next_next_row = list(new_board[row-2])
                tmp_curr_row[col], tmp_next_next_row[col] = tmp_next_next_row[col], tmp_curr_row[col]
                tmp_next_row[col] = '-'
                new_board[row] = ''.join(tmp_curr_row)
                new_board[row-1] = ''.join(tmp_next_row)
                new_board[row-2] = ''.join(tmp_next_next_row)
                possible_move.append(new_board)
            if (board[row-1][col-1] == 'w' and board[row-2][col-2] == '-'):
                new_board = copy.deepcopy(board)
                tmp_curr_row = list(new_board[row])
                tmp_next_row = list(new_board[row-1])
                tmp_next_next_row = list(new_board[row-2])
                tmp_curr_row[col], tmp_next_next_row[col-2] = tmp_next_next_row[col-2], tmp_curr_row[col]
                tmp_next_row[col-1] = '-'
                new_board[row] = ''.join(tmp_curr_row)
                new_board[row-1] = ''.join(tmp_next_row)
                new_board[row-2] = ''.join(tmp_next_next_row)
                possible_move.append(new_board)

    return possible_move


"""
This function returns all possible next steps from the given board.
arguments: game board, black's ('b') turn or white's ('w') turn
return: list of all possible next move from the given game board and player turn
"""
def movegen(game_board, player_turn):
    next_states = [] # The list of all possible nest states from a given current state.

    for row in range(len(game_board)):
        for col in range(len(game_board[row])):
            if (game_board[row][col] == 'w' and player_turn == 'w'):
                new_states = move_white(game_board, row, col) # includes duplicate states here
                for state in new_states: # Append only new states not duplicate states
                    if state not in next_states:
                        next_states.append(state)
            elif (game_board[row][col] == 'b' and player_turn == 'b'):
                new_states = move_black(game_board, row, col) # includes duplicate states here
                for state in new_states: # Append only new states not duplicate states
                    if state not in next_states:
                        next_states.append(state)
            else: # When the given row and column is empty, do nothing.
                continue

    return next_states

"""
This function returns the maximum number from the given list.
arguments: list of numbers
return: highest number
"""
def get_max_score(lst):
    res = lst[0]
    for i in lst:
        if res < i:
            res = i
    return res

"""
This function returns the minimum number from the given list.
arguments: list of numbers
return: lowest number
"""
def get_min_score(lst):
    res = lst[0]
    for i in lst:
        if i < res:
            res = i
    return res

"""
This function returns evaluation score of the given game board.
Evaluation score is calculated by the following rules:
if white wins the game --> evaluation score = infinity
if black wins the game --> evaluation score = -infinity
if the game is not over --> evaluation score = (number of opponent's pieces) - (number of player's pieces)

arguments: game board, indicating whose turn ('w' or 'b')
return: evaluation score (explained above)
"""
def static_board_evaluator(board, original_player):
    num_white = 0
    num_black = 0
    num_white_last_row = 0
    num_black_first_row = 0
    max_value = float('inf')
    min_value = -float('inf')

    for row in range(len(board)):
        for col in range(len(board[row])):
            if (board[row][col] == 'w'):
                num_white += 1
                if (row == len(board) - 1): # Check whether a white piece has reached the opponent's side edge.
                    num_white_last_row += 1
            if (board[row][col] == 'b'):
                num_black += 1
                if (row == 0): # Check whether a black piece has reached the opponent's side edge.
                    num_black_first_row += 1

    if (original_player == 'w'):
        if (num_white == num_white_last_row and num_black == num_black_first_row and num_white > 0 and num_black > 0):
            if (num_white > num_black):
                return max_value
            else:
                return min_value

        if (num_black == 0 or num_white == num_white_last_row):
            return max_value
        elif (num_white == 0 or num_black == num_black_first_row):
            return min_value
        else:
            return num_black - num_white

    else:
        if (num_white == num_white_last_row and num_black == num_black_first_row and num_white > 0 and num_black > 0):
            if (num_white > num_black):
                return min_value
            else:
                return max_value

        if (num_white == 0 or num_black == num_black_first_row):
            return max_value
        elif (num_black == 0 or num_white == num_white_last_row):
            return min_value
        else:
            return num_white - num_black


"""
This function is depth first search using minimax algorithm. This is a recursive function.
arguments:
    board: game board
    original_player: indicating whose turn ('w' or 'b')
    curr_player: indicating which player plays in further action
    limit_depth: the limit to explore
    curr_depth: the number of depth currently exploring
return:
    If searching is over, returns the index of the best movement from all possible next movements.
    If searching is NOT over, returns the evaluated score calculated by the function named static_board_evaluator.
"""
def dfs(board, original_player, curr_player, limit_depth, curr_depth):
    all_possible_moves = movegen(board, curr_player)
    if (all_possible_moves == []):
        return static_board_evaluator(board, original_player)

    if (limit_depth == curr_depth): # When the currently exploring depth reached the limit depth.
        score = []
        for state in all_possible_moves:
            score.append(static_board_evaluator(state, original_player)) # Evaluate current board score

        if (curr_depth == 1): # When searching is over, returns the index.
            max_value = score[0]
            res = 0
            for i in range(len(score)):
                if max_value < score[i]:
                    max_value = score[i]
                    res = i
            return res

        else: # When searching is NOT over.
            if (score == []):
                pass
            elif (curr_depth % 2 == 1):
                return get_max_score(score)
            else:
                return get_min_score(score)

    else: # When the currently exploring depth has not reached the limit depth.
        # Need to switch player
        if (curr_player == 'w'):
            curr_player = 'b'
        else:
            curr_player = 'w'

        score = []
        for state in all_possible_moves:
            curr_score = dfs(state, original_player, curr_player, limit_depth, curr_depth + 1)
            score.append(curr_score)

        if (curr_depth == 1): # When searching is over, returns the index.
            max_value = score[0]
            res = 0
            for i in range(len(score)):
                if (max_value < score[i]):
                    max_value = score[i]
                    res = i
            return res

        else: # When searching is NOT over.
            if (score == []):
                pass
            elif (curr_depth % 2 == 1):
                return get_max_score(score)
            else:
                return get_min_score(score)


"""
This function applys minimax algolithm to find the best next move
arguments: game board, indicating whose turn ('w' or 'b'), the limit to explore 
return: the best nest movement of the game board
"""
def minimax(board, original_player, limit_depth):
    curr_depth = 1

    ans_idx = dfs(board, original_player, original_player, limit_depth, curr_depth)
    all_possible_moves = movegen(board, original_player)

    if (all_possible_moves == []): # When the player has no next possible movement. 
        if (movegen(board, 'b' if original_player == 'w' else 'w') == []): # If the opponent player also has no next possible movement.
            return []
        else:
            return board # If the opponent player has (a) next possible movement(s).

    return all_possible_moves[ans_idx]

"""
This function returns true if the game has already done, returns false if not
arguments: game board
return: True or False
"""
def is_game_over(board):
    num_white = 0
    num_black = 0
    num_white_last_row = 0
    num_black_first_row = 0

    for row in range(len(board)):
        for col in range(len(board[row])):
            if (board[row][col] == 'w'):
                num_white += 1
                if (row == len(board) - 1): # Check whether a white piece has reached the opponent's side edge.
                    num_white_last_row += 1
            if (board[row][col] == 'b'):
                num_black += 1
                if (row == 0): # Check whether a black piece has reached the opponent's side edge.
                    num_black_first_row += 1

    if ((num_black == 0) or (num_white == 0)): # When at least one side captures all opponent's pieces.
        return True
    elif ((num_white == num_white_last_row) or (num_black == num_black_first_row)): # When at least all of one color pieces has reached opponent's side 
        return True
    else:
        return False

"""
This function is my top-level function. This returns the best next movement from the given game board.
arguments: game board, black's ('b') turn or white's ('w') turn, how many steps the minimax algorithm goes
return: the list of the best next movement
"""
def oskaplayer(game_board, player_turn, limit_depth):
    flag = is_game_over(game_board)
    if (flag):
        print("The game is already over.")
        return game_board

    ans_board = minimax(game_board, player_turn, limit_depth)

    if(ans_board == []):
        return []

    return ans_board


# ============================== TEST CASES ============================================================
black = 'b'
white = 'w'
board1 = ['www-', '--w', '--', '---', 'bbbb'] # ok
board2 = ['w--w', 'w--', '-w', '-b-', 'b-bb'] # ok
board3 = ['b--b', '---', '-b', '---', '-w--'] # ok
board4 = ['w--w', 'w--', '-w', '-bb', 'b-b-'] # ok
board5 = ['w---', 'www', 'bb', '---', '-b--'] # ok
board6 = ['wwww', '---', '--', '---', 'bbbb'] # ok
board7 = ['bbbb', '---', '--', '---', 'wwww'] # ok
board8 = ['-b--', '--w', '-b', '---', '-w--'] # ok
board9 = ['w-b-', '---', 'w-', 'b--', '--ww'] # ok
board10 = ['b-w-', '---', 'b-', 'w--', '--bb'] #ok

board11 = ['wwwww', '----', '---', '--', '---', '----', 'bbbbb'] # ok
board12 = ['wwwww', '-bb-', '---', '--', '---', '----', 'b--bb'] # ok
board13 = ['-b---', 'wwww', 'bbb', 'w-', '---', '----', '-----'] # ok

board21 = ['wwwwww', '-----', '----', '---', '--', '---', '----', '-----', 'bbbbbb'] # ok
board31 = ['-------', '-bb---', '--w-b', 'w-b-', '--b', '--', '---', '--bw', '--w--', '---w--', '-w-----'] # ok
board41 = ['---------------', '-w--------b---', '-------------', '----w------b', '----w---b--', '------w-b-', '---w-----', '--b-----', '--b----', '--b---', '-----', '-bww', '---', '--', '---', '---w', '----w', '-----b', '------w', '------b-', '--w----w-', '----------', '--w--w-----', '-----b------', '-----b------b', '--b-----------', '---------------'] # ok

# ============================== TEST CASES FROM PIAZZA ============================================================
state1 =  ['w-ww', '---', 'w-', 'b--', 'b-bb']
state2 =  ['-------', '-bb---', '--w-b', 'w-b-', '--b', '--', '---', '--bw', '--w--', '---w--', '-w-----']
state3 =  ['-b---', 'wwww', 'bbb', 'w-', '---', '----', '-----']
state4 =  ['-----', '----', '---', 'b-', 'www', 'bbbb', '-w---']


# ============================== TEST CASES FOR MOVEGEN FUNCTION ============================================================
# print("[white]", movegen(state1, white)) # ok
# print("[black]", movegen(state1, black)) # ok
# print("===============================================================================================")
# print("[white]", movegen(state2, white)) # ok
# print("[black]", movegen(state2, black)) # ok
# print("===============================================================================================")
# print("[white]", movegen(state3, white)) # ok
# print("[black]", movegen(state3, black)) # ok
# print("===============================================================================================")
# print("[white]", movegen(state4, white)) # ok
# print("[black]", movegen(state4, black)) # ok

# print("=== WHITE MOVE ===")
# print(movegen(board1, white))
# print("=== BLACK MOVE ===")
# print(movegen(board1, black))


# ============================== TEST CASES FOR OSKAPLAYER FUNCTION ============================================================
# print("=== WHITE MOVE ===")
# print(oskaplayer(board1, white, 5))
# print("=== BLACK MOVE ===")
# print(oskaplayer(board1, black, 5))
# print("=== WHITE MOVE ===")
# print(oskaplayer(board2, white, 5))
# print("=== BLACK MOVE ===")
# print(oskaplayer(board2, black, 5))
# print("=== WHITE MOVE ===")
# print(oskaplayer(board3, white, 5))
# print("=== BLACK MOVE ===")
# print(oskaplayer(board3, black, 5))
# print("=== WHITE MOVE ===")
# print(oskaplayer(board4, white, 5))
# print("=== BLACK MOVE ===")
# print(oskaplayer(board4, black, 5))
# print("=== WHITE MOVE ===")
# print(oskaplayer(board5, white, 5))
# print("=== BLACK MOVE ===")
# print(oskaplayer(board5, black, 5))
# print("=== WHITE MOVE ===")
# print(oskaplayer(board6, white, 5))
# print("=== BLACK MOVE ===")
# print(oskaplayer(board6, black, 5))
# print("=== WHITE MOVE ===")
# print(oskaplayer(board7, white, 5))
# print("=== BLACK MOVE ===")
# print(oskaplayer(board7, black, 5))
# print("=== WHITE MOVE ===")
# print(oskaplayer(board11, white, 5))
# print("=== BLACK MOVE ===")
# print(oskaplayer(board11, black, 5))
# print("=== WHITE MOVE ===")
# print(oskaplayer(board12, white, 5))
# print("=== BLACK MOVE ===")
# print(oskaplayer(board12, black, 5))
# print("=== WHITE MOVE ===")
# print(oskaplayer(board13, white, 5))
# print("=== BLACK MOVE ===")
# print(oskaplayer(board13, black, 5))
# print("=== WHITE MOVE ===")
# print(oskaplayer(board21, white, 5))
# print("=== BLACK MOVE ===")
# print(oskaplayer(board21, black, 5))
# print("=== WHITE MOVE ===")
# print(oskaplayer(board31, white, 5))
# print("=== BLACK MOVE ===")
# print(oskaplayer(board31, black, 5))
# print("=== WHITE MOVE ===")
# print(oskaplayer(board41, white, 2))
# print("=== BLACK MOVE ===")
# print(oskaplayer(board41, black, 2))

print("=====  Before Move  =====")
print_board(board9)
print("=====  After Move  =====")
print_board(oskaplayer(board9, white, 5))
