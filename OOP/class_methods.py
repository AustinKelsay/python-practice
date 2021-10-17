class BigObject:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # A class method is a method that is bound to the class rather than the object.
    # It is called on the class itself rather than an instance of the class.
    # Class methods are often used to define the behavior of the class,
    # cls works like self but instead of being bound to the instance, it is bound to the class.
    @classmethod
    def add(cls, x, y):
        return cls("Austin", x + y)

class_method = BigObject.add(1, 2)
print(class_method.name)