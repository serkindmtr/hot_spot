from settings import Height, Width
from PrintFunction import print_matrix
import random
import numpy as np

# TODO реализовать гаусовский нормированный шум https://docs.scipy.org/doc/numpy/reference/generated/numpy.random.normal.html
def noise_generator1():
    matrix = np.zeros((Height, Width))
    for i in range(0, Height):
        for j in range(0, Width):
            a = random.randint(0, 255)
            matrix[i, j] = a
    print_matrix(matrix, 'noise')
    return matrix


noise_generator1()