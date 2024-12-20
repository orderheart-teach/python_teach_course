def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero.")
    else:
        return x / y

def calculator():
    print("Welcome to the Simple Calculator!")
    
    operations = {
        '1': ('+', add),
        '2': ('-', subtract),
        '3': ('*', multiply),
        '4': ('/', divide)
    }
    
    while True:
        print("\nPlease select an operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Exit")
        
        choice = input("Enter the number corresponding to the operation (1/2/3/4/5): ").strip()
        
        if choice == '5':
            print("Thank you for using the calculator. Goodbye!")
            break
        
        if choice not in operations:
            print("Invalid choice. Please enter a number between 1 and 5.")
            continue
        
        operation_symbol, operation_func = operations[choice]
        
        try:
            num1 = float(input("Enter the first number: ").strip())
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue
        
        # Get the second number from the user
        try:
            num2 = float(input("Enter the second number: ").strip())
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue
        
        try:
            result = operation_func(num1, num2)
        except ValueError as ve:
            print(f"Error: {ve}")
            continue
        
        print(f"{num1} {operation_symbol} {num2} = {result}")

if __name__ == "__main__":
    calculator()