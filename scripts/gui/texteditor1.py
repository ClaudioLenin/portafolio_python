# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 18:30:22 2023

@author: HP
"""

import tkinter as tk
from tkinter import ttk

def button_func():
    print('test')

def exercise_button_func():
    print('hello')
#create a window
window = tk.Tk()
window.title('Window and Widgets')
window.geometry('800x500')

#ttk label
label = ttk.Label(master = window,text = 'This is a test')
label.pack()

#tk.text
text = tk.Text(master = window)
text.pack()

#ttk entry
entry = ttk.Entry(master = window)
entry.pack()

#exercise label
exercise_label = ttk.Label(master = window,text = 'my label')
exercise_label.pack()

#ttk button
button = ttk.Button(master = window,text = 'A button', command = button_func)
button.pack()

#exercise button
#exercise_button = ttk.Button(master = window,text = 'exercise button', command = exercise_button_func)
exercise_button = ttk.Button(master = window,text = 'exercise button', command = lambda: print('hello'))
exercise_button.pack()

#run
window.mainloop()
