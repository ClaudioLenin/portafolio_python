# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 13:41:59 2023

@author: HP
"""

import tkinter as tk
from tkinter import ttk

def button_func():
    #get the content of the entry
    entry_text = entry.get() 
    
    #update the label
    #label.config(text = 'some other text')
    label['text'] = entry_text
    entry['state'] = 'disabled'
    print(label.configure())

#window
window = tk.Tk()
window.title('Getting and setting widgets')

#widgets
label = ttk.Label(master = window,text = 'Some text')
label.pack()

entry = ttk.Entry(master = window)
entry.pack()

button = ttk.Button(master = window, text = 'The button', command = button_func)
button.pack()

def reset_func():
    label['text'] = 'some text'
    entry['state'] = 'enabled'
    
exercise_button = ttk.Button(master = window, text = 'exercise button', command = reset_func)
exercise_button.pack()

#run
window.mainloop()