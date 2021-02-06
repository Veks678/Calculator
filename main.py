from tkinter import *
import tkinter as tk

from interface_parameters import Param_widgets, Param_window, Param_frames

class main:
    label_widgets_list = ['Expression','Decision','7','8','9','+','4', \
                          '5','6','-','1','2','3','*','←','0','C','/', \
                          '=','.']
    def __init__(self):
        object_windows = Param_window()

        Param_frames().call_frame()

        for widget_label in self.label_widgets_list:
            object_widgets = Param_widgets(widget_label)
            object_widgets.call_widgets()

        object_windows.call_window()

if __name__ == '__main__':
    main()
