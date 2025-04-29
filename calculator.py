number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))
operation = input("Enter an operation (+, -, *, /): ")

if operation == '+':
    result = number1 + number2
elif operation == '-':
    result = number1 - number2
elif operation == '*':
    result = number1 * number2
elif operation == '/':
    if number2 == 0:
        result = "Error: Division by zero is not allowed."
    else:
        result = number1 / number2
else:
    result = "Invalid operation."

print("Result:", result)
