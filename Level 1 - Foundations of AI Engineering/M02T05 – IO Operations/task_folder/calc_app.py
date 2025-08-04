# create a simple calculator application that handles exceptions
def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero.")
    return x / y
def calculator():
    while True:
        try:
            print("Select operation:")
            print("1. Add")
            print("2. Subtract")
            print("3. Multiply")
            print("4. Divide")
            print("5. Exit")
            
            choice = input("Enter choice (1/2/3/4/5): ")
            
            if choice == '5':
                print("Exiting the calculator.")
                break
            
            if choice not in ['1', '2', '3', '4']:
                raise ValueError("Invalid choice. Please select a valid operation.")
            
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            
            if choice == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")
                # store calculation in text file equation.txt
                with open("equation.txt", "a") as file:
                    file.write(f"{num1} + {num2} = {add(num1, num2)}\n")
            elif choice == '2':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")
                # store calculation in text file equation.txt
                with open("equation.txt", "a") as file:
                    file.write(f"{num1} - {num2} = {subtract(num1, num2)}\n")
            elif choice == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")
                # store calculation in text file equation.txt
                with open("equation.txt", "a") as file:
                    file.write(f"{num1} * {num2} = {multiply(num1, num2)}\n")
            elif choice == '4':
                print(f"{num1} / {num2} = {divide(num1, num2)}")
                # store calculation in text file equation.txt
                with open("equation.txt", "a") as file:
                    file.write(f"{num1} / {num2} = {divide(num1, num2)}\n")
        
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

# if the user wants to display the previous equations from the text file equation.txt
def display_equations():
    try:
        with open("equation.txt", "r") as file:
            equations = file.readlines()
            if equations:
                print("Previous calculations:")
                for equation in equations:
                    print(equation.strip())
            else:
                print("No previous calculations found.")
    except FileNotFoundError:
        print("No calculations have been made yet.")
        