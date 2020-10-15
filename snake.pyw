from tkinter import *
from random import randint
from time import sleep
from threading import Thread
from math import log
from PIL import Image, ImageTk

class Radiation():
    def __init__(self):
        global canv, food_image, food, rad_list, fr, s2
        ccc = []
        for t in rad_list:
            ccc.append([t.x, t.y])
        self.x = randint(0, 49)
        self.y = randint(self.x == 0, 24)
        while [self.x, self.y] == [food.x, food.y] or [self.x, self.y] in ccc:
            self.x = randint(0, 49)
            self.y = randint(self.x == 0, 24)
        self.fff = canv.create_image(self.x * 20 + 10,
                                  self.y * 20 + 10,
                                  image = rad_image)
    def update(self):
        global s, food, rad_list, fr, s2
        ccc = []
        for t in rad_list:
            ccc.append([t.x, t.y])
        self.x = randint(0, 49)
        self.y = randint(0, 24)
        if fr == 'ON':
          while [self.x, self.y] in s.snake or [self.x, self.y] == [food.x, food.y] or [self.x, self.y] in s2.snake:
            self.x = randint(0, 49)
            self.y = randint(0, 24)
        else:
          while [self.x, self.y] in s.snake or [self.x, self.y] == [food.x, food.y]:
            self.x = randint(0, 49)
            self.y = randint(0, 24)
        canv.delete(self.fff)
        self.fff = canv.create_image(self.x * 20 + 10,
                                  self.y * 20 + 10,
                                  image = rad_image)

class Food():
    def __init__(self):
        global canv, food_image, rad
        self.x = randint(0, 49)
        self.y = randint(self.x == 0, 24)
        self.fff = canv.create_image(self.x * 20 + 10,
                                  self.y * 20 + 10,
                                  image = food_image)
    def update(self):
        global s, rad, s2, fr
        self.x = randint(0, 49)
        self.y = randint(0, 24)
        try:
            rad
        except:
          if fr == 'On':
           while [self.x, self.y] in s.snake or [self.x, self.y] in s2.snake:
            self.x = randint(0, 49)
            self.y = randint(0, 24)
          else:
           while [self.x, self.y] in s.snake:
            self.x = randint(0, 49)
            self.y = randint(0, 24)
        else:
          if fr == 'On':
           while [self.x, self.y] in s.snake or [self.x, self.y] == [rad.x, rad.y] or [self.x, self.y] in s2.snake:
            self.x = randint(0, 49)
            self.y = randint(0, 24)
          else:
           while [self.x, self.y] in s.snake or [self.x, self.y] == [rad.x, rad.y]:
            self.x = randint(0, 49)
            self.y = randint(0, 24)
        canv.delete(self.fff)
        self.fff = canv.create_image(self.x * 20 + 10,
                                  self.y * 20 + 10,
                                  image = food_image)
