# shallow copy of immutables
org = 5
cpy = org
print(cpy)  # Output: 5

#deep copy of immutables
org1=5
cpy1=org1
cpy1=6
print(org1)  # Output: 5
print(cpy1)  # Output: 6

# shallow copy of mutables
org_list = [1, 2, 3]
cpy_list = org_list
cpy_list[0] = 10
print(org_list)  # Output: [10, 2, 3]
print(cpy_list)  # Output: [10, 2, 3]

# shallow copy: one level deep, only references of nested child objects
# deep copy: full independent copy of an object and all its nested objects
import copy
org_list1=[0,1,2,3,4]
# methods of deep copy (works for only 1 level deep)
# cpy_list1=copy.copy(org_list1)
# cpy_list1=list(org_list1)
cpy_list1=org_list1[:]

cpy_list1[0]=10
print(org_list1)  # Output: [0, 1, 2, 3, 4]
print(cpy_list1)  # Output: [10, 1, 2, 3, 4]

org_list2 = [1, 2, [3, 4], 5]
cpy_list2 = copy.deepcopy(org_list2)
cpy_list2[2][0] = 30
print(org_list2)  # Output: [1, 2, [3, 4], 5]
print(cpy_list2)  # Output: [1, 2, [30,,4], 5]

print("-----------------------------------------")

# example using classes
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Company:
    def __init__(self, boss, employee):
        self.boss = boss
        self.employee = employee

p1=Person("Alice", 45)
p2=Person("Bob", 30)

CompanyA=Company(p1,p2)
CompanyA_clone=copy.copy(CompanyA)
CompnayB=copy.deepcopy(CompanyA)

CompanyA_clone.boss.age=50
print(CompanyA.boss.age)  # Output: 50
print(CompanyA_clone.boss.age)  # Output: 50

CompnayB.boss.age=56
print(CompanyA.boss.age)  
print(CompnayB.boss.age) 