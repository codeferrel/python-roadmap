#Tuples are used to store multiple items in a single variable.
#loop tuple
thistuple=("apple","banana","cherry")
for i in thistuple:
  print(i)

#access tuple
thistuples = ("apple", "banana", "cherry")
print(thistuples[1])

#update tuple
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x) 