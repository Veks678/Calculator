from tkinter import *
import tkinter as tk

from field_constructor import Creating_fields

class Buttons_logic():
    def __init__(self, widget_label):
        self.widget_label = widget_label
        self.Expression = Creating_fields.field_list[0]
        self.Decision = Creating_fields.field_list[1]

    def check_number(self, number_symbol, Decision_str):
        if number_symbol in ('0'):
            if not Decision_str or '.' in Decision_str \
               or [s for s in Decision_str[0] if s in ('123456789')] \
               or (Decision_str[0] not in '-'\
                   and Decision_str[-1:] not in '0')\
               or (Decision_str[0] in '-' and len(Decision_str) == 1)\
               or (Decision_str[0] in '-' and Decision_str[1] not in '0' ):
                self.Decision.insert(END, number_symbol)
            else:
                return
        else:
            if not Decision_str or '.' in Decision_str \
               or (Decision_str[0] not in '-' \
                   and Decision_str[0] not in '0')\
               or (Decision_str[0] in '-' and Decision_str[-1] not in '0')\
               or (Decision_str[0] in '-' \
                  and [s for s in Decision_str if s in ('123456789')]):
                self.Decision.insert(END, number_symbol)
            else:
                return

    def check_symbol(self, special_symbol, Decision_str):
        if special_symbol in 'C':
            self.Expression.delete("1.0", END)
            self.Decision.delete(0, END)

        elif special_symbol in '←':
            self.Decision.delete(len(Decision_str)-1)

        elif special_symbol in '.':
            if '.' in Decision_str or not Decision_str\
                                   or Decision_str in '-':
                return
            else:
                self.Decision.insert(END, ".")

    def check_arithmetic(self, arithmetic_symbol, Decision_str):
        if arithmetic_symbol in '-':
            if not Decision_str:
                self.Decision.insert(1, '-')
                return
            elif Decision_str[0] in '-' and Decision_str[-1:] in '-':
                print('\nОшибка! Число не найдено')
                return

        if arithmetic_symbol in ('+','*','/','-'):
            if Decision_str[-1:].isdigit() == False:
                print('\nОшибка! Число не найдено')
                return
            if '-' in self.Decision.get() \
                   and self.Expression.get().isdigit() == False\
                   and Decision_str[-1:].isdigit() == True:
                self.Expression.insert(END, '(' + Decision_str + ')')
                self.Expression.insert(END, ' ' + arithmetic_symbol + ' ')
                self.Decision.delete(0, END)
            else:
                self.Expression.insert(END, Decision_str)
                self.Expression.insert(END, ' ' + arithmetic_symbol + ' ')
                self.Decision.delete(0, END)

    def distribute(self):
        if ([s for s in self.widget_label if s in ('1234567890')]):
            self.check_number(self.widget_label, self.Decision.get())

        elif self.widget_label in ('C','←','.'):
            self.check_symbol(self.widget_label, self.Decision.get())

        elif self.widget_label in ('+','-','*','/'):
            self.check_arithmetic(self.widget_label,self.Decision.get())
