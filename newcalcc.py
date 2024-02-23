def get_user_input():
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    return a, b

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        print("Error: Division by zero!")
        return None
    else:
        return a / b

def calculator():
    a, b = get_user_input()
    
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter choice (1/2/3/4): ")

    if choice == '1':
        result = add(a, b)
        print("Result:", result)
    elif choice == '2':
        result = subtract(a, b)
        print("Result:", result)
    elif choice == '3':
        result = multiply(a, b)
        print("Result:", result)
    elif choice == '4':
        result = divide(a, b)
        if result is not None:
            print("Result:", result)
    else:
        print("Invalid input")

calculator()



