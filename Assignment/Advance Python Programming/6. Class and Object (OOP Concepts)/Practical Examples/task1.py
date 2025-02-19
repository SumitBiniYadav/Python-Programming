class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Creating an object of the Person class
person1 = Person("Alice", 25)

# Accessing properties of the class using an object
print(f"Person's Name: {person1.name}")
print(f"Person's Age: {person1.age}")

# Calling the method to display information
person1.display_info()
