# coding=utf-8

from tkinter import *

from gobang.ui.frame import LoginFrame, IndexFrame, ChessFrame



class GoBangWindow:


    def __init__(self, super_window):

        self.super_window = super_window

    def init_window(self):

        self.super_window.title("GOBANG GAME")
        self.super_window.geometry('1000x800+10+10')
        login_frame = LoginFrame(self.super_window)







