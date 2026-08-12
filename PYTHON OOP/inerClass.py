# An inner class is a class defined inside another class. The inner class can access the properties and methods of the outer class.
# Inner classes are useful for grouping classes that are only used in one place, making your code more organized.
class Outer:
  def __init__(self):
    self.name = "Outer Class"

  class Inner:
    def __init__(self):
      self.name = "Inner Class"

    def display(self):
      print("This is the inner class")

outer = Outer()
print(outer.name) 