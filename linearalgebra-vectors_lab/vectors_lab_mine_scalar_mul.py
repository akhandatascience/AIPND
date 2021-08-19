# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 11:58:42 2021
scaling a vector using a scalar 
@author: Loulou
"""
# import NumPy and Matplotlib 
import numpy as np
import matplotlib.pyplot as plt

# Define vector 
v = np.array([1,1])

# define scalar 
a = 3

# define vector av as vector v multiplied by a scalar a
av = a * v

# Plot vector v as blue arrow with red dot at origin(0,0) using Matplotlib
ax = plt.axes()

# plot red dot at origin(0,0)
ax.plot(0,0,'or')

# plot vector v as blue arrow starting at origin 0,0
ax.arrow(0,0, *v, color='blue', linewidth=2.5, head_width=0.30, head_length=0.35)

# plot vector v as dotted vector of cyan color
ax.arrow(0,0, *av, color='cyan', linestyle='dotted', linewidth=2.5, 
         head_width=0.30, head_length=0.35)

# format X-axis 
# Set limits for plot for X-axis
ax.set_xlim(-1,5)

# set major ticks for x-axis
major_xticks = np.arange(-1,5)
ax.set_xticks(major_xticks)

# Set limits for plot for Y-axis
ax.set_ylim(-1,5)

# set major ticks for y-axis
major_yticks = np.arange(-1,5)
ax.set_yticks(major_yticks)

# create gridlines for only major tick marks
plt.grid(b=True, which='major')

# Display final plot
plt.show()

