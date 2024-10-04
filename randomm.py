import random
import numpy as np
#you can import any module as "x" and then use that x instead
# of its full name

num = random.randint(1, 10)
# where 1 to 10 is the range
print(num)  

a = random.normalvariate(0,1)
print(a)

# 1 element can be picked twice in this
mylist = list("ABCDEFGH")
b = [random.choice(mylist) for _ in range(4)]
# this implies it will randomly pick 4 digits from the given list

# if you want all unique elements
mylist2 = list("ABCDEF")
c = random.sample(mylist2, 3)

print(b)
print(c)

random.shuffle(mylist)
print(mylist)

d = np.random.rand(3)
print(d)
