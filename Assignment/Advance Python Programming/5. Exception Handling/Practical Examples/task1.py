def calculator():
    while True:
        try:
            num1 = float(input("Enter first number: "))
            operator = input("Enter operator (+, -, *, /): ")
            num2 = float(input("Enter second number: "))

            if operator == '+':
                result = num1 + num2
            elif operator == '-':
                result = num1 - num2
            elif operator == '*':
                result = num1 * num2
            elif operator == '/':
                if num2 == 0:
                    raise ZeroDivisionError("Cannot divide by zero.")
                result = num1 / num2
            else:
                raise ValueError("Invalid operator.")

            print(f"Result: {result}")
        
        except ValueError as ve:
            print(f"Error: {ve}")
        except ZeroDivisionError as zde:
            print(f"Error: {zde}")
        except Exception as e:
            print(f"Unexpected error: {e}")
        
        choice = input("Do you want to calculate again? (yes/no): ").strip().lower()
        if choice != 'yes':
            print("Exiting calculator. Goodbye!")
            break

if __name__ == "__main__":
    calculator()