# shallow copy - one level deep, only references of nested child object 
# deep copy - full independent copy 

import copy 

org = [0,1,2,3,4]
cpy = copy.copy(org) #- works well when only one level deep 
# or u can use, cpy = list[org]
# or, cpy = org[:]
cpy[0] = -10
print(cpy)   #copy me index 0 will be modified to -10
print(org)   #this remains same

orrg = [[0,1,2,3,4], [5,6,7,8,9]]
cppy = copy.copy(orrg)
cppy[0][1] = -10
print(cppy)    #dono me changes aajate h, here we have to use
print(orrg)    #deep copy

orrg = [[0,1,2,3,4], [5,6,7,8,9]]
cppy = copy.deepcopy(orrg)
cppy[0][1] = -10
print(cppy)    #now isme changes h bs 
print(orrg)    #original remains unaffected