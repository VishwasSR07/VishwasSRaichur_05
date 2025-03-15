# 25. Real-World OOP Example: Student Class
class Student:
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks
    
    def calculate_grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 75:
            return "B"
        elif self.marks >= 60:
            return "C"
        else:
            return "D"
    
    def display(self):
        print(f"Student: {self.name}, Age: {self.age}, Grade: {self.calculate_grade()}")
