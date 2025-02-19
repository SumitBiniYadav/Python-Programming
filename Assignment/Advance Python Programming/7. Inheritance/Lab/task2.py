# Parent class 1
class Father:
    def work(self):
        return "Father goes to work"

# Parent class 2
class Mother:
    def cook(self):
        return "Mother cooks food"

# Child class inheriting from both Father and Mother
class Child(Father, Mother):
    def play(self):
        return "Child plays games"

# Create an instance of Child
child = Child()
print(child.work())  # Inherited from Father
print(child.cook())  # Inherited from Mother
print(child.play())  # Child's own method
