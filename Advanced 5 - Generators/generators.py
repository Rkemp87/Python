# range(100)
# list(range(100))
from time import time
# def make_list(num):
#     result = []
#     for i in range(num):
#         result.append(i*2)
#
#     return result
#
# my_list = make_list(100)
# print(my_list)

#generators are iterable
#not all iterables are generators

def generator_function(num):
    for i in range(num):
        yield i #pauses the function and comes back to it

g = generator_function(100)
# for item in generator_function(1000):
#     print(item)
next(g)
next(g)
print(next(g))


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
    print('1')
    for i in range(10000000):
        i*5
@performance
def long_time2():
    print('2')
    for i in list(range(10000000)): # due to this being turned into a list it's going to take longer
        i*5

long_time()
long_time2()

# how a for loop works under the hood
def special_for(iterable):
    iterator = iter(iterable)
    while True:
        try:
            print(iterator)
            print(next(iterator))
        except StopIteration:
            break

special_for([1,2,3])

# how range works under the hood
class MyGen():
    current = 0
    def __init__(self, first, last):
        self.first = first
        self.last = last
    def __iter__(self):
        return self
    def __next__(self):
        if MyGen.current < self.last:
            num = MyGen.current
            MyGen.current += 1
            return num
        raise StopIteration
gen = MyGen(0,100)

for i in gen:
    print(i)

    

