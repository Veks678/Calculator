from tkinter import *
import tkinter as tk


class Creating_fields:
    field_list = []

    def __init__(self, frame_fields, bg_fields, fg_fields, font_fields, \
                 wight_fields, padx_buttons, pady_buttons, fields_type, \
                 fields_label):
        self.frame_fields = frame_fields
        self.bg_fields = bg_fields
        self.fg_fields = fg_fields
        self.font_fields = font_fields
        self.wight_fields = wight_fields
        self.padx_buttons = padx_buttons
        self.pady_buttons = pady_buttons
        self.fields_type = fields_type
        self.fields_label = fields_label

    def create_widgets(self):
        def check_keys(event):
            if (event.state & 4 and event.keysym == "v") or \
                event.char.isdigit() == False:
                return "break"

        self.Field = self.fields_type(self.frame_fields, \
                                      bg = self.bg_fields,
                                      fg = self.fg_fields, \
                                      font = self.font_fields, \
                                      width = self.wight_fields)

        self.Field.bind("<Key>", check_keys)

    def run_widgets(self):
        self.Field.pack(padx = self.padx_buttons, \
                        pady = self.pady_buttons, \
                        side = LEFT, fill = Y)

        if len(self.field_list) > 1:
            del self.field_list[:]
        else:
            self.field_list.append(self.Field)
