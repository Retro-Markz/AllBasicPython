# Tuples are used to store multiple items in a single variable.
#A tuple is a collection which is ordered and unchangeable.


print()
thistuple = ("apple", "banana", "cherry")
print(thistuple)
print()

# When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.


# Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.

# Since tuples are indexed, they can have items with the same value:

thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

# Tuple Length
# To determine how many items a tuple has, use the len() function:

thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

print()

# Create Tuple With One Item
# To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.


thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

