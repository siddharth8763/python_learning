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

# add10=lambda x,y: x + y + 10 
# print(add10(5,2))

##################################################################

#lambda arguments: expression
# points2D = [(1, 2), (15, 1), (5, 1), (10, 4)]
# points2D_sorted_1 = sorted(points2D)
# points2D_sorted = sorted(points2D, key=lambda x: x[1])
# print(points2D)
# print(points2D_sorted_1) # sorted by the first element of each tuple. default
# print(points2D_sorted) # sorted by the second element of each tuple

########################################################################

# a=[1, 2, 3, 4, 5]
# b=map(lambda x: x*2, a)
# print(list(b))

# # same as 

# c=[ x + 2 for x in a] 
# print(c)

########################################################

# a = [1, 2, 3, 4, 5, 6]
# b=filter(lambda x: x % 2 == 0,a)
# print(list(b))

# # # same as

# c= [x for x in a if x%2==0]
# print(c)

################################################

# from functools import reduce
# a=[1, 2, 3, 4]
# product_a=reduce(lambda x,y: x*y, a)
# print(product_a)

#################################################

# x =-5
# if x < 0:
#     raise Exception('x should be positive')

################################################

# x = - 5
# assert (x>=0), 'x is not positive'

##################################################

# try:
#     a = 5 / 0
#     b = a + 4
# except ZeroDivisionError as e:
#     print(e)
# except TypeError as e:
#     print(e)
# else:
#     print('everything is fine')
# finally:
#     print('cleaning up...')

##################################################

# class ValueTooHighError (Exception):
#     pass

# def test_value(x):
#     if x > 100:
#         raise ValueTooHighError('value is too high')
# test_value (200)

# try:
#     test_value(200)
# except ValueTooHighError as e:
#     print(e)

#########################################################

# import logging
# logging.basicConfig(
# 	level=logging.DEBUG,
# 	format='%(asctime)s %(name)s %(levelname)s %(message)s',
# 	datefmt='%m/%d/%Y %I:%M:%S %p'
# )
# logging.debug('This is a debug message')
# logging.info('This is an info message')
# logging.warning('This is a warning message')
# logging.error('This is an error message')
# logging.critical('This is a critical message')

############################################################

#helper.py
# import logging
# logger=logging.getLogger(__name__)
# logger.info('hello from helper')

# import logging
# logging.basicConfig(
# 	level=logging.DEBUG,
# 	format='%(asctime)s %(name)s %(levelname)s %(message)s',
# 	datefmt='%m/%d/%Y %I:%M:%S %p'
# )
# from helper import logger
# logger.info('hello from main')

###########################################################################

# import logging
# logger=logging.getLogger(__name__)

# stream_h=logging.StreamHandler()
# file_h=logging.FileHandler('app.log')

# stream_h.setLevel(logging.WARNING)
# file_h.setLevel(logging.ERROR)

# formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
# stream_h.setFormatter(formatter)
# file_h.setFormatter(formatter)

# logger.addHandler(stream_h)
# logger.addHandler(file_h)

# logger.warning('This is a warning message')
# logger.error('This is an error message')

########################################################################


# import logging
# import traceback
# a = [1, 2, 3]
# try:
#     a[5]
# except IndexError as e:
#     # logging.error(e, exec_info=True)  # This will log the error with traceback. either this or the next line can be used
#     logging.error(traceback.format_exc())  # This will log the traceback as a string

#########################################################################

# import logging
# from logging.handlers import RotatingFileHandler
# logger=logging.getLogger(__name__)
# logger.setLevel(logging.INFO)
# #roll over after 266, and keep backup logs app.log.1, app.log.2, etc
# handler=RotatingFileHandler('app.log', maxBytes=2000, backupCount=5)
# logger.addHandler (handler)
# for _ in range(10000):
#     logger.info('Hello, world!')

#####################################################

# import logging
# import time
# from logging.handlers import TimedRotatingFileHandler
# logger=logging.getLogger(__name__)
# logger.setLevel(logging.INFO)
# handler=TimedRotatingFileHandler('timed_test.log', when='s', interval=5, backupCount=5)
# logger.addHandler(handler)
# for _ in range(6):
#     logger.info("Hello, world!")
#     time.sleep(5)

