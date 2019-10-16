from math import cos, sin, pi

our_square = [(2, 4), (2, 2), (4, 2), (4, 4)]
phi = pi/4


def rotate_square(square, angle):
    new_square = []
    for i in range(len(square)):
        for j in range(8):
            # поворачивать надо относительно центра, а ты делаешь относительно начала координат
            if j % 2 == 0:
                new_square.append(square[i][0] * cos(angle) + square[i][1] * sin(angle))
            else:
                new_square.append(- square[i][0] * sin(angle) + square[i][1] * cos(angle))
            # попробуй подставить вектор (1,0) и угол pi/4 в эти формулы - он повернется не туда, куда должен бы

    # ты возвращаешь массив координат, а надо массив туплов-координат_точек
    print(new_square)


rotate_square(our_square, phi)

# 3/10 (не решено)
