from functions import perform_operation

def get_user_input():
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    return a, b

def display_menu():
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

def main():
    a, b = get_user_input()
    display_menu()
    choice = input("Enter choice (1/2/3/4): ")

    result = perform_operation(a, b, choice)
    if result is not None:
        print("Result:", result)
    else:
        print("Invalid input")

if __name__ == "__main__":
    main()
