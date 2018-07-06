import numpy as np
import matplotlib.pyplot as plt
from Generation.FrameGenerator import frame_generator
from Detection.RobustAlgorithm import get_el

height = 20
width = 20

h = np.zeros(4)
h[0] = 1.641504505190876
h[1] = 1.6510816387105056
h[2] = 1.6512643595686067
h[3] = 1.6492875966749019

gamma = np.zeros(1)
# gamma[0] = 0.3
# gamma[1] = 0.6
# gamma[2] = 1.0
gamma[0] = 2.0

amplitude = np.zeros(80)
for i in range(amplitude.size):
    amplitude[i] = i + 5

x_target = np.zeros(3)
x_target[0] = 10.5
x_target[1] = 10.5
x_target[2] = 11.0

y_target = np.zeros(3)
y_target[0] = 10.5
y_target[1] = 11.0
y_target[2] = 11.0

result = np.zeros((gamma.size, amplitude.size, x_target.size))

for gamma_iterator in range(gamma.size):
    for amplitude_iterator in range(amplitude.size):
        for target_iterator in range(x_target.size):
            count_results = 0
            for i in range(0, 10000):
                matrix = frame_generator(height,
                                         width,
                                         x_target[target_iterator],
                                         y_target[target_iterator],
                                         gamma[gamma_iterator],
                                         amplitude[amplitude_iterator])
                radius = 3.0 * gamma[gamma_iterator]
                el = get_el(matrix,
                            x_target[target_iterator],
                            y_target[target_iterator],
                            gamma[gamma_iterator],
                            radius)
                if el > h[gamma_iterator]:
                    count_results += 1
            result[gamma_iterator, amplitude_iterator, target_iterator] = count_results

x = []
for amplitude_iterator in range(amplitude.size):
    x.append(amplitude[amplitude_iterator])

for gamma_iterator in range(gamma.size):
    for target_iterator in range(x_target.size):
        y = []
        for amplitude_iterator in range(amplitude.size):
            y.append(result[gamma_iterator, amplitude_iterator, target_iterator])
        print('-----------------------------------------------------------------\n')
        print('Gamma = %f, target:( x = %f , y = %f)\n' % (gamma[gamma_iterator], x_target[target_iterator], y_target[target_iterator]))
        print('Amplitude')
        print(x)
        print('Percentage')
        print(y)
        graph = plt.plot(x, y)
        plt.grid(True)
        plt.title('Gamma = %f, target:( x = %f , y = %f)' % (gamma[gamma_iterator], x_target[target_iterator], y_target[target_iterator]), fontsize=12)
        plt.show()
