from tkinter import *
import tkinter as tk

from window_constructor import Window
from frame_constructor import Frames
from field_constructor  import Creating_fields
from button_constructor import Creating_buttons


class Param_widgets:
    def __init__(self, widget_label):
        self.widget_label = widget_label

        if self.widget_label in ('Expression'):
            self.Object_widgets = Creating_fields(Frames.List_frames[0], \
                                                  "gainsboro", "black", \
                                                  "Arial 10", 27, 1.5, 1.5, \
                                                  Text, self.widget_label)

        elif self.widget_label in ('Decision'):
            self.Object_widgets = Creating_fields(Frames.List_frames[1], \
                                                  "gainsboro", "black", \
                                                  "Arial 13", 20, 1.5, 1.5, \
                                                  Entry, self.widget_label)

        elif self.widget_label in ('7','8','9','+'):
            self.Object_widgets = Creating_buttons(Frames.List_frames[2], \
                                                   "#444", "white", \
                                                   "Arial 14", 55, 1.5, 1.5, \
                                                   Button, self.widget_label)

        elif self.widget_label in ('4','5','6','-'):
            self.Object_widgets = Creating_buttons(Frames.List_frames[3], \
                                                   "#444", "white", \
                                                   "Arial 14", 55, 1.5, 1.5, \
                                                   Button, self.widget_label)

        elif self.widget_label in ('1','2','3','*'):
            self.Object_widgets = Creating_buttons(Frames.List_frames[4], \
                                                   "#444", "white", \
                                                   "Arial 14", 55, 1.5, 1.5, \
                                                   Button, self.widget_label)

        elif self.widget_label in ('←','0','C','/'):
            self.Object_widgets = Creating_buttons(Frames.List_frames[5], \
                                                   "#444", "white", \
                                                   "Arial 14", 55, 1.5, 1.5, \
                                                   Button, self.widget_label)

        elif self.widget_label in ('=','.'):
            self.Object_widgets = Creating_buttons(Frames.List_frames[6], \
                                                   "#444", "white", \
                                                   "Arial 14", 189.1, 1.5, 1.5,\
                                                   Button, self.widget_label)

    def call_widgets(self):
        self.Object_widgets.create_widgets()
        self.Object_widgets.run_widgets()


class Param_window():
    def __init__(self):
        self.window_object = Window((False, False), 246, 335, ' Калькулятор')
    def call_window(self):
        self.window_object.Create_main_window()
        self.window_object.Running_main_window()

class Param_frames():
    def __init__(self):
        self.param_frames = Frames(Window.root_main, 'royalblue4', 246)
    def call_frame(self):
        self.param_frames.create_frame()
        self.param_frames.run_frame()
