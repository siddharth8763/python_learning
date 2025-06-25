# # sort (inplace) and sorted (creates a new list)
# arr=[1,2,3,4,5]
# # arr.sort(reverse=True)
# print(arr)
# arr2=sorted(arr,reverse=True)
# print(arr2)

##############################################################################

# fill arrays with zeros
# arr = [0] * 5
# print(arr)

##############################################################################

##appendeing
# arr = [0] * 5
# print(arr)
# arr2=[1,1,1,1,1]
# print(arr+arr2)

##########################################################

#slicing
# arr=[1,2,3,4,5,6,7,8,9,10]
# print(arr[1::1])
# print(arr[1::])
# print(arr[::1])
# print(arr[::2])
# print(arr[2::])
# print(arr[2:8:3])
# print(arr[::-1])

#################################################

#deep copy and shallow copy
# arr=[1,2,3]
# arr1_deepcopy = arr.copy()
# arr1_deepcopy1 = list(arr)
# arr1_deepcopy2 = arr[:]
# arr1_shallowcopy = arr
# arr1_deepcopy.reverse()
# arr1_shallowcopy.reverse()
# print(arr1_deepcopy)    
# print(arr)
#print(arr1_deepcopy1)
#print(arr1_deepcopy2)

#################################################

# list comprehension
# arr = [1,2,3,4,5]
# squaredArray = [i*i for i in arr]
# print(arr)
# print(squaredArray)

##################################################

#unpacking

# arr=["delta","alpha","beta","gamma"]
# a,b,c,d=arr
# print(a)    
# print(b)
# print(c)
# print(d)

# tpl=("delta","alpha","beta","gamma")
# a,b,c,d=tpl
# print(a)
# print(b)
# print(c)
# print(d)

# tpl = ("delta", "alpha", "beta", "gamma","zetta")
# i1,*i2,i3 = tpl
# print(i1)
# print(i2)
# print(i3)

###############################################

# dict1={"a":1,"b":2,"c":3}
# dict2 = dict(a=4, b=5, c=6)
# print(dict1)
# print(dict2)
# #prior to python 3.6 it was removing any random key but in 3.6 it is removing the last key
# dict2.popitem()

#######################################################

# dict1={"a":1,"b":2,"c":3}
# for key, value in dict1.items():
#     print(key,value)

########################################################

# dict1={"a":1,"b":2,"c":3}
# dict2 = dict(a=4, b=5, c=6, d=7)
# dict1.update(dict2)
# print(dict1)
# print(dict2)

###########################################################

# myset = {}
# print(type(myset)) #dict

# myset = set()
# print(type(myset)) #set

############################################################

# all properties of a set and can not modify it
# a = frozenset({1, 2, 3})
# a.add(2)

##########################################################

# s = "Hellqwerty"
# print(s[0:])
# print(s[:1])
# print(s[0:len(s)])
# print(s[0:5:2])
# print(s[::-1])
# print(s[-5::-3])

##########################################################

# print("yes" if 'e' in "hello" else "no")

##########################################

# s = "Hello"
# print(s.find("el"))

############################################

# s="siddharth" 
# s1 = s.replace("idd","grok") 
# print(s)
# print(s1)

########################################

# s= "howdy mate, good day"
# print(s.split())
# sArr = s.split(" ")
# s1 = " ".join(sArr) 
# print(s1) 

##########################################

# name = "Siddharth"
# age = 27
# op = "My name is {} and my age is {}".format(name,age)
# op1 = f"my name is {name} and my age is {age}"
# print(op)
# print(op1)

###########################################

# from collections import Counter
# s = "siddharth"
# my_counter = Counter(s)
# print(my_counter) # returns a dictionary with the count of each character
# print(my_counter['s']) # returns the count of 's'
# print(my_counter.most_common(2)) # returns the most common 2 elements

################################################

# from collections import namedtuple
# Point = namedtuple('Point', ['x', 'y'])
# pt = Point(1, 2)
# print(pt.x)  # 1
# print(pt.y)  # 2

###########################################################

# from collections import defaultdict
# my_dict = defaultdict(int)
# my_dict['a'] = 1
# my_dict['b'] = 2
# print(my_dict['c'])  # prints 0, since 'c' is not in the dictionary

#############################################################

# from collections import deque
# my_deque = deque([1, 2, 3])
# print(my_deque)  # deque([1, 2, 3])
# my_deque.extendleft([4,5,6])
# print(my_deque)  # deque([6, 5, 4, 1, 2, 3])
# my_deque.rotate(1)  # rotate the deque to the right by 1
# print(my_deque)  # deque([3, 6, 5, 4, 1, 2])
# my_deque.rotate(-1) # rotate the deque to the left by 1

#############################################################

# from itertools import product
# a = [1, 2]
# b = [3, 4]
# prod = product(a, b)
# print(list(prod))  # [(1, 3), (1, 4), (2, 3), (2, 4)]

############################################################

# from itertools import permutations
# a = [1, 2, 3]
# print(list(permutations(a)))  # [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]
# print(list(permutations(a, 2)))  # [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]

# ##############################################################

# from itertools import combinations, combinations_with_replacement
# a = [1, 2, 3, 4]
# comb = combinations(a, 2)
# print(list(comb)) # repition not allowed in this case
# comb_wr= combinations_with_replacement(a, 2)
# print(list(comb_wr)) #repition eg(1,1) allowed in this case

######################################################################

# from itertools import accumulate
# a=[1, 2, 3, 4]
# acc=accumulate(a)
# print(a)
# print(list(acc)) #1st ele remains same then 1+2=3, 3+3=6, 6+4=10

#####################################################################

# from itertools import accumulate
# import operator
# a = [1, 2, 3, 4]
# acc=accumulate(a, func=operator.mul)
# print(a)
# print(list(acc)) # 1st ele remains same then 1*2=2, 2*3=6, 6*4=24

#####################################################################                                   

# from itertools import accumulate
# import operator
# a = [1, 2, 3, 4]
# acc=accumulate(a,func=max)
# print(a)
# print(list(acc)) # 1st ele remains same then max(1,2)=2, max(2,3)=3, max(3,4)=4

##########################################################

# from itertools import groupby
# def smaller_than_3(x): return x < 3
# a = [1, 2, 3, 4]
# group_obj=groupby(a, key=smaller_than_3)
# for key, value in group_obj:
#     print(key, list(value)) # prints the key and the values in that group

##############################################################

# from itertools import groupby
# persons = [{'name': 'Tim', 'age': 25}, {'name': 'Dan', 'age': 25},{'name': 'Lisa', 'age': 27}, {'name': 'Claire', 'age': 28}]
# group_obj=groupby(persons, key=lambda x: x['age'])
# for key, value in group_obj:
#     print(key, list(value)) # prints the age and the persons with that age

##################################################################3

# from itertools import count, cycle, repeat
# a=[1, 2, 3]
# for i in cycle(a):
#     print(i) #this will run indefinitely, printing 1, 2, 3 repeatedly

#####################################################################

# from itertools import count, cycle, repeat
# a = [1, 2, 3] 
# for i in repeat(a, 2):  # repeat the list 2 times
#     print(i)  # prints [1, 2, 3] twice

###################################################################


