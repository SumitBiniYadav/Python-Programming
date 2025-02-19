# Base class
class Person:
    def info(self):
        return "This is a person"

# First derived class (Single Inheritance)
class Employee(Person):
    def job(self):
        return "Employee works"

# Second derived class (Multiple Inheritance)
class Student(Person):
    def study(self):
        return "Student studies"

# Derived from both Employee and Student (Multiple Inheritance)
class Intern(Employee, Student):
    def internship(self):
        return "Intern is learning"

# Create instance of Intern
intern = Intern()
print(intern.info())     # Inherited from Person
print(intern.job())      # Inherited from Employee
print(intern.study())    # Inherited from Student
print(intern.internship())  # Intern's own method
