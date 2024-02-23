# Calculator
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))

print("1. Add\n2. Subtract\n3. Multiply\n4. Divide" )


choice = input("Enter choice (1/2/3/4): ")

if choice == '1':
    result = a + b
    print("Result:", result)
elif choice == '2':
    result = a - b
    print("Result:", result)
elif choice == '3':
    result = a * b
    print("Result:", result)
elif choice == '4':
    if b == 0:
        print("Error: Division by zero!")
    else:
        result = a / b
        print("Result:", result)
else:
    print("Invalid input")
