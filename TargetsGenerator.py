from settings import Height, Width, x_n, y_n, sigma
from PrintFunction import print_matrix
from scipy.special import erf
import numpy as np
import math


def normalize_matrix(matrix, max_element):
    for i in range(0, Height):
        for j in range(0, Width):
            matrix[i, j] = int(round(255 * (matrix[i, j] / max_element)))
    return matrix


def target_generator():
    max_element = 0
    matrix = np.zeros((Height, Width))
    for i in range(0, Height):
        for j in range(0, Width):
            x = np.array([((j - x_n)/(sigma * math.sqrt(2))), (((j + 1) - x_n)/(sigma * math.sqrt(2)))])
            y = np.array([((i - y_n)/(sigma * math.sqrt(2))), (((i + 1) - y_n)/(sigma * math.sqrt(2)))])
            erf_x = erf(x)
            erf_y = erf(y)
            integral = ((erf_x[1] - erf_x[0]) * (erf_y[1] - erf_y[0]))/(8 * sigma)
            if (integral > max_element):
                max_element = integral
            matrix[i, j] = integral
    matrix = normalize_matrix(matrix, max_element)
    print_matrix(matrix, 'target')
    return matrix


target_generator()