#!/usr/bin/python3


def rotate_2d_matrix(matrix):
    """
    Rotate a 2D matrix 90 degrees clockwise in-place.

    Args:
        matrix (list[List]): The 2D natrix to rotate
    """
    n = len(matrix) # Save the original size of the matrix
    
    matrix_copy = []
    copy_row = 0
    for column in range(n):
        for row in range(n - 1, -1, -1):

            if column == 0:
                matrix_copy.append([])
            matrix_copy[copy_row].append(matrix[row][column])
        copy_row += 1

   
    for row in range(n): # Copy the rotated elements back to the original matrix.
        for column in range(n):
            matrix[row][column] = matrix_copy[row][column]
