import math
from graph import*


windowSize(560, 830)                          #general settings
canvasSize(560, 830)
penSize(0)


car = [(33, 699, 60, 705, "black"), (48, 669, 283, 712, "#65C2DD"), 
(90, 644, 208, 670, "#65C2DD"), (101, 648, 136, 669, "#BCE0F0"), 
(157,  648, 192, 669, "#BCE0F0"), (67, 691, 112, 727, "black"), 
(223, 691, 268, 727, "black")]                #example of the 1st car

def changes(scale, x_new, y_new, reflect):    #scaling and reflection of the cars
	l=[]
	for k in range(7): 
		l.append(((car[k][0] - car[0][0]) * scale * reflect + x_new, 
		(car[k][1] - car[0][1]) * scale + y_new,
		(car[k][2] - car[0][0]) * scale * reflect + x_new, 
		(car[k][3] - car[0][1]) * scale + y_new, 
		car[k][4]))
	return l
		
def ellipse(x1, y1, x2, y2, color):           #making colored ellipse
    brushColor(color)
    _ellipse = circle(10, 10, 10)
    changeCoords(_ellipse, [(x1, y1), (x2, y2)])
    return _ellipse



def rectangle_col(x1, y1, x2, y2, color):     #making colored rectangle
    brushColor(color)
    rectangle(x1, y1, x2, y2)
   
   
rectangle_col(0, 0, 570, 525, "black")        #general background
rectangle_col(0, 535, 570, 830, "#5F726A") 

rectangle_col(210, 180, 558, 556, "#C5C7C9")  #backround of the right half
rectangle_col(514, 198, 557, 556, "#90A6A7")
rectangle_col(421, 213, 501, 557, "#82A68E")
ellipse(330, 216, 643, 307, "#BCC4BA")
rectangle_col(449, 265, 537, 608, "#C5D0C3")
rectangle_col(263, 284, 347, 616, "#87A69B")

penColor(255,255, 255)                        #backround of the left half
penSize(6)
rectangle_col(0, 195, 314, 572, "#C5C7C9")
penSize(0)
rectangle_col(0, 210, 9, 281, "#90A6A7")
rectangle_col(23, 228, 102, 575, "#82A68E")
rectangle_col(0, 281, 72, 622, "#C5D0C3")
rectangle_col(209, 210, 296, 572, "#DFE5DC")
rectangle_col(175, 298, 257, 630, "#87A69B")

		
def draw_car(car_arr):                        #drawing of the car
	ellipse(car_arr[0][0], car_arr[0][1], car_arr[0][2], car_arr[0][3], car_arr[0][4])
	for i in range(1, 5):
		rectangle_col(car_arr[i][0], car_arr[i][1], car_arr[i][2], car_arr[i][3], car_arr[i][4])
	ellipse(car_arr[5][0], car_arr[5][1], car_arr[5][2], car_arr[5][3], car_arr[5][4])
	ellipse(car_arr[6][0], car_arr[6][1], car_arr[6][2], car_arr[6][3], car_arr[6][4])
	
draw_car(changes(1, 33, 699, 1))              #coordinates of cars
draw_car(changes(1, 287+250, 744, -1))
draw_car(changes(0.4, 30+100, 622, -1))
draw_car(changes(0.4, 208+100, 629, -1))
draw_car(changes(0.4, 317+100, 623, -1))
draw_car(changes(0.4, 440+100, 641, -1))



run()

