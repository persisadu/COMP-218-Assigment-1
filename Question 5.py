num = int(input("Enter number of graded items (e.g., assignments, exams):"))

total_weight = 0
weighted_suum = 0

for i in range(num):
    score = float(input(f"Enter percentage grade for item #{i+1}: "))
    weight = float(input(f"Enter weight of item #{i+1} (as a percentage):"))
    total_weight += weight
    weighted_sum += score * (weight / 100)

if total_weight != 100:
    print("Warning: Total weights do not add up to 100%.")

print(f"Final weighted percentage: {weighted_sum:.2f}%")

if weighted_sum >= 90:
    gpa = 4.0
elif weighted_sum >= 85:
    gpa = 3.9
elif weighted_sum >= 80:
    gpa = 3.7
elif weighted_sum >= 77:
    gpa = 3.3
elif weighted_sum >= 73:
    gpa = 3.0
elif weighted_sum >= 70:
    gpa = 2.7
elif weighted_sum >= 67:
    gpa = 2.3
elif weighted_sum >= 63:
    gpa = 2.0
elif weighted_sum >= 60:
    gpa = 1.7
elif weighted_sum >= 57:
    gpa = 1.3
elif weighted_sum >= 53:
    gpa = 1.0
elif weighted_sum >= 50:
    gpa = 0.7
else:
    gpa = 0.0

print(f"Your GPA is: {gpa:.1f}")    