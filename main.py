from tkinter import *
import tkinter as tk

from interface_parameters import Param_widgets, Param_window, Param_frames

class main:
    def __init__(self):
        self.__list_frames = []

        self.__label_widgets_list = ['Expression','Decision','7','8','9',\
                                     '+','4','5','6','-','1','2','3','*',\
                                     '←','0','C','/','=','.']

        self.__object_windows = Param_window()

        for label_line in range(7):
            self.__list_frames.append(Param_frames(label_line).call_frame())

        for widget_label in self.__label_widgets_list:
            self.__object_widgets = Param_widgets(widget_label, \
                                                  self.__list_frames)
            self.__object_widgets.call_widgets()

        self.__object_windows.call_window()

if __name__ == '__main__':
    main()
