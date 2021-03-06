from PIL import Image
from PIL import ImageDraw
import numpy as np


def normalise_matrix(matrix):
    matrix *= (255.0 / matrix.max())
    return matrix


def print_normalised_matrix(matrix, draw, height, width):
    for i in range(0, height):
        for j in range(0, width):
            a = int(matrix[i, j])
            draw.point((j, i), fill=(a, a, a))


def print_matrix(matrix, picture_name, width, height):
    img = Image.new("RGB", (width, height), (0, 0, 0))
    draw = ImageDraw.Draw(img)

    clone_matrix = matrix.copy()
    normalise_matrix(clone_matrix)
    print_normalised_matrix(clone_matrix, draw, height, width)

    path = 'name.png'
    path = path.replace('name', picture_name)
    img.save(path, 'png')
