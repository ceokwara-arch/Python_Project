# Calculator
print("\nCalculator\n")

# Ask you if they want to use the calculator and wait for input
question = input("Do you want to use the calculator? yes or no ").lower()

# Wait for a Yes or No answer.
if question.lower () == "yes":
    print("\nLet's Start")
else:
    quit()

name = input("\nWhat's your name? ").lower()
print("\nHi", name.capitalize ())
# Ask the user for the first number and convert it to an integer
x = int(input("\nEnter the 1st number for the calculation? "))

# Ask the user to choose an operation: add, subtract, multiply, or divide
operation = input("\nChoose operation (+ - * /): ")

# Ask the user for the second number and convert it to an integer
y = int(input("\nEnter the 2nd number for the calculation? "))

# Check which operation the user selected

if operation == "+":
    # Add x and y
    z = x + y
elif operation == "-":
    # Subtract y from x
    z = x - y
elif operation == "*":
    # Multiply x and y
    z = x * y
elif operation == "/":
    # Divide x by y (check for division by zero)
    if y != 0:
        z = x / y
    else:
        print("Error: Cannot divide by zero")
        z = None
else:
    # Handle invalid operation input
    print("Invalid operation")
    z = None

# Only print the result if a valid operation was chosen
if z is not None:
    print("\nAnswer:", z)
