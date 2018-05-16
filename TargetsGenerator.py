from PIL import Image, ImageDraw
import math

W = 1920
H = 1080

img = Image.new("RGB", (W, H), (0, 0, 0))
draw = ImageDraw.Draw(img)

x_n = 1000
y_n = 500
sigma = 2.87

for j in range(0, H):
    for i in range(0, W):
        a = random.randint(0, 255)
        draw.point((i, j), fill=(a, a, a))


def my_func(x, y):
    return (1/2 * math.pi * sigma)*(math.exp((-1/(2 * sigma ** 2)) * ((x - x_n)**2 + (y - y_n)**2)))