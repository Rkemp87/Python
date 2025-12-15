#defining default parameters
def say_hello(name = 'darth',age = 1000):
    print(f'Hello {name}, you are {age} years old')

#positional parameters/arguments
say_hello('rebecca', 38)

#keyword arguments
say_hello(age = 24, name = 'testing' )

#with default parameters
# functions typically should do one thing really well and should return something.
say_hello()

def first_sum(num1, num2):
    return num1 + num2

total = first_sum(10,5)
print(first_sum(4,5))
print(first_sum(10,total))

def another_sum(num1, num2):
    def another_func(n1, n2):
        return n1 + n2
        print('this will not actually print')
    print('this will print since it\'s above the return')
    return another_func(num1, num2)
    print('this will not actually print')

total = another_sum(10,20)
print(total)
#return auto exits the function

#methods vs functions
#methods are owned by something and what owns is it to the left
#you can build your own methods

# docstrings
def test(a):
    """
    Info: this function tests and prints param a
    """
    print(a)

test('!!!!')
help(test)
print(test.__doc__)


#clean code

def is_even(num):
    return num % 2 == 0

print(is_even(5))

# *args and **kwargs
#the * indicates it can take as many arguments as you want
# Rule: params, *args, default params, **kwargs

def super_func(*args):
    return sum(args)

print(super_func(1,2,3,4,5))

def another_super_func(*args, **kwargs):
    another_total = 0
    print(kwargs)
    for items in kwargs.values():
        another_total += items
    return sum(args) + another_total

print(another_super_func(1,2,3,4,5, num1=5, num2 =10))

# Scope - what variables do I have access to?
# if variable is not in a function it's global scope.
#1 - start with local (within function)
#2 - Parent Local
#3 - Global
#4 - built in python functions

a = 1
def parent():
    a = 10
    def confusion():
        return a
    return confusion()
print(parent())
print(a)

# parameters are considered local variables
#dependency injection
total = 0
def count(total):
    total += 1
    return total

print(count(count(count(total))))

##nonlocal is equal to parent local
def outer():
    x = 'local'
    def inner():
        nonlocal x
        x = 'nonlocal'
        print('inner:', x)
    inner()
    print('outer:', x)

outer()

# Why do we need scope? - machines don't have infinite cpu so scope
# helps to make sure your programs run efficiently