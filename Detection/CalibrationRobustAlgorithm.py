from scipy.special import erf
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw
from Detection.PrintTargetFunction import print_matrix
from Generation.NoiseGenerator import noise_generator
import numpy as np
import math


def get_coefficients(matrix, x_target, y_target, gamma, radius):
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
            coefficient = ((erf_x[1] - erf_x[0]) * (erf_y[1] - erf_y[0]))/(8 * (gamma ** 2))
            up_sum += coefficient * matrix[i, j]
            low_sum += coefficient ** 2

    el = up_sum / math.sqrt(low_sum)
    return el


# setting constants

gamma = np.zeros(4)
gamma[0] = 0.3
gamma[1] = 0.6
gamma[2] = 1.0
gamma[3] = 2.0

radius = np.zeros(4)
for radius_iterator in range(radius.size):
    radius[radius_iterator] = gamma[radius_iterator] * 3.0


x_target = np.zeros(3)
y_target = np.zeros(3)
x_target[0] = 10.5
y_target[0] = 10.5
x_target[1] = 10.5
y_target[1] = 11.0
x_target[2] = 11.0
y_target[2] = 11.0

count_iteration = 10 ** 5

mas = np.empty((4, 3), np.ndarray)

h = np.zeros(4)

for gamma_iterator in range(gamma.size):
    h_potential = np.zeros(3)
    for target_iterator in range(0, 3):
        el_mas = np.zeros(count_iteration + 1)

        for experiment_iterator in range(1, count_iteration + 1):
            matrix = noise_generator(20, 20)
            el = get_coefficients(matrix,
                                  x_target[target_iterator],
                                  y_target[target_iterator],
                                  gamma[gamma_iterator],
                                  radius[gamma_iterator])
            el_mas[experiment_iterator] = el

        el_mas.sort(kind='quicksort')
        mas[gamma_iterator, target_iterator] = el_mas
        true_num = int(count_iteration * 0.95)
        h_potential[target_iterator] = el_mas[true_num]
    h[gamma_iterator] = h_potential.max()

file = open('gamma.txt', 'w')
for i in range(0, 4):
    file.write(str(h[i]) + '\n')
file.close()

for i in range(0, 4):
    for j in range(0, 3):
        ax_x = np.arange(1, count_iteration + 2, 1)
        graph = plt.plot(ax_x, mas[i, j])
        plt.grid(True)
        plt.title('Gamma = %f, [x,y] = [%f,%f]' % (gamma[i], x_target[j], y_target[j]), fontsize=12)
        plt.show()
