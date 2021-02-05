from tkinter import *
import tkinter as tk
from frame_constructor import Frames
from field_constructor  import Creating_fields
from button_constructor import Creating_buttons


root = Tk()
root.title(' Калькулятор')
root.geometry('205x335')
root.resizable(width = False, height = False)


class Call_buttons():
    label_widgets_list = ['Expression','Decision','7','8','9','+','4', \
                          '5','6','-','1','2','3','*','←','0','C','/', \
                          '=','.']
    def __init__(self):
        for s in self.label_widgets_list:
            if s in ('Expression'):
                Object_widgets = \
                Creating_fields(Frames.List_frames[0], "gainsboro", \
                                "black", "Arial 10", 22, 2, 1, Text, s\
                                ).create_widgets()

            elif s in ('Decision'):
                param_widgets = \
                Creating_fields(Frames.List_frames[1], "gainsboro", \
                                "black", "Arial 13", 17, 2, 1, Entry, s\
                                ).create_widgets()

            elif s in ('7','8','9','+'):
                param_widgets = \
                Creating_buttons(Frames.List_frames[2], "#444", "white", \
                                 "Arial 14", 3, 1, 1, Button, s\
                                 ).create_widgets()

            elif s in ('4','5','6','-'):
                param_widgets = \
                Creating_buttons(Frames.List_frames[3], "#444", "white", \
                                 "Arial 14", 3, 1, 1, Button, s\
                                 ).create_widgets()

            elif s in ('1','2','3','*'):
                param_widgets = \
                Creating_buttons(Frames.List_frames[4], "#444", "white", \
                                 "Arial 14", 3, 1, 1, Button, s\
                                 ).create_widgets()

            elif s in ('←','0','C','/'):
                param_widgets = \
                Creating_buttons(Frames.List_frames[5], "#444", "white", \
                                 "Arial 14", 3, 1, 1, Button, s\
                                 ).create_widgets()

            elif s in ('=','.'):
                param_widgets = \
                Creating_buttons(Frames.List_frames[6], "#444", "white", \
                                 "Arial 14", 11, 1, 1, Button, s\
                                 ).create_widgets()



param_frames = Frames(root, 'olivedrab', 210)
param_frames.create_frame()

Call_buttons()

root.mainloop()
