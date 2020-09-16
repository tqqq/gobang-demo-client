# coding=utf-8

from tkinter import *




class LoginWindow:
    entry_user_name = None
    entry_password = None




    def __init__(self, init_name):
        self.super_window = init_name


    def init_window(self):

        # 窗口
        self.super_window.title("GOBANG LOGIN")
        self.super_window.geometry('1000x800+10+10')  # 窗口宽高，to_up/to_left
        self.super_window['bg'] = '#FFFFFF'  # 背景颜色

        e1 = StringVar()
        e2 = StringVar()
        self.entry_user_name = Entry(self.super_window, textvariable=e1)
        e1.set('user name')
        self.entry_password = Entry(self.super_window, textvariable=e2)
        e2.set('password')
        self.entry_user_name.pack()
        self.entry_password.pack()

        button_login = Button(self.super_window, text='LOGIN', command=self.on_login_click)
        button_login.pack()



    def on_login_click(self):
        pass



