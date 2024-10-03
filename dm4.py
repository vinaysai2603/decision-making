'''
 A fruit seller buys a dozen of banana at Rs.X. He sells 1 banana at Rs.Y. Write a program to determine the profit or loss in Rs. for the fruitseller.
Input format:
Input consists of 2 floating point numbers
The first input corresponds to the total cost(X)
The second input corresponds to the sold cost(Y)
Output format:
Print "Profit or Loss" with Rupees.
Sample Input:
60
4
Sample Output:
Loss : Rs.12.00
'''
def calculate_profit_loss(total_cost, sold_cost_per_banana):
    # Calculate the total selling price for a dozen bananas
    sold_price_for_dozen = sold_cost_per_banana * 12
    
    # Calculate profit or loss
    profit_loss = sold_price_for_dozen - total_cost
    
    return profit_loss

# Input
total_cost = float(input("Enter the total cost of a dozen bananas (X): "))  # Total cost for a dozen bananas
sold_cost_per_banana = float(input("Enter the selling price per banana (Y): "))  # Selling price per banana

# Calculate profit or loss
profit_loss = calculate_profit_loss(total_cost, sold_cost_per_banana)

# Output the result
if profit_loss > 0:
    print(f"Profit : Rs.{profit_loss:.2f}")
elif profit_loss < 0:
    print(f"Loss : Rs.{-profit_loss:.2f}")
else:
    print("No Profit No Loss")

