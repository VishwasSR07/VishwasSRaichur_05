# 20. File Handling with OOP
class FileHandler:
    def __init__(self, filename):
        self.filename = filename
    
    def write_file(self, content):
        with open(self.filename, 'w') as file:
            file.write(content)
    
    def read_file(self):
        with open(self.filename, 'r') as file:
            return file.read()
