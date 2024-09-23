myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

print(my_var)

#to print multiple variables, separate them with coma

print(myvar, MYVAR, _my_var, myvar2)

'''
#ilegal variable names
2myvar = "John"
my-var = "John"
my var = "John"
'''

#it can be defined the type of the variable at the moment of declaring it

x = 5
y = "John"
print(x)
print(y)

w = 4       # x is of type int
z = "Sally" # x is now of type str
print(z)

#Casting. to specify the data type of a variable, this can be done with casting.
a = str(3)    # x will be '3'
b = int(3)    # y will be 3
c = float(3)  # z will be 3.0

print(a,b,c)

#--------------------
#
#
#------SCOPE
#
#
#Global variables
#Global variables can be used by everyone, both inside of functions and outside.

m = "awesome"

def myfunc():
  print("Python is " + m)

myfunc()

#If you create a variable with the same name inside a function,
# this variable will be local, and can only be used inside the function.
# The global variable with the same name will remain as it was, global and with
# the original value.

f = "awesome"

def myfunc():
  f = "fantastic"
  print("Python is " + f)

myfunc()

print("Python is " + f)

#Normally, when you create a variable inside a function, that variable is local,
# and can only be used inside that function.
#To create a global variable inside a function,
# you can use the global keyword.

def myfunc():
  global g
  g = "fantastic"

myfunc()

print("Python is " + g)


#Also, use the global keyword if you want to change a global variable inside a function.
h = "awesome"

def myfunc():
  global h
  h = "fantastic"

myfunc()

print("Python is " + h)