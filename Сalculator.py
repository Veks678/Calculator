from tkinter import *
import tkinter as tk
import time


root = Tk()
root.title(' Калькулятор')
root.geometry('205x292')
root.resizable(width = False, height = False)


class Frames():
    List_frames = []
    def __init__(self, background_line = 'olivedrab', width_line = 205,\
                 height_line = 44):
        self.background_line = background_line
        self.width_line = width_line
        self.height_line = height_line
        self.List_name_frames = ['Expression_line', 'Decision_line', \
                                 'First_line', 'Second_line', 'Third_line', \
                                 'Fourth_line', 'Fifth_line']

    def creature(self):
        for name_line in self.List_name_frames:
            if name_line in 'Decision_line':
                name_line = Frame(root, background = self.background_line, \
                                  width = self.width_line, height = 29)
                self.List_frames.append(name_line)
            else:
                name_line = Frame(root, background = self.background_line, \
                                  width = self.width_line,
                                  height = self.height_line)
                self.List_frames.append(name_line)

            for line in self.List_frames:
                line.pack()
                line.pack_propagate(False)

class Creating_buttons():
    def __init__(self, frame_buttons = 'default', command_buttons = 'default'):
        self.frame_buttons = frame_buttons
        self.bg_buttons = "#555"
        self.fg_buttons = "white"
        self.font_buttons = "Arial 14"
        self.width_buttons = 3
        self.command_buttons = command_buttons

    def parameter_selection(self):
        if self.command_buttons in ('1','2','3','4','5','6','7','8','9','0'):
            self.bg_buttons = "#444"

        Reusable_button = Button(self.frame_buttons,
                                 text = self.command_buttons,
                                 bg = self.bg_buttons, fg = self.fg_buttons,
                                 font = self.font_buttons,
                                 width = self.width_buttons,
                       command = Buttons_logic(self.command_buttons).push_logic)

        Reusable_button.pack(side = LEFT, padx = 2, pady = 2)

class Call_buttons():
    def __init__(self):

        Command_buttons_list = ['7','8','9','+','4','5','6','-','1',\
                                '2','3','*','←','0','c','/','.']

        index_frame_list = [2, 3, 4, 5, 6]

        for s in Command_buttons_list:
            if s in ('7','8','9','+'):
                Object_creating_button = \
                Creating_buttons(Frames.List_frames[index_frame_list[0]], s)
            elif s in ('4','5','6','-'):
                Object_creating_button = \
                Creating_buttons(Frames.List_frames[index_frame_list[1]], s)
            elif s in ('1','2','3','*'):
                Object_creating_button = \
                Creating_buttons(Frames.List_frames[index_frame_list[2]], s)
            elif s in ('←','0','c','/'):
                Object_creating_button = \
                Creating_buttons(Frames.List_frames[index_frame_list[3]], s)
            elif s in ('.'):
                Object_creating_button = \
                Creating_buttons(Frames.List_frames[index_frame_list[4]], s)

            Object_creating_button.parameter_selection()

class Buttons_logic():
    def __init__(self, buttons_names):
        self.buttons_names = buttons_names

    def push_logic(self):
        def check_number_output(number_symbol, Decision_str):

            if number_symbol in ('0'):
                if not Decision_str or '.' in Decision_str \
                   or [s for s in Decision_str[0] if s in ('123456789')] \
                   or (Decision_str[0] not in '-'\
                       and Decision_str[-1:] not in '0')\
                   or (Decision_str[0] in '-' and len(Decision_str) == 1)\
                   or (Decision_str[0] in '-' and Decision_str[1] not in '0' ):
                    Decision.insert(END, number_symbol)
                else:
                    return
            else:
                if not Decision_str or '.' in Decision_str \
                   or (Decision_str[0] not in '-' \
                       and Decision_str[0] not in '0')\
                   or (Decision_str[0] in '-' and Decision_str[-1] not in '0')\
                   or (Decision_str[0] in '-' \
                      and [s for s in Decision_str if s in ('123456789')]):
                    Decision.insert(END, number_symbol)
                else:
                    return

        def check_symbol_output(special_symbol, Decision_str):

            if special_symbol in 'c':
                Expression.delete("1.0", END)
                Decision.delete(0, END)

            elif special_symbol in '←':
                Decision.delete(len(Decision_str)-1)

            elif special_symbol in '.':
                if '.' in Decision_str or not Decision_str\
                                       or Decision_str in '-':
                    return
                else:
                    Decision.insert(END, ".")

        def check_arithmetic_output(arithmetic_symbol, Decision_str):
            if arithmetic_symbol in '-':
                if not Decision_str:
                    Decision.insert(1, '-')
                    return
                elif Decision_str[0] in '-' and Decision_str[-1:] in '-':
                    print('\nОшибка! Число не найдено')
                    return

            if arithmetic_symbol in ('+','*','/','-'):
                if Decision_str[-1:].isdigit() == False:
                    print('\nОшибка! Число не найдено')
                    return
                if '-' in Decision.get() \
                       and Expression.get("1.0", END).isdigit() == False\
                       and Decision_str[-1:].isdigit() == True:
                    Expression.insert(END, '(' + Decision_str + ')')
                    Expression.insert(END, ' ' + arithmetic_symbol + ' ')
                    Decision.delete(0, END)
                else:
                    Expression.insert(END, Decision_str)
                    Expression.insert(END, ' ' + arithmetic_symbol + ' ')
                    Decision.delete(0, END)

        if ([s for s in self.buttons_names if s in ('1234567890')]):
            check_number_output(self.buttons_names, Decision.get())
        elif self.buttons_names in ('c','←','.'):
            check_symbol_output(self.buttons_names, Decision.get())
        elif self.buttons_names in ('+','-','*','/'):
            check_arithmetic_output(self.buttons_names, Decision.get())

class Calculation_logic():
    def __init__(self):
        Expression.insert(END, Decision.get())
        self.Decision_str = Decision.get()
        self.Expression_str = Expression.get("1.0", END)

    def Input_processing(self):
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

        Expressions_concatenated = Calculation_logic().Input_processing()

        if len(Expression.get("1.0", END)) == 1:
            print('\nОшибка! Арифметическое действие не найдено')
            return
        if self.Expression_str[-1:] in ("+" ,"-" ,"*" ,"/"):
            print('\nОшибка! Не найдено числа после арифметического знака!\n')
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

        Decision.delete(0, END)
        Decision.insert(END, result)
        Expression.delete("1.0", END)

def check_keys(event):
    if (event.state & 4 and event.keysym == "v") or \
        event.char.isdigit() == False:
        return "break"


Object_Frames = Frames('olivedrab', 205, 44)
Object_Frames.creature()


Decision = Entry(Frames.List_frames[1], background = "gainsboro", \
                 foreground = "black", font = "Arial 13", width = 17)
Decision.bind("<Key>", check_keys)
Decision.pack(side = LEFT, padx = 1, pady = 1, fill = Y)

Expression = Text(Frames.List_frames[0], background = "gainsboro", \
                  font = "Arial 9", foreground = "black", width = 25)
Expression.bind("<Key>", check_keys)
Expression.pack(side = LEFT, padx = 1, pady = 1)

Pixel_Virtual = tk.PhotoImage(width = 1)
Equally = Button(Frames.List_frames[6], text = "=", background = "#555",
                 image = Pixel_Virtual, compound = 'c', font = "Arial 12",
                 command = Calculation_logic().Processing_computation,
                 foreground = "white",  width = 147,)
Equally.pack(side = LEFT, padx = 2, pady = 2, fill = Y)


Object_Call_buttons = Call_buttons()



root.mainloop()
