def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

#Accessing individual arguments from *args:
def my_function(*args):
  print("Type:", type(args))
  print("First argument:", args[0])
  print("Second argument:", args[1])
  print("All arguments:", args)

my_function("Emil", "Tobias", "Linus") 



#Combining *args and **kwargs

def my_function(title, *args, **kwargs):
  print("title" , title)
  print("position arguments ",args)
  print("Keyboart argument ", kwargs)


  my_function("User info ", "CodeF ","Tobias ", age=25 , city ="Oslo")