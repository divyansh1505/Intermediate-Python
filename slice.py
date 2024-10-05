mylist = []

for i in range (100):  #means i goes from 1 to 99
    mylist.append(i)

print(mylist) 

print(mylist[1:10])  #prints items with index 0 to 9
print(mylist[1:10:2]) #prints items with index 0 to 9 with 2 ka gap

print(mylist[1:100:8])