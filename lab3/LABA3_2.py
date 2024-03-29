from infa_2019_surmeeva.lab3.graph import windowSize, canvasSize
from infa_2019_surmeeva.lab3.graph import penSize, brushColor
from infa_2019_surmeeva.lab3.graph import circle, rectangle
from infa_2019_surmeeva.lab3.graph import changeCoords, run

windowSize(570, 830)
canvasSize(570, 830)
penSize(0)


def ellipse(x1, y1, x2, y2, color):  # drawingColoredEllipses
    brushColor(color)
    _ellipse = circle(10, 10, 10)
    changeCoords(_ellipse, [(x1, y1), (x2, y2)])
    return _ellipse


def rectangle_col(x1, y1, x2, y2, color):  # drawingColoredRectangles
    brushColor(color)
    rectangle(x1, y1, x2, y2)


rectangle_col(0, 0, 570, 525, "#C5C7C9")  # housesAndClouds
rectangle_col(0, 535, 570, 830, "#5F726A")
rectangle_col(13, 20, 127, 548, "#90A6A7")
rectangle_col(150, 46, 268, 559, "#82A68E")
ellipse(-128, 46, 405, 165, "#BCC4BA")
ellipse(-273, 374, 327, 528, "#BCC4BA")
rectangle_col(92, 122, 225, 629, "#C5D0C3")
rectangle_col(428, 19, 558, 554, "#DFE5DC")
rectangle_col(377, 150, 501, 643, "#87A69B")
ellipse(168, -3, 742, 118, "#BCC4BA")
ellipse(120, 210, 696, 343, "#BCC4BA")
ellipse(-192, 697, 592, 1200, "#82A68E")
ellipse(-78, 600, 80, 645, "#BCC4BA")
ellipse(37, 657, 197, 702, "#BCC4BA")
ellipse(41, 710, 198, 758, "#BCC4BA")

ellipse(209, 744, 229, 752, "black")  # drawingCar
rectangle_col(223, 715, 462, 758, "#65C2DD")
rectangle_col(267, 690, 384, 717, "#65C2DD")
rectangle_col(275, 697, 313, 715, "#BCE0F0")
rectangle_col(335, 697, 374, 715, "#BCE0F0")

ellipse(240, 741, 290, 773, "black")
ellipse(403, 741, 453, 773, "black")

run()
