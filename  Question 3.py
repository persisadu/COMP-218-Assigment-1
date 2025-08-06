# Program to calculate daily employee pay

# Input: workday/weekend and hours worked
day_type = input("Enter day type (weekday/weekend: ").strip().lower()
hours_worked = float(input("Enter hours worked:"))

# Pay calculation
if day_type == "weekday":
    regular_hours = min(hours_worked, 8)
    overtime_hours = max(0, hours_worked - 8)
    total_pay = (regular_hours * 15) + (overtime_hours * 21)
elif day_type == "weekend":
    total_pay = hours_worked * 21
else:
    print("Invalid input for day type. Please enter 'weekday' or 'weekend'.")
    total_pay = 0

print(f"Total pay for the day: ${total_pay:.2f}")