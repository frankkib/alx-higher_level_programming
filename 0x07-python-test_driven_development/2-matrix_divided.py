#!/usr/bin/python3
"""this module is for matrix division"""


def matrix_divided(matrix, div):
    """divides all elements
    Args:
        matrix (int) & (float): list of intergers and floats
        div (int) & float: the divider
    Returns:
        the newly divided matrix
        """
    msg = "matrix must be a matrix (list of lists) of integers/floats"
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(col, int) or isinstance(col, float))
                    for col in [num for row in matrix for num in row])):
        raise TypeError(msg)
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = [
            list(map(lambda x: round(x / div, 2), row))
            for row in matrix]
    return (new_matrix)
