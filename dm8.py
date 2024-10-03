'''
There are 3 labs in the CSE department are L1, L2, and L3 with a seating capacity of x, y, and z respectively. One of the 3 labs has been allocated for ACE training. Out of the available labs, find the lab which has minimal seating capacity.
Input format:
Input consists of 3 integers and a string
The first input denotes the seating capacity of L1(a)
The second input denotes the seating capacity of L2(b)
The third input denotes the seating capacity of L3(c)
The fourth input denotes the lab which is allocated for ACE training
Output format:
Print the minimal seating capacity lab amongst the available labs.
Refer the Sample output for formatting
Sample Input:
30
40
20
L3
Sample Output:
L1
'''
def find_minimal_lab(lab_capacities, allocated_lab):
    # Remove the allocated lab from the list of capacities
    del lab_capacities[allocated_lab]
    
    # Find the lab with minimal seating capacity
    minimal_lab = min(lab_capacities, key=lab_capacities.get)
    
    return minimal_lab

# Input
capacity_L1 = int(input("Enter the seating capacity of L1: "))  # Capacity of L1
capacity_L2 = int(input("Enter the seating capacity of L2: "))  # Capacity of L2
capacity_L3 = int(input("Enter the seating capacity of L3: "))  # Capacity of L3
allocated_lab = input("Enter the allocated lab for ACE training (L1, L2, L3): ")  # Allocated lab

# Store capacities in a dictionary
lab_capacities = {
    'L1': capacity_L1,
    'L2': capacity_L2,
    'L3': capacity_L3
}

# Find the lab with minimal seating capacity
minimal_lab = find_minimal_lab(lab_capacities, allocated_lab)

# Output the result
print(minimal_lab)
