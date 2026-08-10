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

##################################
# Use a getter method to access a private property:
class Person:
  def __init__(self, name, age):
    self.name = name
    self.__age = age

  def get_age(self):
    return self.__age

p1 = Person("Tobias", 25)
print(p1.get_age()) 


######################################
# Use a setter method to change a private property:
class Person:
  def __init__(self, name, age):
    self.name = name
    self.__age = age

  def get_age(self):
    return self.__age

  def set_age(self, age):
    if age > 0:
      self.__age = age
    else:
      print("Age must be positive")

p1 = Person("code", 21)
print(p1.get_age())

p1.set_age(22)
print(p1.get_age()) 