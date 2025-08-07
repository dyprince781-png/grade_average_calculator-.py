# Grade Average Calculator

# Ask the user for number of subjects
num_subjects = int(input("How many subjects? "))

# Create a list to store all the grades
grades = []

# Get each grade
for i in range(num_subjects):
    grade = float(input(f"Enter grade for subject {i+1}: "))
    grades.append(grade)

# Calculate the average
average = sum(grades) / num_subjects

# Print the result
print(f"\nYour average grade is: {average:.2f}")

# Check performance
if average >= 70:
    print("Amazing result!")
elif average >= 60:
    print("Good job.")
elif average >= 50:
    print("You passed.")
else:
    print("You have to work on your skill") 
