def mygenerator():
    yield 1
    yield 2 
    yield 3  

g = mygenerator()

for i in g:
    print(i)

def countdown(num):
   print("Starting.......")
   while num>0:
    yield num
    num -=1 

cd = countdown(4)

value = next(cd)
# The next(cd) function starts the generator and executes 
# the code inside the countdown() function until it reaches
# the first yield.
print(value)  #4

print(next(cd))  #3
print(next(cd))  #2
print(next(cd))  #1

# ek aur dala to it raises StopIteration

def squaremaker(x):
    while (x>0):
        yield x*x
        x -=1 

n = int(input("Enter any number : "))
square = squaremaker(n)

for i in range (1, n+1):
    print(next(square))


# Generator is more effiecient than return type functions,
# it takes less space

print("Moving on to Fibonacci Sequence")
f = int(input("Enter the limit : "))

# 0,1,1,2,3,5,8,13,21,34,55....
def fibonacci(limit):
    a, b = 0,1
    while a<limit:
        yield a
        a,b = b, a+b

fib = fibonacci(f)

for i in fib:
    print(i)
# See, you can write loop this way also gor generators

