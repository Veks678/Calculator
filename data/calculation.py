from tkinter import *
import tkinter as tk

class Calculation_logic:
    def __init__(self, Expression, Decision):
        self.Expression, self.Decision = Expression, Decision

    def Input_processing(self):
        if (len(self.Expression.get("1.0", 'end-1c'))) == 0:
            return None
        elif self.Expression.get("1.0", 'end-1c').isdigit():
            return None

        self.Expression.insert(END, self.Decision.get("1.0",'end-1c'))
        self.Expression_str = self.Expression.get("1.0", END)

        for symbol in self.Expression_str:
            if symbol in (' ', '\n', '(', ')'):
                self.Expression_str = self.Expression_str.replace(symbol,'')

        if self.Expression_str[-1:] in ("+" ,"-" ,"*" ,"/"):
            self.Expression.delete('end-2c')
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

        return Expressions_concatenated

    def Processing_computation(self):
        Expression = self.Input_processing()

        if Expression == None:
            return

        for symbol in Expression.copy():
            if symbol in ('+','-','*','/'):
                num1, num2 = ''.join(Expression[0:1]), ''.join(Expression[2:3])
                if not set(".").isdisjoint(num1) == True or\
                   not set(".").isdisjoint(num2) == True:
                    result = str(round(float(eval(f'{num1} {symbol} {num2}')),20))
                else:
                    result = str(eval(f'{num1} {symbol} {num2}'))

                del Expression[0:3]
                Expression.insert(0, result)

        self.Decision.delete("1.0",'end-1c')
        self.Decision.insert(END, result)
        self.Expression.delete("1.0", END)
