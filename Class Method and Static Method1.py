# 13. Class Method and Static Method
class Example:
    count = 0
    
    def __init__(self):
        Example.count += 1
    
    @classmethod
    def get_count(cls):
        return cls.count
    
    @staticmethod
    def static_method():
        print("This is a static method")
