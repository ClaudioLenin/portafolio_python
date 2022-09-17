# -*- coding: utf-8 -*-
"""
Created on Sat Feb 26 14:51:22 2022

@author: PC HP
"""
import numpy as np
import matplotlib.pyplot as plt
plt.rcdefaults()

fig, ax = plt.subplots()

#Examples data
people = ("Lilian","Sthephania","Claudio","Lenin")
y_pos = np.arange(len(people))
performance = 3 + 10 * np.random.rand(len(people))
error = np.random.rand(len(people))

ax.barh(y_pos,performance,xerr=error,align="center",color="green",ecolor="black")
ax.set_yticks(y_pos)
ax.set_yticklabels(people)
ax.invert_yaxis()#labels read top-to-bottom
ax.set_xlabel('Performance')
ax.set_title("How fast do you want to go today?")

plt.show()