from PIL import Image, ImageDraw
import random

W = 1920
H = 1080

img = Image.new("RGB", (W, H), (0, 0, 0))
draw = ImageDraw.Draw(img)

for j in range(0, H):
    for i in range(0, W):
        a = random.randint(0, 255)
        draw.point((i, j), fill=(a, a, a))

img.save("/Users/sdima96/Pictures/perlin2d.png","png")
