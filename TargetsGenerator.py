from PIL import Image
from PIL import ImageDraw
from scipy.integrate import quad
from scipy.special import erf
import numpy as np
import math

W = 1024
H = 640

img = Image.new("RGB", (W, H), (0, 0, 0))
draw = ImageDraw.Draw(img)

x_n = 320
y_n = 512
sigma = 10.87


# def my_func(x, y):
#     return (1 / 2 * math.pi * (sigma ** 2)) * (math.exp((-1 / (2 * sigma ** 2)) * ((x - x_n) ** 2 + (y - y_n) ** 2)))
#
#
# for j in range(0, H):
#     for i in range(0, W):
#         integral = dblquad(my_func, i, j + 1, i, i + 1)
#         a = round(100 * integral[0])
#         draw.point((i, j), fill=(a, a, a))
# img.save("/Users/sdima96/Pictures/target.png", "png")

# def my_func1(x):
#     return (1 / 2 * math.pi * (sigma ** 2)) * (math.exp((-1 / (2 * sigma ** 2)) * ((x - x_n) ** 2)))
#
#
# def my_func2(y):
#     return math.exp((-1 / (2 * sigma ** 2)) * ((y - y_n) ** 2))


def normalize_mas(mas, max_element):
    for i in range(0, H):
        for j in range(0, W):
            mas[i, j] = int(round(255 * (mas[i, j] / max_element)))
    return mas


def print_mas(mas):
    for i in range(0, H):
        for j in range(0, W):
            a = int(mas[i, j])
            draw.point((i, j), fill=(a, a, a))
    img.save("Pictures/target.png", "png")


def target_generator():
    max_element = 0
    mas = np.zeros((H, W))
    for i in range(0, H):
        for j in range(0, W):
            # integral1 = quad(my_func2, i, (i + 1))
            # integral2 = quad(my_func1, j, (j + 1))
            x = np.array([((j - x_n)/(sigma * math.sqrt(2))), (((j + 1) - x_n)/(sigma * math.sqrt(2)))])
            y = np.array([((i - y_n)/(sigma * math.sqrt(2))), (((i + 1) - y_n)/(sigma * math.sqrt(2)))])
            erf_x = erf(x)
            erf_y = erf(y)
            integral = ((erf_x[1] - erf_x[0]) * (erf_y[1] - erf_y[0]))/(8 * sigma)
            # integral = integral1[0] * integral2[0]
            # a = round(integral)
            if (integral > max_element):
                max_element = integral
            mas[i, j] = integral
    mas = normalize_mas(mas, max_element)
    print_mas(mas)
    return mas


target_generator()