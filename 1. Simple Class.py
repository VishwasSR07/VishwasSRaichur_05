# 1. Simple Class
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def display(self):
        print(f"Car: {self.brand} {self.model}")
