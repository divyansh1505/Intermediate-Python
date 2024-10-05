import copy

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Company:
    def __init__(self, boss, employee):
        self.boss = boss
        self.employee = employee

p1 = Person("Divyansh", 18)
p2 = Person("Arnavi", 19)

# p3 = p1
# p3.age = 20 
# print(p3.age)
# print(p1.age)    #BOTH GOT AFFECTED
#So make a shallow copy

p3 = copy.copy(p1)
p3.age = 20
print(p3.age)
print(p1.age)

com = Company(p2, p1)   #p2 becomes boss and p1 becomes employee
com_clone = copy.deepcopy(com)  #makes a deep copy

com_clone.boss.age = 21  #copy me boss ki age change krdi
print(com_clone.boss.age)
print(com.boss.age)