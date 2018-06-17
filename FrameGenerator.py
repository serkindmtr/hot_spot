from PIL import Image, ImageDraw
from NoiseGenerator1 import noise_generator1
from PerlinNoiseGenerator import noise_generator2
from TargetsGenerator import target_generator

noise1 = noise_generator1()
noise2 = noise_generator2()
target = target_generator()

W = 1024
H = 640

img = Image.new("RGB", (W, H), (0, 0, 0))
draw = ImageDraw.Draw(img)

for i in range(0, H - 1):
    for j in range(0, W - 1):
        a = int((noise1[i, j] + target[i, j]) / 2)
        draw.point((j, i), fill=(a, a, a))

img.save("Pictures/frame.png", "png")