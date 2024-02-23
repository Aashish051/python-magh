from logic import CalculatorLogic

def perform_operation(a, b, choice):
    calc = CalculatorLogic()
    if choice == '1':
        return calc.add(a, b)
    elif choice == '2':
        return calc.subtract(a, b)
    elif choice == '3':
        return calc.multiply(a, b)
    elif choice == '4':
        return calc.divide(a, b)
    else:
        return None