class Snake():
    def __init__(self, num = 0):
        global canv
        self.cr = True
        self.length = 1
        self.num = num
        self.snag = [canv.create_rectangle(0, 0, 20, 20, fill = 'orange' * num + 'Black' * abs(num - 1))]
        self.snake = [[49 * num, 0]]
        self.direction = self.direction2 = 'l' * num + abs(num - 1) * 'r'
        self.ppp = False
    def update(self):
        global canv, mode, fr, s2, s
        self.direction = self.direction2
        a = self.snag[0]
        canv.delete(a)
        if self.direction == 'r':
            self.snag.append(
                canv.create_rectangle((self.snake[-1][0] + 1) * 20,
                                  self.snake[-1][1] * 20,
                                  (self.snake[-1][0] + 2) * 20,
                                  (self.snake[-1][1] + 1) * 20, fill = 'orange' * self.num + 'Black' * abs(self.num - 1)))
            self.snake.append([self.snake[-1][0] + 1, self.snake[-1][1]])
        elif self.direction == 'l':
            self.snag.append(
                canv.create_rectangle((self.snake[-1][0] - 1) * 20,
                                  self.snake[-1][1] * 20,
                                  (self.snake[-1][0]) * 20,
                                  (self.snake[-1][1] + 1) * 20, fill = 'orange' * self.num + 'Black' * abs(self.num - 1)))
            self.snake.append([self.snake[-1][0] - 1, self.snake[-1][1]])
        elif self.direction == 'u':
            self.snag.append(
                canv.create_rectangle((self.snake[-1][0]) * 20,
                                  (self.snake[-1][1] - 1) * 20,
                                  (self.snake[-1][0] + 1) * 20,
                                  (self.snake[-1][1]) * 20, fill = 'orange' * self.num + 'Black' * abs(self.num - 1)))
            self.snake.append([self.snake[-1][0], self.snake[-1][1] - 1])
        elif self.direction == 'd':
            self.snag.append(
                canv.create_rectangle((self.snake[-1][0]) * 20,
                                  (self.snake[-1][1] + 1) * 20,
                                  (self.snake[-1][0] + 1) * 20,
                                  (self.snake[-1][1] + 2) * 20, fill = 'orange' * self.num + 'Black' * abs(self.num - 1)))
            self.snake.append([self.snake[-1][0], self.snake[-1][1] + 1])
        if not self.ppp:
            self.snag.pop(0)
            self.snake.pop(0)
        self.ppp = False
        if mode == 'BOX':
          if self.snake[-1][0] < 0 or self.snake[-1][0] > 49 or self.snake[-1][1] < 0 or self.snake[-1][1] > 24:
            self.delete()
        else:
            if self.snake[-1][0] < 0:
                self.snake[-1][0] = 49
                canv.coords(self.snag[-1], self.snake[-1][0] * 20,
                            self.snake[-1][1] * 20,
                            self.snake[-1][0] * 20 + 20,
                            self.snake[-1][1] * 20 + 20)
            if self.snake[-1][0] > 49:
                self.snake[-1][0] = 0
                canv.coords(self.snag[-1], self.snake[-1][0] * 20,
                            self.snake[-1][1] * 20,
                            self.snake[-1][0] * 20 + 20,
                            self.snake[-1][1] * 20 + 20)
            if self.snake[-1][1] < 0:
                self.snake[-1][1] = 24
                canv.coords(self.snag[-1], self.snake[-1][0] * 20,
                            self.snake[-1][1] * 20,
                            self.snake[-1][0] * 20 + 20,
                            self.snake[-1][1] * 20 + 20)
            if self.snake[-1][1] > 24:
                self.snake[-1][1] = 0
                canv.coords(self.snag[-1], self.snake[-1][0] * 20,
                            self.snake[-1][1] * 20,
                            self.snake[-1][0] * 20 + 20,
                            self.snake[-1][1] * 20 + 20)
        if fr == "OFF":
          if self.snake.count(self.snake[-1]) > 1:
            self.delete()
        if fr == 'ON':
            if self.num == 0:
                if self.snake[-1] in s2.snake:
                    self.delete()
            else:
                if self.snake[-1] in s.snake:
                    self.delete()
        self.eat()
        self.rad()
    def deg(self):
        global canv, fr
        canv.delete(self.snag[0])
        self.snake.pop(0)
        self.snag.pop(0)
        if len(self.snake) == 0:
            self.delete()
    def rad(self):
        global rad_list
        for t in rad_list:
          if [t.x, t.y] in self.snake:
            self.deg()
            t.update()
    def grow(self):
        self.ppp = True
        self.length += 1
    def eat(self):
        global food
        if [food.x, food.y] in self.snake:
            self.grow()
            food.update()
    def delete(self):
        global canv, fr, wonner
        self.cr = False
        sleep(1)
        if fr == "ON":
            if self.num == 0:wonner = 'Orange'
            else:wonner = 'Black'
        menu()
def lvl_change():
    global lvl, lvl_btn
    if lvl == 10:lvl = 0
    lvl += 1
    lvl_btn['text'] = 'Level: ' + str(lvl)
def change_mode():
    global mode, btn_mode1
    if mode == 'BOX':mode = 'INF'
    else:mode = 'BOX'
    btn_mode1['text'] = 'Mode: ' + mode
def change_rdm():
    global rdm, btn_rad
    if rdm == 'ON':rdm = 'OFF'
    else:rdm = 'ON'
    btn_rad['text'] = 'Rad mode:' + rdm
def frf():
    global fr, fr_btn
    if fr == 'ON':fr = 'OFF'
    else:fr = 'ON'
    fr_btn['text'] = 'Play with friend:' + fr
