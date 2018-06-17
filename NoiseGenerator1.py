from PIL import Image, ImageDraw
import random
import numpy as np

W = 1024
H = 640

img = Image.new("RGB", (W, H), (0, 0, 0))
draw = ImageDraw.Draw(img)


def print_mas(mas):
    for i in range(0, H):
        for j in range(0, W):
            a = int(mas[i, j])
            draw.point((j, i), fill=(a, a, a))
    img.save("Pictures/noise.png", "png")


def noise_generator1():
    mas = np.zeros((H, W))
    for i in range(0, H):
        for j in range(0, W):
            a = random.randint(0, 255)
            mas[i, j] = a
    print_mas(mas)
    return mas


noise_generator1()