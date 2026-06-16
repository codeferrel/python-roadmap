#Dictionaries are used to store data values in key:value pairs.
thisdict={
    "brand ": "ford ",
    "model ":" mustang ",
    "year ":2026

}
print(thisdict)


#copy dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)

#access item ,Add a new item to the original dictionary, and see that the values list gets updated as well:
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()

print(x) #before the change

car["color"] = "red"

print(x)