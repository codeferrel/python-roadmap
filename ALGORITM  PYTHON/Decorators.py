#By placing @changecase directly above the function definition, the function myfunction is being "decorated" with the changecase function.
# The function changecase is the decorator.
# The function myfunction is the function that gets decorated.
# Using the @changecase decorator on two functions:

def changecase(func):
    def myinner():
        return func().upper()
    return myinner

@changecase
def myfunction():
    return "Hello Mbappe"

@changecase
def otherfunction():
    return "I'm Kenjo Fernandes"


print(myfunction())
print(otherfunction())
print("\n")
###############################

def changecase(func):
    def myinner():
        return func().upper()
    return myinner

@changecase
def func2():
    return "HELLO 1"

@changecase
def func3():
    return "HELLO 2"

print(func2())
print(func3())