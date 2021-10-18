# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import ttk
import os

from input_rules import Rules
	
class Constructor_gui(Frame):
    field_list = []
    
    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)
        self.widgets_paramm = {'7':{'x':2,'y':125,'h':40,'w':65,'bg':"#444",'fg':"white"},\
                               '8':{'x':69,'y':125,'h':40,'w':65,'bg':"#444",'fg':"white"},\
                               '9':{'x':136,'y':125,'h':40,'w':65,'bg':"#444",'fg':"white"},\
                               '+':{'x':203,'y':125,'h':40,'w':40,'bg':"gray18",'fg':"white"},\
                               '4':{'x':2,'y':167,'h':40,'w':65,'bg':"#444",'fg':"white"},\
                               '5':{'x':69,'y':167,'h':40,'w':65,'bg':"#444",'fg':"white"},\
                               '6':{'x':136,'y':167,'h':40,'w':65,'bg':"#444",'fg':"white"},\
                               '-':{'x':203,'y':167,'h':40,'w':40,'bg':"gray18",'fg':"white"},\
                               '1':{'x':2,'y':209,'h':40,'w':65,'bg':"#444",'fg':"white"},\
                               '2':{'x':69,'y':209,'h':40,'w':65,'bg':"#444",'fg':"white"},\
                               '3':{'x':136,'y':209,'h':40,'w':65,'bg':"#444",'fg':"white"},\
                               '*':{'x':203,'y':209,'h':40,'w':40,'bg':"gray18",'fg':"white"},\
                               '←':{'x':2,'y':251,'h':40,'w':65,'bg':'gray18','fg':"white"},\
                               '0':{'x':69,'y':251,'h':40,'w':65,'bg':"#444",'fg':"white"},\
                               'C':{'x':136,'y':251,'h':40,'w':65,'bg':'gray18','fg':"white"},\
                               '/':{'x':203,'y':251,'h':40,'w':40,'bg':'gray18','fg':"white"},\
                               '=':{'x':2,'y':293,'h':40,'w':199,'bg':'gray18','fg':"white"},\
                               '.':{'x':203,'y':293,'h':40,'w':40,'bg':'gray18','fg':"white"}}
        
#------------------------------------------------------------------------------ 
    def windows_constructor(self, title, geometry, resizable, bg):
        self.master.attributes("-topmost",True) 
        self.master.title(title)
        self.master.geometry(f'{geometry[0]}x{geometry[1]}+{geometry[2]}+{geometry[3]}')
        self.master.resizable(resizable[0], resizable[1])
        self.master["bg"] = bg
        
        return self.master

#------------------------------------------------------------------------------   
    
    def text(self, bg_t, fg_t, font_t):        
        widget = Text(self.master, bg = bg_t, fg = fg_t, font = font_t) 
        
        widget.bind('<Key>', self.check_keys) 
        self.field_list.append(widget)
        
        widget.pack_propagate(False)
        widget.pack(expand = True, fill = BOTH)
        return widget           
     
    def check_keys(self, event):
        return "break"    
    
    def label(self, bg_l, fg_l, font_l):    
        widget = Label(self.master, bg = bg_l, fg = fg_l, font = font_l)
        
        widget.pack_propagate(False)
        widget.pack(expand = True, fill = BOTH)
        return widget        
    
    def button(self, bg_b, fg_b, font_b, text_b):  
        widget = Button(self.master, bg = bg_b, fg = fg_b,\
                        font = font_b, text = text_b,\
                        command = lambda: Rules(text_b, self.field_list).distribute())
    
        widget.pack_propagate(False)
        widget.pack(expand = True, fill = BOTH)
        
        return widget     

    def text_constructor(self):
        #---------------------------------------------------------------------
        widget = self.text("gainsboro", "black", "Arial 10 bold")
        widget.config(spacing1 = 1)
        widget.place(x = 2, y = 2, height = 89, width = 241)  
        #---------------------------------------------------------------------
        widget = self.text("gainsboro", "black", "Arial 13")
        widget.config(spacing1 = 1)
        widget.place(x = 2, y = 93, height = 30, width = 241)  
        #---------------------------------------------------------------------         
    def button_constructor(self):
        
        for name in self.widgets_paramm:
            widget = self.button(self.widgets_paramm[name]['bg'],\
                                 self.widgets_paramm[name]['fg'],"Arial 14", name)
            
            widget.place(x = self.widgets_paramm[name]['x'],\
                         y = self.widgets_paramm[name]['y'],\
                         height = self.widgets_paramm[name]['h'],\
                         width = self.widgets_paramm[name]['w'])      
        
#------------------------------------------------------------------------------ 
def run_gui():
    window = Constructor_gui(Tk())
    
    window.windows_constructor('Calculator', [245, 335, 471, 398],\
                             [False, False], "royalblue4")

    window.text_constructor()
    window.button_constructor()
    
    window.mainloop()