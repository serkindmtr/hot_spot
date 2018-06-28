import math
import numpy as np
from Generation.PrintFunction import print_matrix


def matrix_module(height, width, matrix):
    for i in range(0, height):
        for j in range(0, width):
            matrix[i, j] = math.fabs(matrix[i, j])
    return matrix


def noise_generator(height, width, print_attribute='no_print'):
    matrix = np.zeros((height, width))
    row, col = matrix.shape
    mean = 0
    sigma = 1
    gauss = np.random.normal(mean, sigma, (row, col))
    gauss = gauss.reshape(row, col)
    noise = matrix + gauss
    noise = matrix_module(height, width, noise)
    if (print_attribute == 'print'):
        print_matrix(noise, 'noise')
    return noise


# noise_generator('print')