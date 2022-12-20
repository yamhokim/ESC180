'''
 X | O | X
---+---+---
 O | O | X
---+---+---
   | X |
'''

from random import randint

# Problem 1
def print_board_and_legend(board):
    for i in range(3):
        line1 = " " +  board[i][0] + " | " + board[i][1] + " | " +  board[i][2]
        line2 = "  " + str(3*i+1)  + " | " + str(3*i+2)  + " | " +  str(3*i+3)
        print(line1 + " "*5 + line2)
        if i < 2:
            print("---+---+---" + " "*5 + "---+---+---")



def make_empty_board():
    board = []
    for i in range(3):
        board.append([" "]*3)
    return board

# Part a)
def get_list_coord(square_num):
    coord = []
    row_num = (square_num -1) // 3
    column_num = 0
    if square_num % 3 == 0:
        column_num = 2
    elif square_num % 3 == 2:
        column_num = 1
    else:
        column_num = 0
    coord.append(row_num)
    coord.append(column_num)
    return coord

# Part b)
def put_in_board(board, mark, square_num):
    coords = get_list_coord(square_num)
    row = coords[0]
    column = coords[1]
    if board[row][column] == " ":
        board[row][column] = mark
    else:
        print("Can't put a mark there!")
        return None


# Problem 2

# Part a)
def get_free_squares(board): # function appending the wrong coordinates
    free_list = []
    for row in range(3):
        for column in range(3):
            if board[row][column] == ' ':
                free_list.append([row, column])
    return free_list


# Part b)
def get_square_number(row, spot):
    if row == 0 and spot == 0:
        return 1
    elif row == 0 and spot == 1:
        return 2
    elif row == 0 and spot == 2:
        return 3
    elif row == 1 and spot == 0:
        return 4
    elif row == 1 and spot == 1:
        return 5
    elif row == 1 and spot == 2:
        return 6
    elif row == 2 and spot == 0:
        return 7
    elif row == 2 and spot == 1:
        return 8
    elif row == 2 and spot == 2:
        return 9

import random
def make_random_move(board, mark):
    blanks_list = []
    for row in range(3):
        for spot in range(3):
            if board[row][spot] == " ":
                x = get_square_number(row, spot)
                blanks_list.append(x)

    put_in_board(board, mark, random.choice(blanks_list))

# Problem 3

# Part a)
def is_row_all_marks(board, row_i, mark):
    for space in board[row_i]:
        if space != mark:
            return False

    return True

# Part b)
def is_col_all_marks(board, col_i, mark):
    for row in board:
        if row[col_i] != mark:
            return False

    return True

# Part c)
def is_win(board, mark):
    for row in board:
        if row[0] == row[1] == row[2] == mark:
            return True

    for column in range(3):
        if board[0][column] == board[1][column] == board[2][column] == mark:
            return True

    if board[0][0] == board[1][1] == board[2][2] == mark:
        return True

    elif board[0][2] == board[1][1] == board[2][0] == mark:
        return True

    return False

# Question 4
def immediate_win(board, mark):
    temp_board = board
    for row in range(3):
        for space in range(3):
            if temp_board[row][space] == " ":
                temp_board[row][space] = mark
                if is_win(temp_board, mark):
                    board[row][space] = mark
                    return
                else:
                    temp_board[row][space] = " "
    make_random_move(board, mark)





if __name__ == '__main__':
    print(get_list_coord(9))
    board = make_empty_board()
    print_board_and_legend(board)

    print("\n\n")

    put_in_board(board, "X", 7)
    put_in_board(board, "X", 8)
    put_in_board(board, "O", 6)
    put_in_board(board, "O", 9)
    print_board_and_legend(board)
    print(immediate_win(board, "O"))
    print_board_and_legend(board)

