income = float(input("Enter your annual taxable income:"))

brackets = [55867, 111733, 173205, 246752]
rates = [0.15, 0.205, 0.29, 0.33]

tax = 0.0
prev = 0.0

for i in range(len(brackets)):
    if income > brackets[i]:
        tax += (brackets[i] - prev) * rates[i]
        prev = brackets[i]
    else:
        tax += (income - prev) * rates[i]
        break
else:
    tax += (income - prev) * rates [-1]

print(f"Estimated federal tax payable: ${tax:.2f}")