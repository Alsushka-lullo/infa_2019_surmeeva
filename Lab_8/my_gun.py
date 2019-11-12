from random import randrange as rnd, choice
import tkinter as tk
import math
import time

root = tk.Tk()
fr = tk.Frame(root)
width_of_canvas = 800
height_of_canvas = 600
height_of_floor = 580
g = 1  # const g = acceleration of ball
root.geometry(str(width_of_canvas) + 'x' + str(height_of_canvas))  # creation of canvas
canv = tk.Canvas(root, bg='white')
canv.pack(fill=tk.BOTH, expand=1)
x_ball = 40  # coordinates of bullet at the beginning
y_ball = 450
lost_of_energy = 0.85


class Ball:
    def __init__(self, root_ball, canvas_ball, x, y, r, vx_gun, vy_gun):
        """ Конструктор класса ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        r - радиус мяча
        vx - начальная скорость по Ох
        vy - начальная скорость по Оу
        """
        self.x = x
        self.y = y
        self.r = r
        self.root = root_ball
        self.canv = canvas_ball
        self.vx = vx_gun
        self.vy = vy_gun
        self.color = choice(['blue', 'green', 'red', 'brown'])
        self.id = canv.create_oval(  # creation of shape
            self.x - self.r,
            self.y - self.r,
            self.x + self.r,
            self.y + self.r,
            fill=self.color
        )
        self.live = 30  # time of living ?

    def get_coords(self):
        return self.canv.coords(self.id)

    def delete_ball(self):
        if self in balls:
            self.canv.delete(self.id)
            balls.remove(self)

    def get_speed(self):
        return self.vx, self.vy  # delete set_coords, move, create moving_ball, get_coords, get_speed, reflection

    def moving_ball(self):  # function for moving
        self.canv.move(self.id, self.vx, self.vy)
        if height_of_floor - self.get_coords()[1] > g:  # changes of velocity
            self.vy += g

    def center_coordinates(self):
        c = self.get_coords()
        return (c[2] + c[0]) / 2, (c[3] + c[1]) / 2

    def reflection_of_the_ball(self):  # cases of reflection
        if width_of_canvas - self.center_coordinates()[0] < self.r or self.center_coordinates()[0] < self.r:
            self.vx = - lost_of_energy * self.vx
        if (height_of_floor - self.center_coordinates()[1] < self.r and self.vy > 0) or self.center_coordinates()[1] \
                < self.r:
            self.vy = - lost_of_energy * self.vy

        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """

    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        return (self.center_coordinates()[0] - obj.center_coords_target()[0]) ** 2 + \
               (self.center_coordinates()[1] - obj.center_coords_target()[1]) ** 2 <= \
               (self.r + obj.get_radius()) ** 2  # узнать, как передовать объект, доставать его кооординаты и радиуc


class Gun:
    def __init__(self, canvas):
        self.f2_power = 10  # начальная мощность, если я правильно поняла
        self.f2_on = False  # говорит, стрелять или нет???
        self.an = 1
        self.x1 = 20
        self.y1 = 450
        self.x2 = 50
        self.y2 = 420
        self.canv = canvas
        self.id = self.canv.create_line(self.x1, self.y1, self.x2, self.y2,
                                        width=7)

    def fire2_start(self, event):
        self.f2_on = True

    def fire2_end(self, event):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls, bullet
        bullet += 1
        self.an = math.atan((event.y - y_ball) / (event.x - x_ball))  # an-угол, под котоорым бросают
        new_ball_vx = self.f2_power * math.cos(self.an)
        new_ball_vy = self.f2_power * math.sin(self.an)
        new_ball = Ball(root, canv, x_ball, y_ball,
                        5, new_ball_vx, new_ball_vy)  # написать что-то про создание мяча, наверное,
        # добивить скорости, координаты,
        balls += [new_ball]
        self.f2_on = False
        self.f2_power = 10

    def targetting(self, event=None):
        """Прицеливание. Зависит от положения мыши."""
        if event is not None:
            self.an = math.atan((event.y - self.y1) / (event.x - self.x1))
        if self.f2_on:
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')
        canv.coords(self.id, self.x1, self.y1,
                    self.x1 + max(self.f2_power, self.x1) * math.cos(self.an),  # change 1 and 2
                    self.y1 + max(self.f2_power, self.x1) * math.sin(self.an)
                    )

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:  # 100-length of gun?
                self.f2_power += 1
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')


class Target:
    def __init__(self, root_of_game, canvas, x, y, r, color):
        self.points = 0
        self.live = 1
        self.canv = canvas
        self.root = root_of_game
        self.r = r
        self.color = color
        self.id_points = self.canv.create_text(30, 30, text=self.points, font='28')
        self.id = self.canv.create_oval(x - r, y - r, x + r, y + r, fill=self.color, width=0)

    def get_radius(self):
        return self.r

    def center_coords_target(self):
        c = self.get_coords_target()
        return (c[2] + c[0]) / 2, (c[3] + c[1]) / 2

    def get_coords_target(self):
        return self.canv.coords(self.id)

    def hit(self, points=1):
        """Попадание шарика в цель."""
        canv.coords(self.id, -10, -10, -10, -10)
        self.points += points
        canv.itemconfig(self.id_points, text=self.points)


t1 = Target(root, canv, rnd(600, 780), rnd(300, 550), rnd(2, 50), 'red')
t1.live = 1
screen1 = canv.create_text(400, 300, text='', font='28')
g1 = Gun(canv)
bullet = 0
balls = []


def new_game(event=''):
    global g1, t1, screen1, balls, bullet
    bullet = 0
    balls = []
    canv.bind('<Button-1>', g1.fire2_start)
    canv.bind('<ButtonRelease-1>', g1.fire2_end)
    canv.bind('<Motion>', g1.targetting)

    time_recovery = 0.03
    t1.live = 1
    while t1.live or balls:
        for b in balls:
            b.reflection_of_the_ball()
            b.moving_ball()
            if b not in balls:
                continue
            if b.hittest(t1) and t1.live:
                t1.live = 0
                t1.hit()
                canv.bind('<Button-1>', '')
                canv.bind('<ButtonRelease-1>', '')
                canv.itemconfig(screen1, text='Вы уничтожили цель за ' + str(bullet) + ' выстрелов')
            root.after(5000, b.delete_ball)
        canv.update()
        time.sleep(time_recovery)
        g1.targetting()
        g1.power_up()
    t1 = Target(root, canv, rnd(600, 780), rnd(300, 550), rnd(2, 50), 'red')  # creation of new target
    canv.itemconfig(screen1, text='')
    canv.delete(g1)

    root.after(750, new_game)


new_game()

root.mainloop()
