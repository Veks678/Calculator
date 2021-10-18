from tkinter import *
import tkinter as tk

from calculation import Calculation_logic

class Rules:
    def __init__(self, widget_label, field_list):
        self.widget_label = widget_label
        self.field_list = field_list
        self.Expression = self.field_list[0]
        self.Decision = self.field_list[1]

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
            self.Decision.delete("1.0",'end-1c')

        elif special_symbol in '←':
            self.Decision.delete('end-2c')

        elif special_symbol in '.':
            if '.' in Decision_str or not Decision_str or Decision_str in '-':
                return
            else:
                self.Decision.insert(END, ".")

    def check_arithmetic(self, arithmetic_symbol, Decision_str):
        if arithmetic_symbol in '-':
            if not Decision_str:
                self.Decision.insert("1.0", '-')
                return
            elif Decision_str[0] in '-' and Decision_str[-1:] in '-':
                return

        if arithmetic_symbol in ('+','*','/','-'):
            if Decision_str[-1:].isdigit() == False:
                return
            if '-' in self.Decision.get("1.0",'end-1c') \
                   and self.Expression.get(1.0, END).isdigit() == False\
                   and Decision_str[-1:].isdigit() == True:
                self.Expression.insert(END, '(' + Decision_str + ')')
                self.Expression.insert(END, ' ' + arithmetic_symbol + ' ')
                self.Decision.delete("1.0",'end-1c')
            else:
                self.Expression.insert(END, Decision_str)
                self.Expression.insert(END, ' ' + arithmetic_symbol + ' ')
                self.Decision.delete("1.0",'end-1c')

    def distribute(self):
        if ([s for s in self.widget_label if s in ('1234567890')]):
            self.check_number(self.widget_label, self.Decision.get("1.0",'end-1c'))

        elif self.widget_label in ('C','←','.'):
            self.check_symbol(self.widget_label, self.Decision.get("1.0",'end-1c'))

        elif self.widget_label in ('+','-','*','/'):
            self.check_arithmetic(self.widget_label,self.Decision.get("1.0",'end-1c'))
            
        elif self.widget_label == '=':
            Calculation_logic(self.Expression, self.Decision).Processing_computation()