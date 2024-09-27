# Dictionary

# Dictionaries are used to store data values in key:value pairs.

# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

print()

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

# Dictionaries are written with curly brackets, and have keys and values:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

print()

# Dictionary items are ordered, changeable, and do not allow duplicates.

# Dictionary items are presented in key:value pairs, and can be referred to by using the key name.

# Print the "brand" value of the dictionary:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])

print()

# When we say that dictionaries are ordered, it means that the items have a defined order, and that order will not change.

# Unordered means that the items do not have a defined order, you cannot refer to an item by using an index.


#  Dictionaries are changeable, meaning that we can change, add or remove items after the dictionary has been created.


# Dictionaries cannot have two items with the same key:


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)

print()

# To determine how many items a dictionary has, use the len() function:

print(len(thisdict))

print()

# The values in dictionary items can be of any data type:

# String, int, boolean, and list data types:

thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}

print(type(thisdict))

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(type(thisdict))

print()

# It is also possible to use the dict() constructor to make a dictionary.

thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)


print()

# Accessing Items
# You can access the items of a dictionary by referring to its key name, inside square brackets:


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]

print(x)

# There is also a method called get() that will give you the same result:
x = thisdict.get("model")

print(x)

print()

# The keys() method will return a list of all the keys in the dictionary.

x = thisdict.keys()
    
print(x)

print()

# The list of the keys is a view of the dictionary, meaning that any changes done to the dictionary will be reflected in the keys list.

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()

print(x) #before the change

car["color"] = "white"

print(x) #after the change

# The values() method will return a list of all the values in the dictionary.

x = thisdict.values()

print(x)

# The list of the values is a view of the dictionary, meaning that any changes done to the dictionary will be reflected in the values list.

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()

print(x) #before the change

car["year"] = 2020

print(x) #after the change

print()

# Add a new item to the original dictionary, and see that the values list gets updated as well:

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()

print(x) #before the change

car["color"] = "red"

print(x) #after the change
print()

# The items() method will return each item in a dictionary, as tuples in a list.

# Get a list of the key:value pairs

x = thisdict.items()

print(x)

print()

# The returned list is a view of the items of the dictionary, meaning that any changes done to the dictionary will be reflected in the items list.


# Make a change in the original dictionary, and see that the items list gets updated as well:

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.items()

print(x) #before the change

car["year"] = 2020

print(x) #after the change

print()

# Add a new item to the original dictionary, and see that the items list gets updated as well:

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.items()

print(x) #before the change

car["color"] = "red"

print(x) #after the change

print()

# To determine if a specified key is present in a dictionary use the in keyword:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")
  
# You can change the value of a specific item by referring to its key name:
print()

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018

print(thisdict)

print()


# The update() method will update the dictionary with the items from the given argument.

# The argument must be a dictionary, or an iterable object with key:value pairs.


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})

print(thisdict)

print()
# Adding an item to the dictionary is done by using a new index key and assigning a value to it:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)

print()

# The update() method will update the dictionary with the items from a given argument. If the item does not exist, the item will be added.

# The argument must be a dictionary, or an iterable object with key:value pairs.

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"color": "red"})

print(thisdict)

print()

# There are several methods to remove items from a dictionary:

# The pop() method removes the item with the specified key name:


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)


print()

# The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)

print()

# The del keyword removes the item with the specified key name:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)

print()

# The del keyword can also delete the dictionary completely:

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# del thisdict
# print(thisdict) #this will cause an error because "thisdict" no longer exists.

# The clear() method empties the dictionary:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)
print()



# You can loop through a dictionary by using a for loop.

# When looping through a dictionary, the return value are the keys of the dictionary, but there are methods to return the values as well.

for x in thisdict:
  print(x)
  
print()

# Print all values in the dictionary, one by one:

for x in thisdict:
  print(thisdict[x])

print()

# You can also use the values() method to return values of a dictionary:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict.values():
  print(x)
  
print()

# You can use the keys() method to return the keys of a dictionary:
for x in thisdict.keys():
  print(x)
  
print()

# Loop through both keys and values, by using the items() method:

for x, y in thisdict.items():
  print(x, y)
  
print()


# You cannot copy a dictionary simply by typing dict2 = dict1, because: dict2 will only be a reference to dict1, and changes made in dict1 will automatically also be made in dict2.

# There are ways to make a copy, one way is to use the built-in Dictionary method copy().

# Make a copy of a dictionary with the copy() method:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)

# Another way to make a copy is to use the built-in function dict().
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict)

# A dictionary can contain dictionaries, this is called nested dictionaries.

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

print()

# Or, if you want to add three dictionaries into a new dictionary:



child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

print(myfamily)

print()

# To access items from a nested dictionary, you use the name of the dictionaries, starting with the outer dictionary:

print(myfamily["child2"]["name"])

# You can loop through a dictionary by using the items() method like this:

for x, obj in myfamily.items():
  print(x)

  for y in obj:
    print(y + ':', obj[y])
    
print()


