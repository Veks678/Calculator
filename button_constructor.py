from tkinter import *
import tkinter as tk

from widget_logic import Buttons_logic
from field_constructor import Creating_fields
from calculation_logic import Calculation_logic

class Creating_buttons():
    def __init__(self, frame_buttons, bg_buttons, fg_buttons, font_buttons, \
                 width_buttons, padx_buttons, pady_buttons, buttons_type, \
                 buttons_label):
        self.frame_buttons = frame_buttons
        self.bg_buttons = bg_buttons
        self.fg_buttons = fg_buttons
        self.font_buttons = font_buttons
        self.width_buttons = width_buttons
        self.padx_buttons = padx_buttons
        self.pady_buttons = pady_buttons
        self.buttons_type = buttons_type
        self.buttons_label = buttons_label
        self.buttons_side = LEFT

    def create_widgets(self):
        if self.buttons_label.isdigit():
            self.bg_buttons = "#555"
        elif self.buttons_label in '.':
            self.buttons_side = RIGHT
            self.width_buttons = 3
        elif self.buttons_label in '=':
            self.buttons_side = LEFT

        Reusable_button = self.buttons_type(self.frame_buttons,
                                           text = self.buttons_label,
                                           bg = self.bg_buttons, \
                                           fg = self.fg_buttons,
                                           font = self.font_buttons,
                                           width = self.width_buttons,
                       command = Command_buttons(self.buttons_label).Command)

        Reusable_button.pack(side = self.buttons_side , \
                             padx = self.padx_buttons , \
                             pady = self.pady_buttons)



class Command_buttons():
    def __init__(self, buttons_label):
        self.buttons_label = buttons_label

    def Command(self):
        if self.buttons_label not in ('='):
            Buttons_logic(self.buttons_label).distribute()
        else:
            Calculation_logic().Processing_computation()
