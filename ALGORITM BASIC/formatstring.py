##
price=59
txt =f"The price is {price} dollars "
print(txt)
##
thislist= ["apple","banana","cherry"]
del thislist[0]
print(thislist)
##
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist) 