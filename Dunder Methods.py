# 15. Dunder Methods
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"Person(Name: {self.name}, Age: {self.age})"
    
    def __repr__(self):
        return f"Person('{self.name}', {self.age})"
