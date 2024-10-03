'''
There are 3 labs in the CSE department are L1, L2, and L3 with a seating capacity of x, y, and z. A single lab needs to be allocated to a class of 'n' students. How many of the 3 labs can accommodate 'n' students?
Input format:
Input consists of 4 integers
The first input denotes the seating capacity of L1(a)
The second input denotes the seating capacity of L2(b)
The third input denotes the seating capacity of L3(c)
The fourth input denotes the number of students(x)
Output format:
Print the number of labs which can accommodate the 'n' number of students
Refer the Sample output for formatting
Sample Input:
30
40
20
25
Sample Output:
2 
'''
def count_accommodating_labs(capacities, num_students):
    count = sum(1 for capacity in capacities if capacity >= num_students)
    return count

# Input
capacity_L1 = int(input("Enter the seating capacity of L1: "))  # Capacity of L1
capacity_L2 = int(input("Enter the seating capacity of L2: "))  # Capacity of L2
capacity_L3 = int(input("Enter the seating capacity of L3: "))  # Capacity of L3
num_students = int(input("Enter the number of students: "))  # Number of students

# Store capacities in a list
capacities = [capacity_L1, capacity_L2, capacity_L3]

# Count the labs that can accommodate the number of students
available_labs_count = count_accommodating_labs(capacities, num_students)

# Output the result
print(available_labs_count)
