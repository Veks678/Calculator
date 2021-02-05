from tkinter import *
import tkinter as tk

from field_constructor import Creating_fields

class Calculation_logic():
    def __init__(self):
        self.Expression = Creating_fields.field_list[0]
        self.Decision = Creating_fields.field_list[1]

    def Input_processing(self):
        self.Expression_str = self.Expression.get("1.0", END)
        self.Expression.insert(END, self.Decision.get())

        self.Expression_str = self.Expression_str.replace(' ', '')
        self.Expression_str = self.Expression_str.replace('(', '')
        self.Expression_str = self.Expression_str.replace(')', '')
        self.Expression_str = self.Expression_str[0:-1]

        long_Expression_str = len(self.Expression_str)

        if long_Expression_str == 0:
            print('\nОшибка! Невозможно вычислить, поле пусто\n')
            return
        if set(["+" , '-', "*" ,"/"]).isdisjoint(self.Expression_str) == True:
            print('\nОшибка! Не найденно арифметическое действие!\n')
            return

        index = []

        while long_Expression_str > 0:
            long_Expression_str = long_Expression_str - 1
            index.insert(0,long_Expression_str)

        Expression_list = [self.Expression_str[i] for i in index]
        print(Expression_list)

        for i, a in enumerate(Expression_list):
            if Expression_list[0] in '-':
                Expression_list.insert(i, (''.join(Expression_list[i: i + 2])))
                del Expression_list[i + 1: i + 3]

            elif Expression_list[i] in '-' \
                 and Expression_list[i - 1] in ('-','+','*','/'):
                Expression_list.insert(i,(''.join(Expression_list[i: i + 2])))
                del Expression_list[i + 1: i + 3]

        Expressions_concatenated = []

        for number in Expression_list.copy():

            index = Expression_list.index(number)

            if number in ("+", "-", "*", "/"):
                Expressions_concatenated.append(''.join(Expression_list[0:index]))
                del Expression_list[0:index]
                Expressions_concatenated.append(Expression_list[0])
                del Expression_list[0]

        Expressions_concatenated.append(''.join(Expression_list[0:]))
        del Expression_list[0]

        return Expressions_concatenated

    def Processing_computation(self):
        self.Expression.insert(END, self.Decision.get())
        self.Expression_str = self.Expression.get("1.0", END)

        Expressions_concatenated = Calculation_logic().Input_processing()

        if len(self.Expression.get("1.0", END)) == 1:
            print('\nОшибка! Арифметическое действие не найдено')
            return
        if self.Expression_str[-1:] in ("+" ,"-" ,"*" ,"/"):
            print('\nОшибка! Не найдено числа после арифметического знака!\n')
            return

        print(Expressions_concatenated)
        for symbol in Expressions_concatenated.copy():
            if symbol in ('+','-','*','/'):
                num1 = ''.join(Expressions_concatenated[0:1])
                num2 = ''.join(Expressions_concatenated[2:3])
                if not set(".").isdisjoint(num1) == True or\
                   not set(".").isdisjoint(num2) == True:
                    if symbol in '+':
                        result = float(num1) + float(num2)
                    elif symbol in '-':
                        result = float(num1) - float(num2)
                    elif symbol in '*':
                        result = float(num1) * float(num2)
                    elif symbol in '/':
                        result = float(num1) / float(num2)
                    result = round(result, 20)
                    result = str(result)
                else:
                    if symbol in '+':
                        result = int(num1) + int(num2)
                    elif symbol in '-':
                        result = int(num1) - int(num2)
                    elif symbol in '*':
                        result = int(num1) * int(num2)
                    elif symbol in '/':
                         result = int(num1) // int(num2)
                    result = str(result)

                del Expressions_concatenated[0:3]
                Expressions_concatenated.insert(0, result)

        self.Decision.delete(0, END)
        self.Decision.insert(END, result)
        self.Expression.delete("1.0", END)
