#Adding an item to the dictionary is done by using a new index key and assigning a value to it:
thisdict={
    "brand": "ford",
    "model": "mustang",
    "year ":2026
}
thisdict ["color"] ="black"
print(thisdict)

#Make a copy of a dictionary with the copy() method:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)

#Make a copy of a dictionary with the dict() function:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict) 

#change values
thisdict={
    "brand":"ford",
    "model":"mustang",
    "year ":2017
}

thisdict['year ']=2020
print(thisdict)


#Nested dictionary ,,,A dictionary can contain dictionaries, this is called nested dictionaries.
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
} 
print(myfamily)