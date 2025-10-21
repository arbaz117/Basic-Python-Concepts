
# Get input from the user for the first number
num1 = float(input("Enter the first number: "))

# Get input from the user for the second number
num2 = float(input("Enter the second number: "))

# Perform basic mathematical operations
addition = num1 + num2
subtract = num1 - num2
multiply = num1 * num2

# Handle division by zero
if num2 != 0:
    divide = num1 / num2
else:
    divide = "Cannot divide by zero"

# Display the results
print("Addition:", addition)
print("Subtraction:", subtract)
print("Multiplication:", multiply)
print("Division:", divide)