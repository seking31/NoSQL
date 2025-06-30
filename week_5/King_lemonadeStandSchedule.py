"""
Author: Sara King
Date: June 29, 2025
File Name: King_lemonadeStandSchedule.py
Description: A simple program to manage a weekly task schedule for a lemonade stand.
"""

tasks = [
    "Buy lemons",         
    "Make lemonade",     
    "Sell lemonade",     
    "Count money",    
    "Clean up"            
]

# Using a for loop to iterate over the list and print each task
print("Lemonade Stand Tasks:")
for task in tasks: 
    print(f"- {task}")  

print("\nWeekly Schedule:")

days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

for i in range(len(days)):  
    day = days[i]
    if day == "Saturday" or day == "Sunday":
        print(f"{day}: Day off! Time to rest.")
    else:
        task = tasks[i % len(tasks)]
        print(f"{day}: Task - {task}")
