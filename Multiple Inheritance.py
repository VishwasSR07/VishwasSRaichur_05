# 8. Multiple Inheritance
class Parent1:
    def func1(self):
        print("Function from Parent1")

class Parent2:
    def func2(self):
        print("Function from Parent2")

class Child(Parent1, Parent2):
    def func3(self):
        print("Function from Child")
