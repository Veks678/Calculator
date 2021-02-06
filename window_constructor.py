from tkinter import *
import tkinter as tk


class Window:
    # Инициализация главного окна приложения
    root_main = Tk()

    def __init__(self, resizable, width, height, title):
        self.resizable = resizable
        self.width = width
        self.height = height
        self.title = title

    # Параметры главного окна
    def Create_main_window(self):
        # Заголовок окна
        self.root_main.title(self.title)
        # Размер окна
        self.root_main.geometry('{}x{}'.format(self.width, self.height))
        # Запрет пользователя на изменение рамеров окна
        self.root_main.resizable(self.resizable[0], self.resizable[1])

    # Запуска главного окна
    def Running_main_window(self):
        # Реализация бесконечного цикла окна (работа окна)
        self.root_main.mainloop()
