print()
mylist = ["apple", "banana", "cherry"]

print(mylist[1])
print()
# List

# Lists are used to store multiple items in a single variable.
# Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.
# Lists are created using square brackets:

thislist = ["apple", "banana", "cherry"]
print(thislist)
print()

# Ordered

# When we say that lists are ordered, it means that the items have a defined order, and that order will not change.
# If you add new items to a list, the new items will be placed at the end of the list.

# Changeable

# The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.


# Allow Duplicates

# Since lists are indexed, lists can have items with the same value:

thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)
print()

# List Length

# To determine how many items a list has, use the len() function:


thislist = ["apple", "banana", "cherry"]
print(len(thislist))

print()

# List Items - Data Types
# List items can be of any data type:

list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
print()

# A list can contain different data types:

list1 = ["abc", 34, True, 40, "male"]
print(list1)
print()

# type()
# From Python's perspective, lists are defined as objects with the data type 'list':
mylist = ["apple", "banana", "cherry"]
print(type(mylist))
print()

# The list() Constructor
# It is also possible to use the list() constructor when creating a new list.


thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)
print()


# Python Collections (Arrays)
# There are four collection data types in the Python programming language:

# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.

# Access Items
# List items are indexed and you can access them by referring to the index number:

thislist = ["apple", "banana", "cherry"]
print(thislist[1])
print()

# Negative Indexing
# Negative indexing means start from the end

# -1 refers to the last item, -2 refers to the second last item etc.

thislist = ["apple", "banana", "cherry"]
print(thislist[-1])
print()

# Range of Indexes
# You can specify a range of indexes by specifying where to start and where to end the range.

# When specifying a range, the return value will be a new list with the specified items.


thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
print()


# By leaving out the start value, the range will start at the first item:
# This example returns the items from the beginning to, but NOT including, "kiwi":

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])
print()

# By leaving out the end value, the range will go on to the end of the list:
# This example returns the items from "cherry" to the end:

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])
print()

# Range of Negative Indexes
# Specify negative indexes if you want to start the search from the end of the list:
# This example returns the items from "orange" (-4) to, but NOT including "mango" (-1):

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])
print()

# Check if Item Exists
# To determine if a specified item is present in a list use the in keyword:

thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")
print()

# Change Item Value
# To change the value of a specific item, refer to the index number:

thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)
print()


# Change a Range of Item Values
# To change the value of items within a specific range, define a list with the new values, and refer to the range of index numbers where you want to insert the new values:

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)
print()

# If you insert more items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly:

thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)
print()

# If you insert less items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly:

thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)
print()

# Insert Items
# To insert a new list item, without replacing any of the existing values, we can use the insert() method.

# The insert() method inserts an item at the specified index:

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)
print()

# Append Items
# To add an item to the end of the list, use the append() method:

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)
print()

# Insert Items
# To insert a list item at a specified index, use the insert() method.

# The insert() method inserts an item at the specified index:

thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)
print()

# Extend List
# To append elements from another list to the current list, use the extend() method.

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)
print()

# Add Any Iterable
# The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).

thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)
print()



# Remove Specified Item
# The remove() method removes the specified item.

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)
print()

# If there are more than one item with the specified value, the remove() method removes the first occurrence:
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)
print()

# Remove Specified Index
# The pop() method removes the specified index.

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)
print()

# If you do not specify the index, the pop() method removes the last item.

thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)
print()

# The del keyword also removes the specified index:

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)
print()

# The del keyword can also delete the list completely.
thislist = ["apple", "banana", "cherry"]
del thislist
print()

# Clear the List
# The clear() method empties the list.

# The list still remains, but it has no content.

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)
print()

# Loop Through a List
# You can loop through the list items by using a for loop:

thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)
print()
  
fruitList = ["banana", "mango", "cherry"]
for i in fruitList:
    print(i)
print()

# Loop Through the Index Numbers
# You can also loop through the list items by referring to their index number.

# Use the range() and len() functions to create a suitable iterable.

thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])
  
print()

# Using a While Loop
# You can loop through the list items by using a while loop.

# Use the len() function to determine the length of the list, then start at 0 and loop your way through the list items by referring to their indexes.

# Remember to increase the index by 1 after each iteration.

thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
    print(thislist[i])
    i = i+1


print()

# Looping Using List Comprehension
# List Comprehension offers the shortest syntax for looping through lists:

# A short hand for loop that will print all items in a list:

thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]
print()

# List Comprehension
# List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.

# Example:

# Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.

# Without list comprehension you will have to write a for statement with a conditional test inside:

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)
print()

# With list comprehension you can do all that with only one line of code:

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)

print()

items= ["joystick",'Processor', "case", "mouse"]

shopList = [i for i in items if "o" in i]

print(shopList)
print()

# The Syntax
# newlist = [expression for item in iterable if condition == True]

# The return value is a new list, leaving the old list unchanged.

# Condition
# The condition is like a filter that only accepts the items that valuate to True.

newlist = [x for x in fruits if x != "apple"]
print(newlist)
print()\
    
#The condition if x != "apple"  will return True for all elements other than "apple", making the new list contain all fruits except "apple".

# The condition is optional and can be omitted:

newlist = [x for x in fruits]
print(newlist)
print()

# Iterable
# The iterable can be any iterable object, like a list, tuple, set etc.
# You can use the range() function to create an iterable:

newlist = [x for x in range(10)]
print(newlist)
print()

# Expression
# The expression is the current item in the iteration, but it is also the outcome, which you can manipulate before it ends up like a list item in the new list:

newlist = [x.upper() for x in fruits]
print(newlist)
print()

newlist = ['hello' for x in fruits]
print(newlist)
print()

# The expression can also contain conditions, not like a filter, but as a way to manipulate the outcome:

newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)
print()


# Sort List Alphanumerically
# List objects have a sort() method that will sort the list alphanumerically, ascending, by default:

# Sort List Alphanumerically
# List objects have a sort() method that will sort the list alphanumerically, ascending, by default:

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)
print( )

