import math
import numpy as np
from Generation.PrintFunction import print_matrix
from settings import Height, Width


def matrix_module(matrix):
    for i in range(0, Height):
        for j in range(0, Width):
            matrix[i, j] = math.fabs(matrix[i, j])
    return matrix


def noise_generator(flag):
    matrix = np.zeros((Height, Width))
    row, col = matrix.shape
    mean = 0
    sigma = 1
    gauss = np.random.normal(mean, sigma, (row, col))
    gauss = gauss.reshape(row, col)
    noise = matrix + gauss
    noise = matrix_module(noise)
    if (flag == 1):
        return noise
    print_matrix(noise, 'noise')
    return noise


noise_generator(0)