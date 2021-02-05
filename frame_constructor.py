from tkinter import *
import tkinter as tk


class Frames():
    List_frames = []

    def __init__(self, windows_line, bg_line, width_line):
        self.windows_line = windows_line
        self.bg_line = bg_line
        self.width_line = width_line

        self.List_name_frames = ['Expression_line', 'Decision_line', \
                                 'First_line', 'Second_line', 'Third_line', \
                                 'Fourth_line', 'Fifth_line']

    def create_frame(self):
        for name_line in self.List_name_frames:
            if name_line in 'Expression_line':
                self.height_line = 82
            elif name_line in 'Decision_line':
                self.height_line = 29
            else:
                self.height_line = 45

            name_line = Frame(self.windows_line, \
                              background = self.bg_line, \
                              width = self.width_line,
                              height = self.height_line)
            self.List_frames.append(name_line)

            for line in self.List_frames:
                line.pack()
                line.pack_propagate(False)
