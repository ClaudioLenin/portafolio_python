# -*- coding: utf-8 -*-
"""
Created on Sat Jul  2 20:08:58 2022

@author: Claudio Pilataxi
"""
message = "Three can keep a secret, if two of them are dead."
translated = ""

i = len(message)-1

while(i>=0):
    translated = translated + message[i]
    i=i-1

print(translated)
    
