# Python Sets

myset = {"apple", "banana", "cherry"}

# Set
# Sets are used to store multiple items in a single variable.

# Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.

# A set is a collection which is unordered, unchangeable*, and unindexed.

# * Note: Set items are unchangeable, but you can remove items and add new items.

# Sets are written with curly brackets.

thisset = {"apple", "banana", "cherry"}
print(thisset)

print()
# Note: Sets are unordered, so you cannot be sure in which order the items will appe

# Set items are unordered, unchangeable, and do not allow duplicate values.

# Unordered means that the items in a set do not have a defined order.

# Set items can appear in a different order every time you use them, and cannot be referred to by index or key.

# Set items are unchangeable, meaning that we cannot change the items after the set has been created.



# Duplicate values will be ignored:


thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)

print()
# Note: The values True and 1 are considered the same value in sets, and are treated as duplicates:

thisset = {"apple", "banana", "cherry", True, 1, 2}

print(thisset)

print()


# False and 0 is considered the same value:

thisset = {"apple", "banana", "cherry", False, True, 0}

print(thisset)

print()

# Get the Length of a Set
# To determine how many items a set has, use the len() function.


thisset = {"apple", "banana", "cherry"}

print(len(thisset))


print()

# Set items can be of any data type:

# String, int and boolean data types:

set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

# A set can contain different data types:

set1 = {"abc", 34, True, 40, "male"}

# From Python's perspective, sets are defined as objects with the data type 'set':


myset = {"apple", "banana", "cherry"}
print(type(myset))

print()

# It is also possible to use the set() constructor to make a set.

thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)

print()

# You cannot access items in a set by referring to an index or a key.

# But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword.

thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)
  
print()

# Check if "banana" is present in the set:

thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)

print()

# Check if "banana" is NOT present in the set:

thisset = {"apple", "banana", "cherry"}

print("banana" not in thisset)

print()

# To add one item to a set use the add() method.

thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)

print()

# To add items from another set into the current set, use the update() method.

# Add elements from tropical into thisset:

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)

print()

# The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.).


thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)

print()

# To remove an item in a set, use the remove(), or the discard() method.

thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)

print()

# Remove "banana" by using the discard() method:

thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)

print()

# You can also use the pop() method to remove an item, but this method will remove a random item, so you cannot be sure what item that gets removed.

# The return value of the pop() method is the removed item.


thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x)

print(thisset)

print()

# Note: Sets are unordered, so when using the pop() method, you do not know which item that gets removed.

thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)

print()

# The del keyword will delete the set completely:

# thisset = {"apple", "banana", "cherry"}

# del thisset

# print(thisset)

print()

# You can loop through the set items by using a for loop:

thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

print()

# Join Sets

# There are several ways to join two or more sets in Python.

# The union() and update() methods joins all items from both sets.

# The intersection() method keeps ONLY the duplicates.

# The difference() method keeps the items from the first set that are not in the other set(s).

# The symmetric_difference() method keeps all items EXCEPT the duplicates.

# Join set1 and set2 into a new set:


set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

print()

# You can use the | operator instead of the union() method, and you will get the same result.

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1 | set2
print(set3)

print()

# Join multiple sets with the union() method:

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1.union(set2, set3, set4)
print(myset)

print()

# Use | to join two sets:

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1 | set2 | set3 |set4
print(myset)
    
print()

# The union() method allows you to join a set with other data types, like lists or tuples.

# The result will be a set.

x = {"a", "b", "c"}
y = (1, 2, 3)

z = x.union(y)
print(z)

# The update() method inserts the items in set2 into set1:

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)

print()

# Note: Both union() and update() will exclude any duplicate items.

# The intersection() method will return a new set, that only contains the items that are present in both sets.

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2)
print(set3)

print()


# You can use the & operator instead of the intersection() method, and you will get the same result.

# Use & to join two sets:

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 & set2
print(set3)

print()

# Note: The & operator only allows you to join sets with sets, and not with other data types like you can with the intersection() method.

# Keep the items that exist in both set1, and set2:

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.intersection_update(set2)

print(set1)

print()

# Join sets that contains the values True, False, 1, and 0, and see what is considered as duplicates:

set1 = {"apple", 1,  "banana", 0, "cherry"}
set2 = {False, "google", 1, "apple", 2, True}

set3 = set1.intersection(set2)

print(set3)

print()

# The difference() method will return a new set that will contain only the items from the first set that are not present in the other set.

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.difference(set2)

print(set3)

print()

# Use - to join two sets:

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 - set2
print(set3)

print()



