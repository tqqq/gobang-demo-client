# coding=utf-8

from tkinter import *


class ChessWindow:

    canvas = None
    chessboard = []
    rows = 15    # 行数
    size = 30    # 每一格的大小

    label_player1_name = None
    label_player2_name = None
    label_player1_time = None
    label_player2_time = None

    button_play = None
    button_leave = None




    def __init__(self, init_name):
        self.super_window = init_name


    def init_chessboard(self):

        # 窗口
        self.super_window.title("GOBANG GAME")
        self.super_window.geometry('1000x800+10+10')  # 窗口宽高，to_up/to_left
        self.super_window['bg'] = '#FFFFFF'  # 背景颜色

        # 绘制棋盘
        self.canvas = Canvas(self.super_window, bg='#EEE8AA', cursor='circle', width=480, height=480, highlightthickness=0)
        self.canvas.place(x=30, y=30)

        # 绑定监听事件
        self.canvas.bind("<Button-1>", self.on_canvas_click)

        for i in range(15):
            x1, y1 = self.calculate_position(0, i)
            x2, y2 = self.calculate_position(self.rows-1, i)
            x3, y3 = self.calculate_position(i, 0)
            x4, y4 = self.calculate_position(i, self.rows-1)
            self.canvas.create_line(x1, y1, x2, y2)
            self.canvas.create_line(x3, y3, x4, y4)

        # play name label
        self.label_player1_name = Label(self.super_window, bg='#FFFFFF', justify=LEFT, font='Verdana 10')
        self.label_player2_name = Label(self.super_window, bg='#FFFFFF', justify=LEFT, font='Verdana 10')
        self.label_player1_time = Label(self.super_window, bg='#FFFFFF', justify=LEFT, font='Verdana 14 bold')
        self.label_player2_time = Label(self.super_window, bg='#FFFFFF', justify=LEFT, font='Verdana 14 bold')

        self.label_player1_name.place(x=640, y=40, width=80, height=30)
        self.label_player1_time.place(x=560, y=30, width=40, height=40)
        self.label_player2_name.place(x=640, y=310, width=80, height=30)
        self.label_player2_time.place(x=560, y=300, width=40, height=40)

        # restart button, leave button
        self.button_play = Button(self.super_window, bg='#555555', fg='#000000', text='play', command=self.on_button_play_click)
        self.button_leave = Button(self.super_window, bg='#555555', fg='#000000', text='leave', command=self.on_button_leave_click)

        self.button_play.place(x=190, y=570, width=60, height=30)
        self.button_leave.place(x=290, y=570, width=60, height=30)

        # 设置为不可见
        self.button_play.place_forget()
        self.button_leave.place_forget()


    def init_user_info(self, match):
        player1_name = match.player1_name
        player2_name = match.player2_name

        self.label_player1_name['text'] = player1_name
        self.label_player2_name['text'] = player2_name


    def calculate_position(self, x, y):
        return x*self.size + self.size, y*self.size + self.size


    def update_left_time(self, player, left_time):
        if player == 1:
            self.label_player1_time['text'] = str(left_time)
        else:
            self.label_player2_time['text'] = str(left_time)


    def update_chessboard(self, player, x, y):
        xc, yc = self.calculate_position(x=x, y=y)
        x1 = xc - self.size/2
        y1 = yc - self.size/2
        x2 = xc + self.size/2
        y2 = yc + self.size/2

        if player == 1:
            self.canvas.create_oval(x1, y1, x2, y2, fill='#000000')
        else:
            self.canvas.create_oval(x1, y1, x2, y2, fill='#FFFFFF')

    #
    # 显示button_leave和 button_play
    #
    def show_leave_button(self):
        self.button_play.place(x=190, y=570, width=60, height=30)
        self.button_leave.place(x=290, y=570, width=60, height=30)


    #
    # 删除button_leave和 button_play
    #
    def remove_leave_button(self):
        self.button_play.place_forget()
        self.button_leave.place_forget()

    def on_button_play_click(self):
        print('123')
        pass


    def on_button_leave_click(self):

        print('456')
        pass

    def on_canvas_click(self, event):
        print(str(event))
        x = event.x
        y = event.y

        delta_x = x % self.size
        delta_y = y % self.size


        if (delta_x + delta_y) < self.size / 2:
            x1 = x - delta_x
            y1 = y - delta_y
        elif (delta_x - delta_y) > self.size / 2:
            x1 = x - delta_x + self.size
            y1 = y - delta_y
        elif (delta_y - delta_x) > self.size / 2:
            x1 = x - delta_x
            y1 = y - delta_y + self.size
        elif (delta_x + delta_y) > 3 * self.size / 2:
            x1 = x - delta_x + self.size
            y1 = y - delta_y + self.size
        else:
            return

        x2 = x1 / self.size - 1
        y2 = y1 / self.size - 1

        if x2 <= 15 and y2 <= 15:
            pass


        print(str(event))
        pass






