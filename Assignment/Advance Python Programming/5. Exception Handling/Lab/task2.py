def calculator():
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
                raise ZeroDivisionError("Error: Division by zero is not allowed.")
            result = num1 / num2
        else:
            raise ValueError("Error: Invalid operator.")
        
        print(f"Result: {result}")
    
    except ValueError as ve:
        print(f"Invalid input: {ve}")
    except ZeroDivisionError as zde:
        print(zde)
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("Execution completed.")

if __name__ == "__main__":
    calculator()
