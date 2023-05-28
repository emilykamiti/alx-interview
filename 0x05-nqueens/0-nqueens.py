#!/usr/bin/python3
"""solve the N queen problem
"""

import sys


def board_set_up(N):
    """Creates a balnk chess board, NxN"""
    matrix = []
    for now in range(N):
        matrix_row = []
        for column in range(N):
            matrix_row.append(0)
        matrix.append(matrix_row)
    return (matrix)


def print_solution(matrix):

    """Prints the coordinates of the queens on the bpard"""
    queens_cordinates = []
    for i, row in enumerate(matrix):
        for j, column in enumerate(row):
            if column == 1:
               queen = []
               queen.append(i)
               queen.append(j)
               queens_coordinates.append(queen)
    print(queens_coordinates)


def is_safe(matrix, new_row, new_column):

    """Checks if a queen can be placed in the given position"""
    # Checks row up to column
    for i in range(new_column):
        if matrix[new_row][i]:
            return False

    # Checks upper diagonal
    for i, j in zip(range(new_row, -1, -1),
                    range(new_column, -1, -1)):
         if matrix[i][j]:
            return False

    N = len(matrix
) 
    #Checks lower diagonal
    for i, j in zip(range(new_row, N, 1),
                     range(new_column, -1, -1)):
         if matrix[i][j]:
            return False

    return True


def solve(matrix, new_column):

    """Solves the N Queen Puzzle recursively"""

    N = len(matrix)

    #All queens are placed
    if new_column >= N:
        print_solution(matrix)
        return matrix

    for new_row in range(N):
        if is_safe(matrix, new_row, new_column):
            matrix[new_row][new_column] = 1
            #Try to recursively solve the rest of the queens
            solve(matrix, new_column + 1)
            #If it can't solve, reset to 0
            matrix[new_row][new_column] = 0
    return None

    if __name__ == "__main__":
        if len(sys.argv) != 2:
           print("Usage: nqueens N")
           sys.exit(1)

        N = sys.argv[1]

        try:
            N = int(N)
        except Exception as e:
            print("N must be a number")
            sys.exit(1)

        if N < 4:
            print("N must be at least 4")
            sys.exit(1)
        matrix = board_set_up(N)
        solve(matrix, 0)
