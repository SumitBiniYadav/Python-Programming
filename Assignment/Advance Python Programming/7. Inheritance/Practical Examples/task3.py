# Parent class
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return "Animal makes a sound"

# Another Parent class
class Pet:
    def is_pet(self):
        return True

# Child class inheriting from both Animal and Pet
class Dog(Animal, Pet):
    def speak(self):
        return f"{self.name} barks"

# Creating an instance of Dog
dog = Dog("Buddy")
print(dog.speak())  # Output: Buddy barks
print(dog.is_pet())  # Output: True