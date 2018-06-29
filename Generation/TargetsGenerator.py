import math

import numpy as np
from scipy.special import erf

from Generation.PrintFunction import print_matrix


def detection_psf_frame(x_target, y_target, radius):
    x_target_minus_r = int(math.floor(x_target - radius))
    x_target_plus_r = int(math.ceil(x_target + radius))
    y_target_minus_r = int(math.floor(y_target - radius))
    y_target_plus_r = int(math.ceil(y_target + radius))
    psf_frame = {'x_target_minus_r': x_target_minus_r,
                 'x_target_plus_r': x_target_plus_r,
                 'y_target_minus_r': y_target_minus_r,
                 'y_target_plus_r': y_target_plus_r}
    return psf_frame


def target_generator(height, width, x_target, y_target, gamma, amplitude, print_attribute='no_print'):
    radius = gamma * 3
    matrix = np.zeros((height, width))
    psf_frame = detection_psf_frame(x_target, y_target, radius)
    for i in range(psf_frame['y_target_minus_r'], psf_frame['y_target_plus_r']):
        for j in range(psf_frame['x_target_minus_r'], psf_frame['x_target_plus_r']):
            x = np.array([((j - x_target) / (gamma * math.sqrt(2))), (((j + 1) - x_target) / (gamma * math.sqrt(2)))])
            y = np.array([((i - y_target) / (gamma * math.sqrt(2))), (((i + 1) - y_target) / (gamma * math.sqrt(2)))])
            erf_x = erf(x)
            erf_y = erf(y)
            integral = amplitude * ((erf_x[1] - erf_x[0]) * (erf_y[1] - erf_y[0])) / (8 * (gamma ** 2))
            matrix[i, j] = integral
    if (print_attribute == 'print'):
        print_matrix(matrix, 'target')
    return matrix


# target_generator()
