# Parent class
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return "Animal makes a sound"

# Intermediate class inheriting from Animal
class Mammal(Animal):
    def has_fur(self):
        return True

# Child class inheriting from Mammal
class Dog(Mammal):
    def speak(self):
        return f"{self.name} barks"

# Creating an instance of Dog
dog = Dog("Buddy")
print(dog.speak())  # Output: Buddy barks
print(dog.has_fur())  # Output: True
