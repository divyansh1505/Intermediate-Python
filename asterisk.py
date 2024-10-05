result = 5*6
print(result)  #30

result2 = 2**5
print(result2) #32

result3 = [4] * 5
print(result3) #[4, 4, 4, 4, 4]

def fxn (a,b,*args,**kwargs):
    print(a,b)
    for arg in args:
        print(arg)
    for key in kwargs:
        print(key, kwargs[key])

fxn(1,2,3,4,5, six=6, seven=7)

# 1 and 2 goes in parameter a and b
# 3,4,5 are taken as tuple and khol deta h *


# we already used asterisk in unpacking list, tuple and dict

mytuple = (1,2,3,4)
mytuple2 = (5,) #to create tuple with 1 element, use ","
myset = {6,7}
mydict = {"a":8, "b":9, "c":10}

mylist = [*mytuple, *mytuple2, *myset, *mydict]
#here mydict pr bs * lgega and it append the keys in mylist

print(mylist)

mydict1 = {"a":1, "b":2}
mydict2 = {"c":3, "d":4}

my_dict = {**mydict1, **mydict2}
print(my_dict)