class MathOperations:
    # Method overloading using default arguments
    def add(self, a, b, c=0):  
        return a + b + c

# Usage
obj = MathOperations()
print("Sum of 2 numbers:", obj.add(5, 10))       # Calls method with two arguments
print("Sum of 3 numbers:", obj.add(5, 10, 15))   # Calls method with three arguments
