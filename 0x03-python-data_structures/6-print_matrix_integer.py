#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for num in range(len(matrix)):
        for i in range(len(matrix[num])):
            if i != 0:
                print(" ", end='')
                print("{:d}".format(matrix[num][i]), end='')
                print()
