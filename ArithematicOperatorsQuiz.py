
"""
AI and deep learnin with Python
Data types and operators
Quiz Data types and Operators 
"""

#  Problem 1
"""
Average Electricity Bills 
Write an expression that calculates the average of 23, 32 and 64
Place the exppression in the print()
"""
average_num = (23 + 32 + 64)/3.0 # calculate mean average
print("The average electricity bill is ", "$ ", '{:.2f}'.format(average_num))

""" 
Calculate number of tiles
Two parts of floor need tiling. One part is 9 tiles wide by 7 tiles long. 
The other is 5 tiles wide by 7 tiles long. Tiles come in package of 6. 
"""

#  Problem 2

# Calculating the total number of tiles
NumberTilesTotal = (9 * 7) + (5 * 7)
print("The total number of tiles are ", NumberTilesTotal)

# You bought 17 packages of 6 tiles each. Now calculate how many tiles will be left
NumberofTilesLeft = (17 * 6) - NumberTilesTotal
print("The number of tiles will be left over are ", NumberofTilesLeft)
   


