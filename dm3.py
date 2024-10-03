'''
The newly appointed Vice-Chancellor of Anna University wanted to create an automated grading system for the students to check their grade. When a student enters a mark, the grading system displays the corresponding grade.
Write a program to solve the given problem.
  Marks scored  
  Grade 
100
S
90 - 99
A
80 - 89
B
70 - 79
C
60 - 69
D
50 - 59
E
<50
F

Input format:
The input consists of one integer which corresponds to the marks scored by the student

Output format:
If a student marks greater than 100, print "Invalid Input". Otherwise, print the grade.
Sample Input:
78
Sample Output:C
'''
def determine_grade(marks):
    if marks > 100:
        return "Invalid Input"
    elif marks == 100:
        return "S"
    elif 90 <= marks < 100:
        return "A"
    elif 80 <= marks < 90:
        return "B"
    elif 70 <= marks < 80:
        return "C"
    elif 60 <= marks < 70:
        return "D"
    elif 50 <= marks < 60:
        return "E"
    elif marks < 50:
        return "F"
    else:
        return "Invalid Input"  # This handles any unexpected input

# Input
marks = int(input("Enter the marks scored: "))  # Read marks as an integer

# Determine the grade
result = determine_grade(marks)

# Output the result
print(result)
