# Base class
class Grandparent:
    def legacy(self):
        return "Grandparent's legacy"

# Intermediate class
class Parent(Grandparent):
    def wisdom(self):
        return "Parent's wisdom"

# Child class inheriting from Parent (which already inherits from Grandparent)
class Child(Parent):
    def fun(self):
        return "Child enjoys life"

# Create an instance of Child
child = Child()
print(child.legacy())  # Inherited from Grandparent
print(child.wisdom())  # Inherited from Parent
print(child.fun())     # Child's own method
