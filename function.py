def print_name(a,b,c):
    print(f"Name: {a}, {b}, {c}")


print_name("John", "Doe", "Smith")
# output: Name: John, Doe, Smith

print_name(c="Smith", a="John", b="Doe")
# output:  Name: John, Doe, Smith


print_name("Alice", c="Johnson", b="Marie")
# output: Name: Alice, Marie, Johnson


#print_name(b="Brown", a="Charlie", "Davis")
#error: positional argument follows keyword argument

#print_name("Eve", "Taylor", a="Williams")
#error: multiple values for argument 'a'

def default_name(a, b="DefaultB", c="DefaultC"):
    print(f"Name: {a}, {b}, {c}")

default_name("OnlyA")
# output: Name: OnlyA, DefaultB, DefaultC

# unlike js default parameters, python default parameters must be at the end

# def default_name_invalid(a="DefaultA", b, c="DefaultC"):
#     print(f"Name: {a}, {b}, {c}")

# error: non-default argument follows default argument


def foo(a,b,*args, **kwargs):
    print(f"a: {a}, b: {b}")
    print(f"args: {args}")
    print(f"kwargs: {kwargs}")
    print("----")
    
    for arg in args:
        print(f"arg: {arg}")
    
    for key in kwargs:
        print(f"key: {key}, value: {kwargs[key]}")

foo(1,2,3,4,5, name="Alice", age=30)


def bar(a,b,*,c,d):
    print(f"a: {a}, b: {b}, c: {c}, d: {d}")

bar(1,2,c=3,d=4)
# output: a: 1, b: 2, c: 3, d

def bar1(*args,last):
    print(f"args: {args}, last: {last}")

    for arg in args:
        print(f"arg: {arg}")

bar1(1,2,3,last=4)


def unpacking_example(a,b,c):
    print(f"a: {a}, b: {b}, c: {c}")

values = (10,20,30)
values_list = [1,2,3]
#parameter and arguments should match for dict unpacking
values_dict = {'a':100, 'b':200, 'c':300}
unpacking_example(*values)
unpacking_example(**values_dict)
unpacking_example(*values_list)
print("----------------------------------")


def global_local():
    x=number    
    #incorrect way to modify global variable 
    #number = 5
    print("number inside the function:", x)

def global_local1():
    global number
    x=number
    number = 5
    print("number inside the function:", x)    

number=10
global_local()
global_local1()
print("number outside the function:", number)

print("----------------------------------")

def hoola(x):
    x=5

varr_this=10
hoola(varr_this)
print("varr_this after hoola function:", varr_this)

def fool(a_list):
    a_list.append(4)

my_list=[1, 2, 3]
fool(my_list)
# here the list is modified because lists are mutable
print(my_list)

print("----------------------------------")

def fool1(a_list):
    a_list=[200, 300, 400]
    a_list.append(4)
    a_list[0]=-100

my_list1 = [1, 2, 3]
fool1(my_list1)
# the local variable will not affect the original list
print(my_list1)

print("----------------------------------")

def fool2(a_list):
    a_list+=[400, 500]

my_list2 = [10, 20, 30]
fool2(my_list2)
# the original list is modified because += modifies the list in place
print(my_list2)

print("----------------------------------")

def fool3(a_list):
    a_list=a_list+[400, 500]

my_list3 = [10, 20, 30]
fool3(my_list3)
# the original list is not modified because a_list is reassigned to a new list
print(my_list3)
