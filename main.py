from tkinter import *
import tkinter as tk

from interface_parameters import Param_widgets, Param_window, Param_frames

class main:
    def __init__(self):
        self.__label_widgets_list = ['Expression','Decision','7','8','9',\
                                     '+','4','5','6','-','1','2','3','*',\
                                     '←','0','C','/','=','.']
        self.__list_frames = []
        self.__index_frame = 0

        self.__object_windows = Param_window()

        for label_line in range(7):
            self.__list_frames.append(Param_frames(label_line).call_frame())

        for label_line in range(20):
            Param_widgets(self.__label_widgets_list[label_line], \
                          self.__list_frames[self.__index_frame]\
                          ).call_widgets()

            if label_line in (0,1,5,9,13,17,19):
                self.__index_frame += 1

        self.__object_windows.call_window()

if __name__ == '__main__':
    main()
