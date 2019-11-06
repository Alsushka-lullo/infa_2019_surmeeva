import random
import time
from tkinter import *
from random import randrange as rnd, choice

width_of_canvas = 800
height_of_canvas = 600
number_of_balls = 8
colors = ['red', 'orange', 'yellow', 'green', 'blue']

root = Tk()
root.title("Game")
root.geometry(str(width_of_canvas) + 'x' + str(height_of_canvas))
canvas = Canvas(root, bg='white')
canvas.pack(fill=BOTH, expand=1)


class Score:
    def __init__(self, root_score, canvas_score, game_of_players):
        self.sum_points = 0
        self.sum_faults = 0
        self.canvas = canvas_score
        self.game_score = game_of_players
        self.root = root_score
        self.canvas.bind("Button-1", self.click)
        self.root.protocol('WM_DELETE_WINDOW', game_of_players.on_closing)

    def click(self, event):
        for ball in self.game_score.list_of_balls:
            if (event.x - ball.center_coordinates()[0]) ** 2 + \
                    (event.y - ball.center_coordinates()[1]) ** 2 <= ball.get_radius() ** 2:
                self.game_score.list_of_balls.remove(ball)
                ball.kill_the_ball()
                self.sum_points += 1
            else:
                self.sum_faults += 1


class GameWithBalls:
    def __init__(self, g_root, g_canvas):
        self.list_of_balls = []
        self.root = g_root
        self.our_canv = g_canvas
        '''self.root = Tk()
        self.root.title("Game")
        self.root.geometry(str(width_of_canvas) + 'x' + str(hight_of_canvas))
        self.our_canv = Canvas(self.root, bg='white')
        self.our_canv.pack(fill=BOTH, expand=1)'''
        self.score_of_player = Score(root, self.our_canv, self)
        self.time_of_beginning = 0
        self.our_canv.bind('<Button-1>', self.score_of_player.click, self.list_of_balls)

    def start(self):
        self.time_of_beginning = time.perf_counter()
        self.fill_with_random()

    def fill_with_random(self):
        while len(self.list_of_balls) < number_of_balls:
            self.list_of_balls.append(Ball(self.root, self.our_canv,
                                           rnd(100, 700), rnd(100, 500), rnd(30, 50), choice(colors)))
        self.root.after(100, self.fill_with_random)

    def on_closing(self):
        f = open('Score.txt', 'a')
        f.write(str(self.score_of_player.sum_points) + " " + str(self.score_of_player.sum_faults)
                + "\n" + str(self.time_of_beginning) + " " + str(time.perf_counter()) + "\n")
        f.close()
        self.root.destroy()


game = GameWithBalls(root, canvas)

root_names = Toplevel(root)

root_names.title("Name_of_player")
Label(root_names, text="Do you want to remember your score?" + " " + "\n Put your name, if yes.").grid(row=0, column=1,
                                                                                                       columnspan=2,
                                                                                                       sticky=W)
Label(root_names, text="Your name:").grid(row=1, column=0, sticky=W, padx=10, pady=10)
table_name = Entry(root_names)
table_name.grid(row=1, column=1, columnspan=2, sticky=W + E, padx=10)

button_yes = Button(root_names, text="    Yes    ", bg="#f77c7c", command=root_names.destroy)
button_yes.grid(row=2, column=1, sticky=E, padx=10, pady=10)
button_no = Button(root_names, text="    No   ", bg="#f77c7c", command=root_names.destroy)
button_no.grid(row=2, column=2)


def on_closing_name(event):
    global game
    game.start()


def remember_names_of_players(event):
    f = open('Score.txt', 'a')
    f.write(table_name.get() + "\n")
    f.close()


def if_yes(event):
    remember_names_of_players(event)
    on_closing_name(event)


button_yes.bind('<Button-1>', if_yes)
button_no.bind('<Button-1>', on_closing_name)


class Ball:
    def __init__(self, root_ball, canvas_ball, x, y, r, color):
        self.r = r
        self.color = color
        self.root = root_ball
        self.canvas = canvas_ball
        self.shape = self.canvas.create_oval(x - r, y - r, x + r, y + r, fill=choice(colors), width=0)
        self.v_x = rnd(-5, 5)
        self.v_y = rnd(-5, 5)
        self.moving_ball()

    def get_radius(self):
        return self.r

    def center_coordinates(self):
        c = self.get_coordinates()
        return (c[2] + c[0]) / 2, (c[3] + c[1]) / 2

    def get_coordinates(self):
        return self.canvas.coords(self.shape)

    def moving_ball(self):
        self.canvas.move(self.shape, self.v_x, self.v_y)
        coord = self.get_coordinates()
        if not coord:
            return
        if coord[0] > 0 and coord[2] < width_of_canvas and coord[1] > 0 and coord[3] < height_of_canvas:
            self.root.after(100, self.moving_ball)
        else:
            self.reflection_of_the_ball()

    def reflection_of_the_ball(self):
        if width_of_canvas - self.center_coordinates()[0] < self.r or self.center_coordinates()[0] < self.r:
            self.v_x = - self.v_x
        if height_of_canvas - self.center_coordinates()[1] < self.r or self.center_coordinates()[1] < self.r:
            self.v_y = - self.v_y
        self.moving_ball()

    def kill_the_ball(self):
        self.canvas.delete(self.shape)


root.mainloop()
