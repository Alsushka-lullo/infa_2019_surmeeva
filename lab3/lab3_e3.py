from math import *
from infa_2019_surmeeva.lab3.graph import *

penSize(2)
canvasSize(1200,800) # основа
penColor(0,255,0)
brushColor(0,245,0)
rectangle(0,400,1200,800)
penColor(200,230,255)
brushColor(200,230,255)
rectangle(0,0,1200,400)


penColor(255,50,200)
brushColor("yellow")  # солнце
verts=[]
t=0
while t<241:
    z_1=pi/120*t
    z_2=pi/8*t
    x=100+50*(1+0.05*sin(z_2))*cos(z_1)
    y=100+50*(1+0.05*sin(z_2))*sin(z_1)
    verts.append((x, y))  
    t+=1
polygon(verts)

penColor(0,0,0)
brushColor(210,200,10) #дом1 
rectangle(150,450,400,600)
brushColor(255,100,100)
polygon([(150,450),(400,450),(275,300),(150,450)])
brushColor(150,150,255)
penColor(255,100,10)
rectangle(165,485,265,550)
penColor(0,0,0)
brushColor("brown")
rectangle(280, 485, 380, 600)
brushColor(210,200,10) #дом2
rectangle(825,460,1000,575)
brushColor(255,100,100)
polygon([(825,460),(1000,460),(912,350),(825,460)])
brushColor(150,150,255)
penColor(255,100,10)
rectangle(830,495,920,545)
brushColor("brown")
rectangle(930, 495, 990, 575)


penColor(0,0,0)
brushColor(255,255,255) # облака
circle(300,150,50)
circle(350,150,50)
circle(410,150,50)
circle(300,130,50)
circle(350,130,50)
circle(410,130,50)
circle(900,200,50)
circle(950,200,50)
circle(1010,200,50)
circle(1010,180,50)
circle(900,180,50)
circle(950,180,50)
circle(660,250,35)
circle(685,250,35)
circle(710,250,35)
circle(660,230,35)
circle(710,230,35)
circle(685,230,35)

penColor(0,0,0) # дерево
brushColor(0,0,0)
rectangle(575,300,600,590)
brushColor(0,90,0)
circle(590,300,45)
circle(530,340,45)
circle(650,340,45)
circle(590,380,45)
circle(540,420,45)
circle(630,420,45)
brushColor(0,0,0)
rectangle(1075,400,1095,570)
brushColor(0,90,0)
circle(1090,360,35)
circle(1125,400,35)
circle(1055,400,35)
circle(1055,400,35)
circle(1090,410,35)
circle(1120,450,35)
circle(1055,450,35)

run()


