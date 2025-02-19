# Parent class
class Animal:
    def speak(self):
        return "Animal speaks"

# Child class inheriting from Animal
class Dog(Animal):
    def bark(self):
        return "Dog barks"

# Create an instance of Dog
dog = Dog()
print(dog.speak())  # Inherited from Animal
print(dog.bark())   # Dog's own method
