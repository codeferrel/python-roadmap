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

thisdict={
    "brand":"ford",
    "model":"mustang",
    "year ":2017
}

thisdict['year ']=2020
print(thisdict)