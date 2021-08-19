# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 11:09:09 2021
AI Nano degree Vector Lab 
Plotting a vector in 2D
@author: Loulou
"""
# import NumPy and Matplotlib 
import numpy as np
import matplotlib.pyplot as plt

# Define vector 
v = np.array([1,1])

# Plot vector v as blue arrow with red dot at origin(0,0) using Matplotlib
ax = plt.axes()

# plot red dot at origin(0,0)
ax.plot(0,0,'or')

# plot vector v as blue arrow starting at origin 0,0
ax.arrow(0,0, *v, color='blue', linewidth=2.0, head_width=0.20, head_length=0.25)

# format X-axis 
# Set limits for plot for X-axis
ax.set_xlim(-2,2)

# set major ticks for x-axis
major_xticks = np.arange(-2,3)
ax.set_xticks(major_xticks)

# Set limits for plot for Y-axis
ax.set_ylim(-2,2)

# set major ticks for y-axis
major_yticks = np.arange(-1,3)
ax.set_yticks(major_yticks)

# create gridlines for only major tick marks
plt.grid(b=True, which='major')

# Display final plot
plt.show()