def menu():
    global canv, btn, s, root, mode, btn_mode1, lvl_btn, lvl, pilImage, image, imagesprite, rdm, btn_rad, lvl, fr
    global fr_btn, wonner
    canv.delete('all')
    imagesprite = canv.create_image(500, 250, image = image)
    #-----------------------------------Кнопка играть с другом--------------------------------------------------
    fr_btn = Button(canv, bg = 'black', fg = 'yellow',
                 command = frf, text = 'Play with friend:' + fr, font = ('aria', 10))
    fr_btn.place(relx = 0.75, rely = 0.80, relheight = 0.1, relwidth = 0.15)
    #-----------------------------------Кнопка уровня-----------------------------------------------------------
    lvl_btn = Button(canv, bg = 'black', fg = 'yellow',
                 command = lvl_change, text = 'Level: ' + str(lvl), font = ('aria', 12))
    lvl_btn.place(relx = 0.75, rely = 0.45, relheight = 0.1, relwidth = 0.15)
    #-----------------------------------Кнопка мода-------------------------------------------------------------
    btn_mode1 = Button(canv, bg = 'black', fg = 'yellow',
                 command = change_mode, text = 'Mode: ' + mode, font = ('aria', 12))
    btn_mode1.place(relx = 0.3, rely = 0.45, relheight = 0.2, relwidth = 0.4)
    #-----------------------------------Кнопка радиации---------------------------------------------------------
    btn_rad = Button(canv, bg = 'black', fg = 'yellow',
                 command = change_rdm, text = 'Rad mode:' + rdm, font = ('aria', 12))
    btn_rad.place(relx = 0.75, rely = 0.625, relheight = 0.1, relwidth = 0.15)
    #-----------------------------------Очки--------------------------------------------------------------------
    if fr == "OFF":
        try:canv.create_text(500, 100,
                         text = "Your result length: " + str(s.length) + ' x' + str(lvl) + ' = ' + str(lvl * s.length) + ' score',
                         font = ('aria', 22), fill = 'blue')
        except:None
    else:
        try:canv.create_text(500, 100,
                         text = wonner + ' won!',
                         font = ('aria', 22), fill = 'blue')
        except:None
    #-----------------------------------Кнопка старта-----------------------------------------------------------
    btn = Button(canv, bg = 'black', fg = 'yellow',
                 command = start, text = 'start', font = ('aria', 26))
    btn.place(relx = 0.3, rely = 0.7, relheight = 0.2, relwidth = 0.4)
    root.mainloop()
def start():
    global s, food, root, btn, btn_mode1, lvl, lvl_btn, pilImage, image, imagesprite, rad_list, rdm, btn_rad, s2
    global fr_btn, fr
    fr_btn.destroy()
    btn_rad.destroy()
    lvl_btn.destroy()
    canv.delete('all')
    btn_mode1.destroy()
    btn.destroy()
    imagesprite = canv.create_image(500, 250, image = image)
    s = Snake()
    if fr == 'ON':s2 = Snake(1)
    food = Food()
    rad_list = []
    if rdm == 'ON':
        for t in range(randint(5, 10)):rad_list.append(Radiation())
    while s.cr:
        s.update()
        if fr == 'ON':s2.update()
        root.update()
        sleep(0.1 / max(1, log(lvl + 1, 2)))
root = Tk()
root.geometry('1000x500')
root.resizable(0, 0)
root.title('Snake by PyPro')

mode = 'BOX'
canv = Canvas(root)

pilImage = Image.open("files/GUI/grass.jpg").resize((1000, 500))
image = ImageTk.PhotoImage(pilImage)

pilImage2 = Image.open("files/GUI/food.webp").resize((20, 20))
food_image = ImageTk.PhotoImage(pilImage2)

pilImage3 = Image.open("files/GUI/radiation.jpg").resize((20, 20))
rad_image = ImageTk.PhotoImage(pilImage3)

canv.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)
def w2(none):
    global s2
    try:
        if s2.direction!='d':s2.direction2 = 'u'
    except:
        None
def a2(none):
    global s2
    try:
        if s2.direction!='r':s2.direction2 = 'l'
    except:
        None
def _s_2(none):
    global s2
    try:
        if s2.direction!='u':s2.direction2 = 'd'
    except:
        None
def d2(none):
    global s2
    try:
        if s2.direction!='l':s2.direction2 = 'r'
    except:
        None
def w(none):
    global s
    try:
        if s.direction!='d':s.direction2 = 'u'
    except:
        None
def a(none):
    global s
    try:
        if s.direction!='r':s.direction2 = 'l'
    except:
        None
def _s_(none):
    global s
    try:
        if s.direction!='u':s.direction2 = 'd'
    except:
        None
def d(none):
    global s
    try:
        if s.direction!='l':s.direction2 = 'r'
    except:
        None
root.bind('w', w2)
root.bind('s', _s_2)
root.bind('a', a2)
root.bind('d', d2)
root.bind('<Up>', w)
root.bind('<Down>', _s_)
root.bind('<Left>', a)
root.bind('<Right>', d)
rdm = "ON"
fr = 'OFF'
lvl = 1
menu()
