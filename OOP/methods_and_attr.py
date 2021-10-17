class BigObject:
    # Class Object Attribute
    # This is a class obj attribute because it is hard coded in the class
    membership = True
    def __init__(self, name):
        # Class attribute's
        self.name = name
        self.data = []

    def shout(self):
        # You can refer to any Class Object Attributes in the class either with the self keyword which must be passed in or just the class name
        # If it is a dynamic attribute that gets instantiated at runtime you must use the self keyword
        print(self.membership)
        print(BigObject.membership)


# gives you information about the class
help(BigObject)