#Return an iterator from a tuple, and print each value:
mytuple=("apple","banana","cherry")
myit=iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

#Strings are also iterable objects, containing a sequence of characters:
myinit=("banana")
myin=iter(myinit)

print(next(myin))
print(next(myin))
print(next(myin))
print(next(myin))
print(next(myin))
print(next(myin))