#Unpacking Tuples, Lists, Dictionary.

def unpacker(a,b,c):
    print(a,b,c)

mylist = [1,2,3]
unpacker(*mylist)

mytuple = ("d", "e", "f")
unpacker(*mytuple)

mydict = {"a":10, "b":20, "c":30}  #use the parameters as key
unpacker(**mydict)

# We saw *args take tuple arguments and **kwargs take dict argument, we
# can unpack tuple and list using * and dict using **