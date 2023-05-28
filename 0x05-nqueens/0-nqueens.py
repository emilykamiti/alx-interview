#!/usr/bin/python3
"""
Program that solves the N queen problem
"""

import sys


def is_safe(board, row, col):

    """
       This checks if the queen is safe
    """
    for i in range(row):
        if(
            board[i] == col 
            or board[i][1] - board[i][0] == col - row 
            or board[i][1] + board[i][0]== col + row
         ):

  	    return False
    return True

def solve_nqueens(n, row=0, board=None):
    if board is None:
        board = []

    if row == n:
        print(board)
        return

    for col in range(n):
        if is_safe(board, row, col):
            board.append([row,col])
            solve_nqueens(n, row + 1, board)
            board.pop()

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
        if n < 4:
            print("N must be at least 4")
            sys.exit(1)

        solve_nqueens(n)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
