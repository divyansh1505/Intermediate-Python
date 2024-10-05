# 1. *args:
# This allows you to pass a variable number of non-keyword arguments to a function. 
# The *args syntax is used to pass a variable number of positional arguments to the 
# function, and these arguments are received as a tuple.

def my_function(*args):
    for arg in args:
        print(arg)

my_function(1, 2, 3, 4)

# 2. **kwargs:
# This allows you to pass a variable number of keyword arguments to a function. 
# The **kwargs syntax collects these keyword arguments into a dictionary.

def my_function(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

my_function(name="Divyansh", age=18, city="New Delhi")

# *args collects positional arguments as a tuple.
# **kwargs collects keyword arguments as a dictionary.

def exam(*kabootar, last):  #you can use any word *  lgake and it behaves like *args
    for arg in kabootar:
        print(arg)
    print (last)

exam(1,2,3,4, last=100)
