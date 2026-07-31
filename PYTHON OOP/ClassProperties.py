# Properties are variables that belong to a class. They store data for each object created from the class.

# Create a class with properties:
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Emil", 36)

print(p1.name)
print(p1.age) 