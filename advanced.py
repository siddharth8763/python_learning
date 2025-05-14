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
