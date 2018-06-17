from PIL import Image, ImageDraw
from Detection.PrintTargetFunction import print_matrix
import numpy as np
import math

img = Image.open('../Pictures/target.png')
size = img.size
Width = size[0]
Height = size[1]

pixel = img.getpixel((0, 0))

matrix = np.zeros((Height, Width))

result_matrix = np.zeros((Height, Width))

for i in range(0, Height):
    for j in range(0, Width):
        pixel = img.getpixel((j, i))[0]
        matrix[i, j] = pixel / 255

# TODO Разобраться в робастом алгоритме и изменить мапинг цели
for i in range(0, Height - 1):
    for j in range(0, Width - 1):
        if ((matrix[i, j] > 0.05) & (matrix[i, j + 1] > 0.05) & (matrix[i + 1, j] > 0.05) & (
                    matrix[i + 1, j + 1] > 0.05)):
            L1 = int(matrix[i, j])
            L2 = int((matrix[i, j + 1] + (matrix[i, j])) / math.sqrt(2))
            L3 = int((matrix[i + 1, j] + (matrix[i, j])) / math.sqrt(2))
            L4 = int((matrix[i, j] + matrix[i + 1, j] + matrix[i, j + 1] + matrix[i + 1, j + 1]) / 2)
            if (L1 == L2 == L3 == L4):
                result_matrix[i, j] = 255

print_matrix(result_matrix, 'result_target')
