##
price=59
txt =f"The price is {price} dollars "
print(txt)
##
thislist= ["apple","banana","cherry"]
del thislist[0]
print(thislist)

##list comprehension
#show words with letter a
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist) 

#List objects have a sort() method that will sort the list alphanumerically, ascending, by default:

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)