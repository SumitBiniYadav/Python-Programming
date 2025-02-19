# Parent class
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return "Animal makes a sound"

# Child class 1 inheriting from Animal
class Dog(Animal):
    def speak(self):
        return f"{self.name} barks"

# Child class 2 inheriting from Animal
class Cat(Animal):
    def speak(self):
        return f"{self.name} meows"

# Creating instances of Dog and Cat
dog = Dog("Buddy")
cat = Cat("Whiskers")
print(dog.speak())  # Output: Buddy barks
print(cat.speak())  # Output: Whiskers meows