from Detection.RobustAlgorithm import robust_algorithm
from Detection.RobustAlgorithm import get_el
from Generation.FrameGenerator import frame_generator
import matplotlib.pyplot as plt
import random
import numpy as np

height = 34
width = 34

gamma = np.zeros(3)
gamma[0] = 0.5
gamma[1] = 1.0
gamma[2] = 3.0

h = np.zeros(3)
h[0] = 1.2841391649390979
h[1] = 1.286974989619119
h[2] = 1.2846477179722848

result = np.empty(3, dtype=dict)

for gamma_iterator in range(0, 3):

    amplitude_range = list()
    amplitude_iterator = 3
    while amplitude_iterator <= 20:
        amplitude_range.append(amplitude_iterator)
        amplitude_iterator += 0.5

    percentage_list = dict()
    for amplitude_iterator in range(0, len(amplitude_range)):
        percentage = 0
        for j in range(0, 10):
            x_target = 9 + (random.randint(0, 32) * 0.5)
            y_target = 9 + (random.randint(0, 32) * 0.5)
            matrix = frame_generator(height,
                                     width,
                                     x_target,
                                     y_target,
                                     gamma[gamma_iterator],
                                     amplitude_range[amplitude_iterator])
            result_matrix = robust_algorithm(matrix, gamma[gamma_iterator], h[gamma_iterator])
            if (result_matrix.count({'x': x_target, 'y': y_target}) > 0):
                percentage += 1
        percentage_list.update({amplitude_range[amplitude_iterator]: percentage})
    result[gamma_iterator] = percentage_list

for i in range(0, 3):
    y = []
    x = []
    amplitude_iterator = 3
    while amplitude_iterator <= 20:
        x.append(amplitude_iterator)
        y.append(result[i][amplitude_iterator])
        amplitude_iterator += 0.5
    print(x)
    print(y)