#####################################

# import json
# #serilization
# person = {"name": "John", "age": 30, "city": "New York", "hasChildren": False, "titles": ["engineer", "programmer"]}
# personJSON=json.dumps(person, indent=4, sort_keys=True)
# print(personJSON)

# #optional: writing to a file
# with open('person.json', 'w') as file:
#     json.dump(person, file,indent=4, sort_keys=True)

# #deserialization
# person_dict = json.loads(personJSON)
# print(person_dict)

# #optional: reading from a file
# with open('person.json', 'r') as file:
#     person_dict_from_file = json.load(file)
#     print(person_dict_from_file)

##############################################

# custom serialization with json
# import json
# class User:
#     def _init_(self, name, age):
#         self.name = name
#         self.age=age

# user=User ('Max', 27)

# def encode_user(o):
#     if isinstance(o, User):
#         return {'name': o.name, 'age': o.age, o._class_name_: True}
#     else:
#         raise TypeError('Object of type user is not serializable')

# userJSON = json.dumps(user,default=encode_user, indent=4)
# print(userJSON)

#################################################################
# import json
# from json import JSONEncoder

# class User:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# user = User('Max', 27)

# # custom serialization with JSONEncoder
# class UserEncoder(JSONEncoder):
#     def default(self, o):
#         if isinstance(o, User):
#             return {'name': o.name, 'age': o.age, o.__class__.__name__: True}
#         return JSONEncoder.default(self, o)

# userJSON = UserEncoder().encode(user)
# print(userJSON)

# # custom deserialization
# # using object_hook to decode JSON back to User object
# def decode_user(dct):
#     if User.__name__ in dct:
#         return User(name=dct['name'], age=dct['age'])
#     return dct

# user=json.loads(userJSON, object_hook=decode_user)
# print(user.name)

################################################################

# import random
# mylist=list("ABCDEFGH")
# #unique
# a=random.sample(mylist, 3)
# #duplicate
# b=random.sample(mylist, k=3)
# print(a)
# print(b)
# print(random.shuffle(mylist)) #shuffles the list in place

#####################################################

# import numpy as np
# a = np.random.randint(0,10, size=(3,4))
# print(a)

######################################################

#without decorators
# def start_end_decorator(func):
#     def wrapper():
#         print('Start')
#         func()
#         print('End')
#     return wrapper

# def print_name():
#     print('Alex')

# print_name=start_end_decorator(print_name)

# #with decorators
# @start_end_decorator
# def print_name1():
#     print('Alex')

# print_name()
# print_name1()

######################################################

# def start_end_decorator(func):
#     def wrapper(*args, **kwargs):
#         print('Start')
#         result=func(*args, **kwargs)
#         print('End')
#         return result
#     return wrapper

# @start_end_decorator
# def add5(x):
#     return x + 5

# result=add5(16)
# print(result)  # Output: 21

######################################################3

# import functools

# def start_end_decorator(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         print('Start')
#         result = func(*args, **kwargs)
#         print('End')
#         return result
#     return wrapper

# @start_end_decorator
# def add5(x):
#     return x + 5

# print(help(add5))  # This will show the original function's docstring and name
# print(add5.__name__)  # This will print 'add5'
# result = add5(16)
# print(result)  # Output: 21

##########################################################

# # decorator with arguments
# import functools
# def repeat(num_times):
#     def decorator_repeat(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kwargs):
#             for _ in range(num_times):
#                 result=func(*args, **kwargs)
#             return result
#         return wrapper
#     return decorator_repeat

# @repeat(num_times=4)
# def greet(name):
#     print(f'Hello {name}')
# greet('Alex')

###########################################################

# # class based decoraters
# class CountCalls:
#     def __init__(self, func):
#         self.func=func
#         self.num_calls=0

#     def __call__(self, *args, **kwargs):
#         self.num_calls += 1
#         print(f'This is executed (self.num_calls) times')
#         return self.func(*args, **kwargs)

# @CountCalls
# def say_hello():
#     print('Hello')

# say_hello()
# say_hello()    

################################################################ 
