
"""
Created on Wed Aug 25 12:52:52 2021
AI and deep learnin with Python
Data types and operators
Quiz Data types and Operators 

"""
# The current volume of a water reservoir is ( in cubic meters)
reservoir_volume = 4.445e8

# The amount of rainfall from a storm (in cubic meters)
rainfall = 5e6

# Decrease the rainfall variable by 10% to account for runoff
rainfall *= 0.9 

# add the rainfall variable to the reservoir_volume variable
reservoir_volume += rainfall

print(reservoir_volume)