#!/usr/bin/python3
"""
N-Queens Puzzle Solver. 
This program's aim is to solve the N-Queens puzzle,
which mainly involves placing N queen on the NxN chessboard in such a way that no two queens attack each other.
"""

import sys



def initialize_board(N):
    """
    Initializes an empty chessboard of size NxN.
    """
    board = []
    for _ in range(N):
       row = [0] * N
       board.append(row)
    return board


def print_queens_coordinates(board):
    """
    Prints the coordinates of the queens on the dashboard.
    """
    queens_coordinates = []
    for row in range(len(board)):
        for column in range(len(board[row])):
            if board[row][column] == 1:
                queens_coordinates.append((row, column))
    print(queens_coordinates)



def is_safe(board, row, column):

    """
    This checks if placing a queen at a given position is safe.
    """
    N = len(board)


    # Checks the row to the left side of the current column.
    for i in range(column):
        if board[row][i] == 1:
            return False


    # Checks for the upper diagonal.
    for i, j in zip(range(row, -1, -1), range(column, -1, -1)):
        if board[i][j] == 1:
            return False

    # checks for the lower diagonal.
    for i, j in zip(range(row, N, 1), range(column, -1, -1)):
        if board[i][j] == 1:
            return False
    return True



def solve_n_queens(board, column):
    """
    Using backtracking, recursively solves the N-Queen Puzzle.
    """
    N = len(board)

    if column >= N:
        print_queens_coordinates(board)
        return

    for row in range(N):
        if is_safe(board, row, column):
            board[row][column] = 1
            solve_n_queens(board, column + 1)
            board[row][column] = 0
    return None


if __name__ == "__main__":
    if len(sys.argv) !=2:
        print("Usage: nqueens N")
        sys.exit(1)

    N = sys.argv[1]
    try:
        N = int(N)
    except ValueError:
        print("N must be a number\n", end='')
        sys.exit(1)


    if N < 4 :
        print("N must Be atleast 4\n", end='')
        sys.exit(1)


    chessboard = initialize_board(N)
    solve_n_queens(chessboard, 0)
