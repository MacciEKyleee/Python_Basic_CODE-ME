import numpy
import numpy as np


def print_board(board):
    for i in board:
        print(" ")
        for x in i:
            print(x, end=" | ")


def player_X(x):
    if x == "A1":
        board[1][1] = "X"
        print_board(board)
    if x == "A2":
        board[1][2] = "X"
        print_board(board)
    if x == "A3":
        board[1][3] = "X"
        print_board(board)
    if x == "B1":
        board[2][1] = "X"
        print_board(board)
    if x == "B2":
        board[2][2] = "X"
        print_board(board)
    if x == "B3":
        board[2][3] = "X"
        print_board(board)
    if x == "C1":
        board[3][1] = "X"
        print_board(board)
    if x == "C2":
        board[3][2] = "X"
        print_board(board)
    if x == "C3":
        board[3][3] = "X"
        print_board(board)
    return board


def player_Y(y):
    if y == "A1":
        board[1][1] = "O"
        print_board(board)
    if y == "A2":
        board[1][2] = "O"
        print_board(board)
    if y == "A3":
        board[1][3] = "O"
        print_board(board)
    if y == "B1":
        board[2][1] = "O"
        print_board(board)
    if y == "B2":
        board[2][2] = "O"
        print_board(board)
    if y == "B3":
        board[2][3] = "O"
        print_board(board)
    if y == "C1":
        board[3][1] = "O"
        print_board(board)
    if y == "C2":
        board[3][2] = "O"
        print_board(board)
    if y == "C3":
        board[3][3] = "O"
        print_board(board)
    return board
def get_uniq_values(row_set):
    result = row_set - {"A","B","C"}
    return result


def cheack_win(board):

    prepared_set = get_uniq_values(set(board))

    for row in prepared_set:
        if len(prepared_set((row))) == 1:
            print("Wygrywający to:", set(row))

        elif len(prepared_set((row))) == 1:
            board_transposed = np.transpose(prepared_set)
            print("Wygrywający to: ", set(row))

    for x in board:
        if (board[1][1] == board[2][2] == board[3][3]) or (board[1][3] == board[2][2] == board[3][1]):
            print("Wygranym jest: ", x)


print("Tic tac toe game ")
print("-------------------------------------------------------")

board = [
     [" ",1 ,2 ,3],
    ["A",".",".","."],
    ["B",".",".","."],
    ["C",".",".","."],


]
print_board(board)




move_counter = 0

while move_counter < 3:
    x = input("\n Player X choose: ")

    player_X(x)

    y = input("\n Player Y choose: ")

    player_Y(y)
    move_counter += 1


cheack_win(board)