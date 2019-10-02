from math import sin, cos, pi
from infa_2019_surmeeva.lab3.graph import canvasSize
from infa_2019_surmeeva.lab3.graph import penSize, brushColor, penColor
from infa_2019_surmeeva.lab3.graph import circle, rectangle, polygon
from infa_2019_surmeeva.lab3.graph import run


penSize(2)
canvasSize(1200, 800)  # основа
penColor(0, 255, 0)
brushColor(0, 245, 0)
rectangle(0, 400, 1200, 800)
penColor(200, 230, 255)
brushColor(200, 230, 255)
rectangle(0, 0, 1200, 400)

penColor(0, 0, 0)  # дерево
brushColor(0, 0, 0)
rectangle(880, 320, 900, 500)
brushColor(0, 90, 0)
circle(890, 200, 50)
circle(830, 240, 50)
circle(950, 240, 50)
circle(890, 280, 50)
circle(840, 320, 50)
circle(930, 320, 50)

brushColor(255, 255, 255)  # облако
circle(600, 150, 50)
circle(650, 150, 50)
circle(710, 150, 50)
circle(600, 130, 50)
circle(710, 130, 50)
circle(650, 130, 50)

brushColor(210, 200, 10)  # дом
rectangle(200, 300, 600, 550)
brushColor(255, 100, 100)
polygon([(200, 300), (600, 300), (400, 150), (200, 300)])
brushColor(150, 150, 255)
penColor(255, 100, 10)
rectangle(230, 400, 380, 475)
brushColor("brown")
rectangle(480, 380, 590, 550)

brushColor("yellow")  # sun
verts = []
t = 0
while t < 241:
    z_1 = pi / 120 * t
    z_2 = pi / 8 * t
    x = 1100 + 50 * (1 + 0.05 * sin(z_2)) * cos(z_1)
    y = 100 + 50 * (1 + 0.05 * sin(z_2)) * sin(z_1)
    verts.append((x, y))
    t += 1
polygon(verts)

run()
