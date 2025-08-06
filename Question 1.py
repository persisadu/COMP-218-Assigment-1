# Program to find the biggest of three numbers

#Input: Read three numbers from the user
num1 = float(input("Enter the first number:"))
num2 = float(input("Enter the second number:"))
num3 = float(input("Enter the third number:"))

# Find the largest number
largest = max(num1, num2, num3)

# Output the result
print("The biggest number is:", largest)