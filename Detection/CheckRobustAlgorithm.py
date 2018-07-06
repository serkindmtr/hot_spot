from Generation.TargetsGenerator import target_generator
from Generation.NoiseGenerator import noise_generator
from Generation.PrintFunction import print_matrix
from Detection.RobustAlgorithm import true_robust_algorithm
from Detection.RobustAlgorithm import search_true_target
import random
import numpy as np
import matplotlib.pyplot as plt

gamma = 0.3
h = 1.641504505190876
experiment_iterations = 1000
height = 11
width = 14


def target_creator():
    targets = []
    for i in range(1,10,3):
        for j in range(1,10,3):
            rand = random.randint(1,4)
            if rand == 1:
                targets.append({'x': j + 1, 'y': i + 1})
            if rand == 2:
                targets.append({'x': j + 1.5, 'y': i + 1})
            if rand == 3:
                targets.append({'x': j + 1, 'y': i + 1.5})
            if rand == 4:
                targets.append({'x': j + 1.5, 'y': i + 1.5})

    rand = random.randint(1, 4)
    if rand == 1:
        targets.append({'x': 11, 'y': 2})
    if rand == 2:
        targets.append({'x': 11.5, 'y': 2})
    if rand == 3:
        targets.append({'x': 11, 'y': 2.5})
    if rand == 4:
        targets.append({'x': 11.5, 'y': 2.5})
    return targets


def frame_generator(targets, amplitude):
    result_matrix = np.zeros((height, width))
    for i in range(0,len(targets)):
        target_matrix = target_generator(height, width, targets[i]['x'], targets[i]['y'], gamma, amplitude)
        result_matrix += target_matrix
    noise = noise_generator(height, width)
    result_matrix += noise
    return result_matrix


#main

amplitude_range = [0.5, 0.6, 0.7, 0.8, 0.9, 1.0]

result_amplitude = []
for amplitude_iterator in range(0, len(amplitude_range)):
    experiment_pre_result = []
    for experiment_iterator in range(0, experiment_iterations):
        targets = target_creator()
        matrix = frame_generator(targets,amplitude_range[amplitude_iterator])
        print_matrix(matrix, 'checkRobastFrame', width, height)
        pre_result_targets = true_robust_algorithm(matrix, gamma, h)
        robust_targets = search_true_target(pre_result_targets, gamma)
        result = 0
        for i in range(0,len(targets)):
            for j in range(0, len(robust_targets)):
                if (targets[i]['x'] == robust_targets[j]['x']) and (targets[i]['y'] == robust_targets[j]['y']):
                    result += 1
                    break
        experiment_pre_result.append(result)
    result_amplitude.append(experiment_pre_result)

x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for amplitude_iterator in range(0, len(amplitude_range)):
#     y = np.zeros(11)
#
#     for i in range(0, len(result_amplitude[amplitude_iterator])):
#         for j in range(0, y.size):
#             if result_amplitude[amplitude_iterator][i] >= j:
#                 y[j] +=1
#     graph = plt.plot(x, y)
#     plt.grid(True)
#     plt.title('Amplitude = %f' % (amplitude_range[amplitude_iterator]), fontsize=12)
#     plt.show()

hand = []
for amplitude_iterator in range(0, len(amplitude_range)):
    y = np.zeros(11)

    for i in range(0, len(result_amplitude[amplitude_iterator])):
        for j in range(0, y.size):
            if result_amplitude[amplitude_iterator][i] >= j:
                y[j] +=1
    graph, = plt.plot(x, y,label=('Amplitude = %.2f' % amplitude_range[amplitude_iterator]))
    hand.append(graph)
    print('-----------------------------------------------------------\n')
    print('Amplitude %.2f' % amplitude_range[amplitude_iterator])
    print(x)
    print(y)
plt.grid(True)
plt.legend(handles=hand)
plt.title('Gamma = %f' % gamma, fontsize=12)
plt.show()
