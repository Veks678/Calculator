from tkinter import *
import tkinter as tk

from widget_logic import Buttons_logic
from field_constructor import Creating_fields
from calculation_logic import Calculation_logic

class Creating_buttons:
    Pixel_Virtual = tk.PhotoImage(width = 1)

    def __init__(self, frame_buttons, bg_buttons, fg_buttons, font_buttons, \
                 width_buttons, padx_buttons, pady_buttons, buttons_type, \
                 buttons_label):
        self.__frame_buttons = frame_buttons
        self.__bg_buttons = bg_buttons
        self.__fg_buttons = fg_buttons
        self.__font_buttons = font_buttons
        self.__width_buttons = width_buttons
        self.__padx_buttons = padx_buttons
        self.__pady_buttons = pady_buttons
        self.__buttons_type = buttons_type
        self.__buttons_label = buttons_label
        self.__buttons_side = LEFT

    def create_widgets(self):
        if self.__buttons_label.isdigit():
            self.__bg_buttons = "#555"
        elif self.__buttons_label in '.':
            self.buttons_side = RIGHT
            self.__width_buttons = 36
        elif self.__buttons_label in '=':
            self.buttons_side = LEFT
        elif self.__buttons_label not in ('←','C'):
            self.__width_buttons = 36

        self.__Reusable_button = self.__buttons_type(self.__frame_buttons,
                                                text = self.__buttons_label,
                                                bg = self.__bg_buttons,
                                                fg = self.__fg_buttons,
                                                font = self.__font_buttons,
                                                width = self.__width_buttons,
                                                image = self.Pixel_Virtual,
                                                compound = 'c',
                    command = Command_buttons(self.__buttons_label).Command)


    def run_widgets(self):
        self.__Reusable_button.pack(side = self.__buttons_side , \
                                    padx = self.__padx_buttons , \
                                    pady = self.__pady_buttons, \
                                    expand = True, fill = BOTH)


class Command_buttons:
    def __init__(self, buttons_label):
        self.__buttons_label = buttons_label

    def Command(self):
        if self.__buttons_label not in ('='):
            Buttons_logic(self.__buttons_label).distribute_widgets()
        else:
            Calculation_logic().Processing_computation()
