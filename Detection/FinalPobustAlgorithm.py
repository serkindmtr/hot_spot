import math
import numpy as np

from scipy.special import erf


def true_robust_algorithm(matrix, gamma, h):
    radius = gamma * 3
    y_range, x_range = matrix.shape
    min_y_range = math.ceil(radius)
    min_x_range = math.ceil(radius)
    max_y_range = math.floor(y_range - radius)
    max_x_range = math.floor(x_range - radius)
    i = min_y_range
    j = min_x_range
    target = list()
    while i <= max_y_range:
        while j <= max_x_range:
            if (min_x_range <= j) and (j <= max_x_range) and (min_y_range <= i) and (i <= max_y_range):
                el = get_el(matrix, j, i, gamma, radius)
                if el > h:
                    target.append({'x': j, 'y': i, 'el': el})

            if (min_x_range <= (j + 0.5)) and ((j + 0.5) <= max_x_range) and (min_y_range <= i) and (i <= max_y_range):
                el = get_el(matrix, (j + 0.5), i, gamma, radius)
                if el > h:
                    target.append({'x': j + 0.5, 'y': i, 'el': el})

            if (min_x_range <= j) and (j <= max_x_range) and (min_y_range <= (i + 0.5)) and ((i + 0.5) <= max_y_range):
                el = get_el(matrix, j, (i + 0.5), gamma, radius)
                if el > h:
                    target.append({'x': j, 'y': i + 0.5, 'el': el})

            if (min_x_range <= (j + 0.5)) and ((j + 0.5) <= max_x_range) and (min_y_range <= (i + 0.5)) and ((i + 0.5) <= max_y_range):
                el = get_el(matrix, (j + 0.5), (i + 0.5), gamma, radius)
                if el > h:
                    target.append({'x': j + 0.5, 'y': i + 0.5, 'el': el})
            j += 1
        j = min_x_range
        i += 1
    return target


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


def search_true_target(pre_result_targets, gamma):
    true_target = list()
    radius = gamma * 3
    for pre_result_targets_iterator in range(len(pre_result_targets)):
        el_max = pre_result_targets[pre_result_targets_iterator]['el']
        start_el_max = pre_result_targets[pre_result_targets_iterator]['el']
        for i in range(len(pre_result_targets)):
            if((pre_result_targets[pre_result_targets_iterator]['x'] - radius) <= pre_result_targets[i]['x'])\
                    and ((pre_result_targets[pre_result_targets_iterator]['x'] + radius) >= pre_result_targets[i]['x'])\
                    and ((pre_result_targets[pre_result_targets_iterator]['y'] - radius) <= pre_result_targets[i]['y'])\
                    and ((pre_result_targets[pre_result_targets_iterator]['y'] + radius) >= pre_result_targets[i]['y'])\
                    and (pre_result_targets[i]['el'] > el_max):
                el_max = pre_result_targets[i]['el']
        if start_el_max == el_max:
            true_target.append({'x': pre_result_targets[pre_result_targets_iterator]['x'],
                                'y': pre_result_targets[pre_result_targets_iterator]['y'],
                                'el': pre_result_targets[pre_result_targets_iterator]['el']})
    return true_target