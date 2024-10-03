'''

 There are 3 labs in the CSE department. The labs are L1, L2, and L3 with a seating capacity of x, y, and z respectively. A single lab needs to be allocated to a class of 'n' students. The labs need to be utilized to the maximum i.e the number of systems used should not be minimal. Which lab needs to be allocated to this class?
Input format:
Input consists of 4 integers
The first input denotes 'x'
The second input denotes 'y'
The third input denotes 'z'
The fourth input denotes 'n'
Output format:
Print the lab which is suitable for  'n' number of students
Refer the Sample output for formatting
Sample Input:
30
40
20
25
Sample Output:
L1
'''
def allocate_lab(x, y, z, n):
    labs = {'L1': x, 'L2': y, 'L3': z}
    
    suitable_labs = {lab: capacity for lab, capacity in labs.items() if capacity >= n}
    
    if not suitable_labs:
        return "No suitable lab available"
    
    # Find the lab with maximum capacity that can accommodate n students
    selected_lab = max(suitable_labs, key=suitable_labs.get)
    
    return selected_lab

# Input
x = int(input("Enter the capacity of L1: "))  # Seating capacity for L1
y = int(input("Enter the capacity of L2: "))  # Seating capacity for L2
z = int(input("Enter the capacity of L3: "))  # Seating capacity for L3
n = int(input("Enter the number of students: "))  # Number of students

# Allocate the lab
result = allocate_lab(x, y, z, n)

# Output the result
print(result)

