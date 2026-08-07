# Python Encapsulation

# Encapsulation is about protecting data inside a class.

# It means keeping data (properties) and methods together in a class, while controlling how the data can be accessed from outside the class.

# This prevents accidental changes to your data and hides the internal details of how your class works.

# Create a private class property named __age:


class Person:
    def __init__(self,name,age):
        self.name=name
        self.__age=age  # Private property

        p1 =Person ("CodeF" ,"21")
        print(p1.name)
        print(p1.__age)

        pass