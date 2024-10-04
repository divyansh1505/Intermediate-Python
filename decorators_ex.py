# A decorator is essentially a function that takes another function 
# as an argument, extends its behavior, and returns a new function. 
# This allows you to "wrap" an existing function in additional 
# functionality.

n = input("Enter your name : ")

def start_end_decorator(func):

    def wrapper(*args, **kwargs):
        print("Start")
        func(*args, **kwargs)
        print("End")
    return wrapper

@start_end_decorator
def print_name(name):
    print(name)

print_name(n)


class CountCalls:

    def __init__(self, func):
        self.func = func
        self.num_calls = 0 

    def __call__(self, *args, **kwargs):
        self.num_calls +=1
        print (f"This is executed {self.num_calls} times")
        return self.func(*args, **kwargs)
        

@CountCalls
def say_hello():
    print("Hello")
# When you decorate a function like this, it essentially does this 
# behind the scenes:
# say_hello = CountCalls(say_hello)


say_hello()
say_hello()
