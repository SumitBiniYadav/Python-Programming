class Animal:
    def sound(self):  # Parent class method
        print("Animals make different sounds")

class Dog(Animal):
    def sound(self):  # Overriding the parent method
        print("Dog barks")

# Usage
a = Animal()
a.sound()  # Calls the parent class method

d = Dog()
d.sound()  # Calls the overridden method in Dog
