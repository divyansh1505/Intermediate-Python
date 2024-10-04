#intertools : product, permuations, combination, accumlate, groupby and infinite iterators 

from itertools import groupby 

def smaller_than_3(x):
    return x < 6 

a = [1,2,3,4,5,6,7,8,9,10]

grp_obj = groupby(a, key=smaller_than_3)
for key, value in grp_obj:
    print(key, list(value))

# output = True [1, 2, 3, 4, 5]
# False [6, 7, 8, 9, 10]

    
