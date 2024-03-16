# Objective:
# The aim of this assignment is to integrate 
# various list operations and methods to solve a complex problem.

# Problem Statement:
# You're organizing a school event, and you have 
# lists containing student names, their grades, and the activities they're interested in.

# Task 1: Given the lists:

# students = ["John", "Doe", "Jane", "Smith"]
# grades = [85, 90, 78, 88]
# activities = ["Football", "Music", "Art", "Dance"]

# Filter out students who have grades below 80. Print 
# the name, grade and activiy. Expected Outcome "Jane", 78, "Art"

students = ["John", "Doe", "Jane", "Smith"]
grades = [85, 90, 78, 88]
activities = ["Football", "Music", "Art", "Dance"]

i=0
Failures = []
while i <= len(grades)-1:
    if grades[i] < 80:
        Failures.append(students[i])
        Failures.append(grades[i])
        Failures.append(activities[i])
        i += 1
    else:
        i += 1
print(Failures)
    

# Task 2: For the remaining students, add students name 
# in a new list named students_approved. Expected Outcome: students_approved = ["John", "Doe", "Smith"]
students_approved = []
x = 0
while x <= len(grades)-1:
    if grades[x] < 80:
        x += 1
    else:
        students_approved.append(students[x])
        x += 1


# Task 3: Print the list students_approved
print(students_approved)