from tkinter import *
import tkinter as tk

from .constructor.window_constructor import Window
from .constructor.frame_constructor import Frames
from .constructor.field_constructor  import Creating_fields
from .constructor.button_constructor import Creating_buttons


class Param_widgets:
    def __init__(self, widget_label, index_frame):
        self.__widget_label = widget_label
        self.__index_frame = index_frame

        if self.__widget_label in ('Expression'):
            self.__Object_widgets = Creating_fields(self.__index_frame,\
                                                    "gainsboro", "black",\
                                                    "Arial 10", 27, 1.5,\
                                                    1.5, Text,\
                                                    self.__widget_label)

        elif self.__widget_label in ('Decision'):
            self.__Object_widgets = Creating_fields(self.__index_frame,\
                                                    "gainsboro", "black",\
                                                    "Arial 13", 20, 1.5,\
                                                    1.5, Entry,\
                                                    self.__widget_label)


        elif self.__widget_label not in ('Decision','Expression','=','.'):
            self.__Object_widgets = Creating_buttons(self.__index_frame,\
                                                     "#444", "white",\
                                                     "Arial 14", 55, 1.5,\
                                                     1.5, Button,\
                                                     self.__widget_label)

        elif self.__widget_label in ('=','.'):
            self.__Object_widgets = Creating_buttons(self.__index_frame,\
                                                     "#444", "white",\
                                                     "Arial 14", 189.1, 1.5,
                                                     1.5, Button,\
                                                     self.__widget_label)


    def call_widgets(self):
        self.__Object_widgets.create_widgets()
        self.__Object_widgets.run_widgets()


class Param_window():
    def __init__(self):
        self.__window_object = Window((False, False), 246, \
                                      335, ' Калькулятор')
    def call_window(self):
        self.__window_object.Create_main_window()
        self.__window_object.Running_main_window()

class Param_frames():
    def __init__(self, label_line):
        self.__label_line = label_line

        if self.__label_line == 0:
            self.__height_line = 82
        elif self.__label_line == 1:
            self.__height_line = 29
        else:
            self.__height_line = 45

        self.__param_frames = Frames(Window.root_main, 'royalblue4',\
                                     246, self.__height_line, \
                                     self.__label_line)
    def call_frame(self):
        self.List_frames = self.__param_frames.create_frame()
        self.__param_frames.run_frame()
        return self.List_frames
