import matplotlib.pyplot as plt
from PIL import Image, ImageDraw
from Detection.PrintTargetFunction import print_matrix
from Generation.NoiseGenerator import noise_generator
import numpy as np
import math

# count_iteration = 10 ** 5
#
# def matrix_module(matrix, Height, Width):
#     for i in range(0, Height):
#         for j in range(0, Width):
#             matrix[i, j] = int(math.fabs(matrix[i, j]))
#     return matrix


def get_matrix():
    matrix = noise_generator(1)

    return matrix


get_matrix()