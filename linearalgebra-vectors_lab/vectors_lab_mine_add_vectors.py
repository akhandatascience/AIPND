# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 21:06:25 2021
AI Nano degree Vector Lab 
Adding two vectors in 2D
@author: Loulou
"""
# import NumPy and Matplotlib 
import numpy as np
import matplotlib.pyplot as plt

# Define vectors 
firstVector = np.array([1,1])
secondVector = np.array([-2,2])

# Add the above two vectors
sumVecors = firstVector + secondVector


# Plot vector v as blue arrow with red dot at origin(0,0) using Matplotlib
ax = plt.axes()

# plot red dot at origin(0,0)
ax.plot(0,0,'or')

# plot first vector as blue arrow starting at origin 0,0
ax.arrow(0,0, *firstVector, color='blue', linewidth=2.5, 
         head_width=0.30, head_length=0.35)

# plot the second vector of cyan color
ax.arrow(0,0, *secondVector, color='cyan', linewidth=2.5, 
         head_width=0.30, head_length=0.35)

# plot the second vector as dotted vector parallel to the original vector
ax.arrow(1,1, *secondVector, color='cyan', linewidth=2.5, 
         linestyle='dotted', head_width=0.30, head_length=0.35)

# plot the vector sum as dotted vector of red color
ax.arrow(0,0, *sumVecors, color='red', linewidth=2.5, 
         head_width=0.30, head_length=0.35)

# format X-axis 
# Set limits for plot for X-axis
ax.set_xlim(-3,3)

# set major ticks for x-axis
major_xticks = np.arange(-3,3)
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

