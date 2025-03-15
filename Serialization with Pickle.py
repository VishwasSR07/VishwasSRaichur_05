# 22. Serialization with Pickle
class Serializer:
    @staticmethod
    def serialize(obj, filename):
        with open(filename, 'wb') as file:
            pickle.dump(obj, file)
    
    @staticmethod
    def deserialize(filename):
        with open(filename, 'rb') as file:
            return pickle.load(file)
