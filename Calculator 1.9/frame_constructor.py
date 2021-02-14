from tkinter import *
import tkinter as tk


class Frames:
    def __init__(self, windows_line, bg_line, width_line, height_line, \
                 label_line):
        self.__windows_line = windows_line
        self.__bg_line = bg_line
        self.__width_line = width_line
        self.__height_line = height_line
        self.__label_line = label_line

    def create_frame(self):
        self.__name_line = Frame(self.__windows_line,
                                 background = self.__bg_line,
                                 width = self.__width_line,
                                 height = self.__height_line)
        return self.__name_line

    def run_frame(self):
        self.__name_line.pack()
        self.__name_line.pack_propagate(False)
