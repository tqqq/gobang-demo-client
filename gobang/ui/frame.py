# coding=utf-8

from tkinter import *
from tkinter import messagebox as MessageBox
import time


from gobang.control.login import user_login
from gobang.control.match import join_match_queue, quit_match_queue


class LoginFrame:

    frame = None
    entry_user_name = None
    entry_password = None
    button_login = None


    def __init__(self, super_window):
        self.super_window = super_window
        self.frame = Frame(super_window)
        self.frame.place(x=0, y=0, width=1000, height=800)
        self.init_frame()



    def init_frame(self):

        e1 = StringVar()
        e2 = StringVar()
        self.entry_user_name = Entry(self.frame, textvariable=e1)
        e1.set('user name')
        self.entry_password = Entry(self.frame, textvariable=e2)
        e2.set('password')
        self.entry_user_name.pack()
        self.entry_password.pack()

        self.button_login = Button(self.frame, text='LOGIN', bg='#555555', fg='#000000', command=self.on_button_login_click)
        self.button_login.pack()


    def on_button_login_click(self):
        user_name = self.entry_user_name.get()
        password = self.entry_password.get()
        if len(user_name) < 2 or len(password) < 2:
            MessageBox.showinfo('info', 'User Name or Password too short')
            return

        result = user_login(user_name=user_name, password=password)

        status = result.get('status')
        if not status:
            MessageBox.showinfo('info', result.get('message'))
            return

        user = result.get('user')
        if user:
            IndexFrame(super_window=self.super_window, user=user)
            self.frame.destroy()



class ChessFrame:

    frame = None

    canvas = None
    chessboard = []
    rows = 15  # 行数
    size = 30  # 每一格的大小

    label_player1_name = None
    label_player2_name = None
    label_player1_time = None
    label_player2_time = None

    button_play = None
    button_leave = None

    def __init__(self, super_window):
        self.frame = Frame(super_window)
        self.frame.place(x=0, y=0, width=1000, height=800)
        self.init_frame()

    def init_frame(self):

        self.frame['bg'] = '#FFFFFF'  # 背景颜色

        # 绘制棋盘
        self.canvas = Canvas(self.frame, bg='#EEE8AA', cursor='circle', width=480, height=480, highlightthickness=0)
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
        self.label_player1_name = Label(self.frame, bg='#FFFFFF', justify=LEFT, font='Verdana 10')
        self.label_player2_name = Label(self.frame, bg='#FFFFFF', justify=LEFT, font='Verdana 10')
        self.label_player1_time = Label(self.frame, bg='#FFFFFF', justify=LEFT, font='Verdana 14 bold')
        self.label_player2_time = Label(self.frame, bg='#FFFFFF', justify=LEFT, font='Verdana 14 bold')

        self.label_player1_name.place(x=640, y=40, width=80, height=30)
        self.label_player1_time.place(x=560, y=30, width=40, height=40)
        self.label_player2_name.place(x=640, y=310, width=80, height=30)
        self.label_player2_time.place(x=560, y=300, width=40, height=40)

        # restart button, leave button
        self.button_play = Button(self.frame, bg='#555555', fg='#000000', text='play', command=self.on_button_play_click)
        self.button_leave = Button(self.frame, bg='#555555', fg='#000000', text='leave', command=self.on_button_leave_click)

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


class IndexFrame:

    frame = None
    label_user_name = None
    label_user_info = None
    button_play = None
    button_cancel = None
    label_play_status = None
    user = None

    def __init__(self, super_window, user):
        self.frame = Frame(super_window)
        self.user = user
        self.frame.place(x=0, y=0, width=1000, height=800)
        self.init_frame()
        self.update_user_info()


    def init_frame(self):

        self.label_user_name = Label(self.frame, bg='#FFFFFF', justify=LEFT, font='Verdana 10')
        self.label_user_info = Label(self.frame, bg='#FFFFFF', justify=LEFT, font='Verdana 10')

        self.button_play = Button(self.frame, bg='#555555', fg='#000000', text='play', command=self.on_button_play_click)
        self.button_cancel = Button(self.frame, bg='#555555', fg='#000000', text='cancel', command=self.on_button_cancel_click)
        self.label_play_status = Label(self.frame, bg='#FFFFFF', text='finding match...', justify=LEFT, font='Verdana 10')
        self.label_user_name.pack()
        self.label_user_info.pack()
        self.label_play_status.pack()
        self.button_play.pack()
        self.button_cancel.pack()

        self.button_cancel.pack_forget()
        self.label_play_status.pack_forget()


    def update_user_info(self, user=None):

        if user:
            for k, v in user:
                self.user[k] = v

        user_name = self.user.get('name')
        user_rank = self.user.get('rank')
        if user_name:
            self.label_user_name['text'] = user_name
        if user_rank:
            self.label_user_info['text'] = user_rank


    def on_button_play_click(self):

        result = join_match_queue(user=self.user)

        status = result.get('status')
        if not status:
            MessageBox.showinfo('info', result.get('message'))
            return

        self.button_play.pack_forget()
        self.button_cancel.pack()
        self.label_play_status.pack()


        # loop to get match





    def on_button_cancel_click(self):

        status = False

        while status:

            result = quit_match_queue(user=self.user)

            if result.get('status'):
                status = True

        self.button_cancel.pack_forget()
        self.label_play_status.pack_forget()
        self.button_play.pack()

        print("index quit clicked")


