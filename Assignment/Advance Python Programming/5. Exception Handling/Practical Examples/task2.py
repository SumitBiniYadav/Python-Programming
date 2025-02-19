def handle_exceptions():
    try:
        filename = input("Enter filename: ")
        with open(filename, 'r') as file:
            data = file.read()
            print("File content:", data)

        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        result = num1 / num2
        print(f"Division result: {result}")

    except FileNotFoundError:
        print("Error: The specified file was not found.")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except ValueError:
        print("Error: Invalid input. Please enter numeric values.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    
    finally:
        print("Execution completed.")

if __name__ == "__main__":
    handle_exceptions()
