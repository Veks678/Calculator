from tkinter import *
import tkinter as tk

import pyperclip
from win32api import LoadKeyboardLayout, GetKeyboardLayout
from pyperclip import paste, copy

class Creating_fields:
    field_list = []

    def __init__(self, windows_line, frame_fields, bg_fields, fg_fields, \
                 font_fields, wight_fields, padx_buttons, pady_buttons, \
                 fields_type, fields_label):
        self.__windows_line = windows_line
        self.__frame_fields = frame_fields
        self.__bg_fields = bg_fields
        self.__fg_fields = fg_fields
        self.__font_fields = font_fields
        self.__wight_fields = wight_fields
        self.__padx_buttons = padx_buttons
        self.__pady_buttons = pady_buttons
        self.__fields_type = fields_type
        self.__fields_label = fields_label

    def create_widgets(self):
        self.__Field = self.__fields_type(self.__frame_fields,
                                        bg = self.__bg_fields,
                                        fg = self.__fg_fields,
                                        font = self.__font_fields,
                                        width = self.__wight_fields)

        self.checking_press()

    def run_widgets(self):
        self.__Field.pack(padx = self.__padx_buttons, \
                          pady = self.__pady_buttons, \
                          side = LEFT, fill = BOTH, expand = True)

        self.updating_widgets()

    def checking_press(self):
        def check_focus(event):
            if GetKeyboardLayout() == 68748313:
                LoadKeyboardLayout("00000409", 1)
            if not self.__windows_line.clipboard_get().isdigit():
                self.__windows_line.clipboard_clear()

        def check_decision(event):
            if (not event.char.isdigit() \
               and event.char not in ('\x08')) \
               and (event.char not in ('\x03', '\x16', '\x18')):
                return 'break'

        def check_expression(event):
            if (not event.char.isdigit() \
               and event.char not in ('\x08')) \
               and (event.char not in ('\x03', '\x16', '\x18')):
                return 'break'

        if self.__fields_label in 'Decision':
            self.__Field.bind("<Key>", check_decision)
            self.__Field.bind("<FocusIn>", check_focus)
            self.__Field.bind("<Leave>", check_focus)
        elif self.__fields_label in 'Expression':
            self.__Field.bind("<Key>", check_expression)
            self.__Field.bind("<FocusIn>", check_focus)
            self.__Field.bind("<Leave>", check_focus)

    def updating_widgets(self):
        if len(self.field_list) > 1:
            del self.field_list[:]
        else:
            self.field_list.append(self.__Field)
