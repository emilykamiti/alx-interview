#!/usr/bin/python3

"""
2d matrix rotation

This script rotatets a 2d matrix 90 degrees clockwise.

Example Usage:
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    rotate_2d_matrix(matrix)
    print(matrix)

Author: Kamiti Emily
"""

def rotate_2d_matrix(matrix):
    """
    Rotate a 2d matrix 90 degrees clockwise.

    Args:
       matrix (list): The 2d matrix to be rotated in place.

    Returns:
        None: The function modifies the original matrix in place.

    Raises:
        ValueError: If the input is not a valid 2d matrix.
    """
    if not matrix or not all(len(row) == len(matrix[0]) for row in matrix):
        raise ValueError("Input is not a valid 2D matrix.")

    left, right = 0, len(matrix) - 1

    while left < right:
        for i in range(right - left):
            top, bottom = left, right
            # Save the value of the top left element in a temporary variable 'top_left'
            top_left = matrix[top][left + i]
            # Move the bottom left to the top left position
            matrix[top][left + i] = matrix[bottom - i][left]
            # Move bottom right element to bottom left position
            matrix[bottom - i][left] = matrix[bottom][right - i]
            # Move top right element to the bottom right position
            matrix[bottom][right- i] = matrix[top + i][right]
            # Move top left element to the top right position
            matrix[top + i][right] = top_left

        right -= 1
        left += 1
