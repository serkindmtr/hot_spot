from PIL import Image
from PIL import ImageDraw
from settings import Height
from settings import Width

img = Image.new("RGB", (Width, Height), (0, 0, 0))
draw = ImageDraw.Draw(img)


def print_matrix(matrix, picture_name):
    for i in range(0, Height):
        for j in range(0, Width):
            a = int(matrix[i, j])
            draw.point((j, i), fill=(a, a, a))

    path = 'Pictures/name.png'
    path = path.replace('name', picture_name)
    img.save(path, 'png')