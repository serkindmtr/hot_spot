from settings import Height, Width
import numpy as np
from NoiseGenerator1 import noise_generator1
from PerlinNoiseGenerator import noise_generator2
from TargetsGenerator import target_generator
from PrintFunction import print_matrix

noise1 = noise_generator1()
noise2 = noise_generator2()
target = target_generator()

matrix = np.zeros((Height, Width))

# TODO узнать о приоде шума и по какому принципу он накладывается -- лекции курикши
for i in range(0, Height):
    for j in range(0, Width):
        a = int(max((noise1[i, j], target[i, j])))
        matrix[i, j] = a

print_matrix(matrix, 'frame')