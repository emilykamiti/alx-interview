#!/usr/bin/python3
"""
Program that solves the N queen problem
"""

import sys
 def is board_set(board, row, col):
    """
       This checks if the queen is safe
    """
    for i in range(row):
        if board[i] == col:
	    return False

    """
       Should there be a queen in the upper left diagonal.
    """
    i, j = row, col
    while i>= 0 and j>=0:
       if board[i] == j:
          return False
       i -= 1
       j -= 1
    """
       should there be a quen in the upper right diagonal
    """
    i, j = row, col
    while i >= 0 and j < len(board):
        if board[i] == j:
            return False
        i -= 1
        j -= 1
    return True

def solve_nqueens(n, row=0, board=[]):
    if row == n:
      print(board)
      return

    for col in range(n):
        if is_safe(board, row, col):
            board.append(col)
            solve_nqueen(n, row + 1, board)
            board.pop()

if __name__ == '__main__':
    if len(sys.argv) ! = 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argve[1])
        if n < 4:
            print("N must be at least 4")
            syst.exit(1)

        solve_nqueen(n)
    except ValueError:
        print("N must be a number)
        sys,exit(1)
