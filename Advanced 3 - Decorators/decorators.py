#decorators
#@name - super charge our function
#wraps another function or enhances

#higher order function - HOC-
#could be a function that accepts another function
#a function that returns another function

#decorator pattern
from time import time

def my_decorator(func):
    def wrap_func(*args, **kwargs):
        print('************')
        func(*args, **kwargs)
        print('************')
    return wrap_func

@my_decorator
def hello(greeting, emoji=':('):
    print(greeting, emoji)

@my_decorator
def bye(greeting):
    print(greeting)
hello('ayo')
bye('later')

def performance(func):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print(f'took {t2 - t1} ms')
        return result
    return wrapper

@performance
def long_time():
    for i in range(1000000000):
        i*5

long_time()