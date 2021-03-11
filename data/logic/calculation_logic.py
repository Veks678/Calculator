from tkinter import *
import tkinter as tk

from ..constructor.field_constructor import Creating_fields

class Calculation_logic:
    def __init__(self):
        self.__Expression = Creating_fields.field_list[0]
        self.__Decision = Creating_fields.field_list[1]

    def __Input_processing(self):
        if (len(self.__Expression.get("1.0", END)) - 1)  == 0:
            print('\nОшибка! Невозможно вычислить, поле пусто\n')
            return None
        elif self.__Expression.get("1.0", END).isdigit():
            print('\nОшибка! Нет арифметического знака!\n')
            return None

        self.__Expression.insert(END, self.__Decision.get())
        self.Expression_str = self.__Expression.get("1.0", END)

        for symbol in self.Expression_str:
            if symbol in (' ', '\n', '(', ')'):
                self.Expression_str = self.Expression_str.replace(symbol,'')

        if self.Expression_str[-1:] in ("+" ,"-" ,"*" ,"/"):
            print('\nОшибка! Нет числа после арифметического знака!\n')
            self.__Expression.delete('end-2c')
            return None

        Expression_list = [self.Expression_str[i] \
                           for i,s in enumerate(self.Expression_str)]

        for i, s in enumerate(Expression_list):
            if (not Expression_list[i-1].isdigit() and s in '-') or\
               Expression_list[0] in '-':
                Expression_list.insert(i, (''.join(Expression_list[i:i+2])))
                del Expression_list[i+1: i+3]

        Expressions_concatenated = []
        for number in Expression_list.copy():
            i = Expression_list.index(number)
            if number in ("+", "-", "*", "/"):
                Expressions_concatenated.append(''.join(Expression_list[0:i]))
                del Expression_list[0:i]
                Expressions_concatenated.append(Expression_list[0])
                del Expression_list[0]

        Expressions_concatenated.append(''.join(Expression_list[0:]))
        del Expression_list[0]

        print(Expressions_concatenated)

        return Expressions_concatenated

    def Processing_computation(self):
        Expressions_concatenated = Calculation_logic().__Input_processing()

        if Expressions_concatenated == None:
            return

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

        self.__Decision.delete(0, END)
        self.__Decision.insert(END, result)
        self.__Expression.delete("1.0", END)
