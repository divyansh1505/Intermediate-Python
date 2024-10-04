try:
    a = 5/1
    b = a + '10'    #Here this will be invalid operation
except ZeroDivisionError as e:     
    print(e)
except TypeError as e:  #So this error will be generated
    print(e)
else:
    print("Everything is fine")
finally:
    print("Have a nice day")


try:
    a = 5/0         #Here this will be invalid operation
    b = a + '10'
except ZeroDivisionError as e:   #So this error will be generated
    print(e)
except TypeError as e:
    print(e)
else:
    print("Everything is fine")
finally:
    print("Have a nice day")

try:
    a = 5/1                 #Here both are good
    b = a + 10
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)
else:
    print("Everything is fine and working properly")  #Hence this will print
finally:
    print("Have a nice day")


#Finally is always printed

#How to raise your own exception?

class ValueTooHighError (Exception):
    pass 

class ValueTooSmallError (Exception):
    pass
    # def __init__(self, message, value):
    #     self.message = message
    #     self.value = value 

def test_value(x):
    if x > 100:
        raise ValueTooHighError('Value is too high')   
    if x < 5:
        raise ValueTooSmallError('Value is too small')
    
n = int(input("Enter a random number : "))
    
try:
    test_value(n)
except ValueTooHighError as e: 
    print(e)
except ValueTooSmallError as e:
    print(e)
else:
    print("Number is in perfect range")
    