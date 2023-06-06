#!/usr/bin/python3


def rotate_2d_matrix(matrix):
    """
    Rotate a @D matrix 90 degrees clockwise in-place.

    Args:
        matrix (list[List]): The 2D natrix to rotate
    """
    n = len(matrix)
    #Transpose the matrix
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] =  matrix[j][i], matrix[i][j]

    for i in range(n):
        matrix[i] = matrix[i][::-1]
if __name__ == "__main__":
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]

    rotate_2d_matrix(matrix)
    print(matrix)
