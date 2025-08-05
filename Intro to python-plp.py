 # Step 1: Define operation functions
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero!"
    return a / b

# Step 2: Map operations to functions in a dictionary
operations = {"+": add, "-": subtract, "*": multiply, "/": divide}

# Step 3: Get user input
print("Enter the first number:")
first_number = float(input())

print("Enter the second number:")
second_number = float(input())

print("Enter the operation (+, -, *, /):")
operation = input().strip()

# Step 4: Perform the operation using the dictionary
if operation in operations:
    result = operations[operation](first_number, second_number)
    
    # Step 5: Display the result
    if result == "Error: Division by zero!":
        print(result)
    else:
        print(f"The result of {first_number} {operation} {second_number} is {result}")
else:
    print("Error: Invalid operation. Please use +, -, *, or /")
 