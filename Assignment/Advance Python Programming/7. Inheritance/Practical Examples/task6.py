# Parent class
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return "Animal makes a sound"

# Another Parent class
class Pet:
    def __init__(self, name):
        super().__init__(name)
    
    def is_pet(self):
        return True

# Child class 1 inheriting from Animal
class Dog(Animal, Pet):
    def __init__(self, name):
        super().__init__(name)
    
    def speak(self):
        return f"{self.name} barks"

# Child class 2 inheriting from Animal
class Cat(Animal, Pet):
    def __init__(self, name):
        super().__init__(name)
    
    def speak(self):
        return f"{self.name} meows"

# Child class inheriting from Dog
class Puppy(Dog):
    def __init__(self, name):
        super().__init__(name)
    
    def speak(self):
        return f"{self.name} yaps"

# Creating instances of Dog, Cat, and Puppy
dog = Dog("Buddy")
cat = Cat("Whiskers")
puppy = Puppy("Charlie")
print(dog.speak())  # Output: Buddy barks
print(cat.speak())  # Output: Whiskers meows
print(puppy.speak())  # Output: Charlie yaps
print(puppy.is_pet())  # Output: True