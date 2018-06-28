from PIL import Image, ImageDraw
from scipy.special import erf
from Detection.PrintTargetFunction import print_matrix
import numpy as np
import math




def get_el(matrix, x_target, y_target, gamma, radius):
    x_target_minus_r = int(math.floor(x_target - radius))
    x_target_plus_r = int(math.ceil(x_target + radius))
    y_target_minus_r = int(math.floor(y_target - radius))
    y_target_plus_r = int(math.ceil(y_target + radius))
    psf_frame = {'x_target_minus_r': x_target_minus_r,
                 'x_target_plus_r': x_target_plus_r,
                 'y_target_minus_r': y_target_minus_r,
                 'y_target_plus_r': y_target_plus_r}
    up_sum = 0
    low_sum = 0

    for i in range(psf_frame['y_target_minus_r'], psf_frame['y_target_plus_r']):
        for j in range(psf_frame['x_target_minus_r'], psf_frame['x_target_plus_r']):
            x = np.array([((j - x_target) / (gamma * math.sqrt(2))), (((j + 1) - x_target) / (gamma * math.sqrt(2)))])
            y = np.array([((i - y_target) / (gamma * math.sqrt(2))), (((i + 1) - y_target) / (gamma * math.sqrt(2)))])
            erf_x = erf(x)
            erf_y = erf(y)
            coefficient = ((erf_x[1] - erf_x[0]) * (erf_y[1] - erf_y[0])) / (8 * (gamma ** 2))
            up_sum += coefficient * matrix[i, j]
            low_sum += coefficient ** 2

    el = up_sum / math.sqrt(low_sum)
    return el


def robust_algorithm(matrix, gamma, h):
    result_matrix = list()
    radius = gamma * 3
    y_range, x_range = matrix.shape
    min_y_range = radius
    min_x_range = radius
    max_y_range = y_range - radius
    max_x_range = x_range - radius
    i = min_y_range
    j = min_x_range
    while i <= max_y_range:
        while j <= max_x_range:
            if ((min_x_range <= j) and (j <= max_x_range) and (min_y_range <= i) and (i <= max_y_range)):
                el = get_el(matrix, j, i, gamma, radius)
                if (el > h):
                    result_matrix.append({'x': j, 'y': i})

            if ((min_x_range <= (j + 0.5)) and ((j + 0.5) <= max_x_range) and (min_y_range <= i) and (i <= max_y_range)):
                el = get_el(matrix, (j + 0.5), i, gamma, radius)
                if (el > h):
                    result_matrix.append({'x': j + 0.5, 'y': i})

            if ((min_x_range <= j) and (j <= max_x_range) and (min_y_range <= (i + 0.5)) and ((i + 0.5) <= max_y_range)):
                el = get_el(matrix, j, (i + 0.5), gamma, radius)
                if (el > h):
                    result_matrix.append({'x': j, 'y': i + 0.5})

            if ((min_x_range <= (j + 0.5)) and ((j + 0.5) <= max_x_range) and (min_y_range <= (i + 0.5)) and ((i + 0.5) <= max_y_range)):
                el = get_el(matrix, (j + 0.5), (i + 0.5), gamma, radius)
                if (el > h):
                    result_matrix.append({'x': j + 0.5, 'y': i + 0.5})
            j += 1
        j = min_x_range
        i += 1
    return result_matrix
