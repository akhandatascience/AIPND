"""
# Created on Sat Aug 28 12:52:52 2021
# AI and deep learnin with Python
Control Flow
Quiz List and comprehension 
"""

# Problem 1:

"""Use a list comprehension to create a new list first_names containing 
just the first names in names in lowercase.
"""
names = ["Rick Sanchez", "Morty Smith", "Summer Smith", 
          "Jerry Smith", "Beth Smith"]

first_names = [name.split()[0].lower() for name in names]
print(first_names)


# Problem 2: 

""" Quiz: Multiples of Three
Use a list comprehension to create a list multiples_3 containing 
the first 20 multiples of 3.
"""
# Try 1:
times_3 = []
counter = 0
if counter <= 20: 
    for i in range(1, 61):
        if i % 3 == 0:
            times_3.append(i)
            counter += 1
print(times_3)
        
#Try 2
times_3 = []
for i in range(1,21):
    times_3.append(i * 3)
print(times_3)

# Try 3
multiples_3 = [i*3 for i in range(1,21) ] # write your list comprehension here
print(multiples_3)

# Problem 3

"""Quiz: Filter Names by Scores

Use a list comprehension to create a list of names passed that only 
include those that scored at least 65.
"""
# Try 1
scores = {
             "Rick Sanchez": 70,
             "Morty Smith": 35,
             "Summer Smith": 82,
             "Jerry Smith": 23,
             "Beth Smith": 98
          }
passed = []
list_names = scores.items()
for element in list_names:
    name, score = element[0], element[1]
    if score >= 65:
        passed.append(name)
print(passed)

# Try 2
passed = [name for name, score in scores.items() if score >= 65] 
print(passed)




