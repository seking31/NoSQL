"""
Author: Sara King
Date: June 15, 2025
File Name: King_lemonadeStand.py
Description: This file simulates a lemonade stand 
"""

def calculate_cost(lemons_cost, sugar_cost):
    return lemons_cost + sugar_cost 

def calculate_profit(lemons_cost, sugar_cost, selling_price):
    total_cost = calculate_cost(lemons_cost, sugar_cost)  
    return selling_price - total_cost  

lemons_cost = 4.25
sugar_cost = 2.75
selling_price = 10.00

cost_output = f"${lemons_cost} + ${sugar_cost} = ${calculate_cost(lemons_cost, sugar_cost)}"
profit_output = f"Selling Price: ${selling_price}, Cost: ${calculate_cost(lemons_cost, sugar_cost)}, Profit: ${calculate_profit(lemons_cost, sugar_cost, selling_price)}"

print(cost_output)

print(profit_output)
