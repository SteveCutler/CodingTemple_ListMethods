# Objective:
# The aim of this assignment is to delve deeper into list methods
# and understand the nuances of identity operators.

# Problem Statement:
# You have two lists of student names. One list contains the 
# names of students who have submitted their assignments, 
# and the other list contains the names of students who attended the last class.

# Task 1: Given the two lists:

# submitted = ["Alice", "Bob", "Charlie", "David"]
# attended = ["Charlie", "Eve", "Alice", "Frank"]

# Find out which students both submitted their assignments and attended the class.

submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]

submittedAndAttended = []
for name in submitted:
    if name in attended:
        submittedAndAttended.append(name) 
    else:
        pass

print(submittedAndAttended,"both submitted their assignments and attended class")

# Task 2: Check if the two lists are identical in terms of their content, regardless of order.

submitted.sort()
attended.sort()
print("True") if submitted == attended else print("False")

print(submitted)
print(attended)

# Task 3: Using list methods, remove any student from 
# the attended list who did not submit their assignment.

i=0
keepName = []

while i <= (len(attended)-1):
    if attended[i] in submitted:
        keepName.append(attended[i])
        i+=1
    else:
        i+=1

for name in attended:
    if name in keepName:
        pass
    else:
        attended.remove(name)

print(attended)

