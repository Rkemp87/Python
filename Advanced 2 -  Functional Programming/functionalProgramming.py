#pure function
# 2 rules
#1 given the same input it will always return the same output
#2 a function should not produce any side effects
from functools import reduce

def multiply_by2(li):
    new_list = []
    for item in li:
        new_list.append(item * 2)
    return new_list

print(multiply_by2([5,10,15]))

# map, filter, zip and reduce

#map

#map(action, [data])

my_list = [1,2,3,4,5,6,7,8,9,10]
def multiply_by3(item):
    return item*3

print(list(map(multiply_by3, [5,10,15]))) #map creates an object so you need to turn it into a list to view it
print(list(map(multiply_by3, my_list))) # this doesn't change my list, it creates a new list
print(my_list) # this will be the same as the original my_list

#filter

def only_odd(num):
    return num % 2 != 0

print(list(filter(only_odd, [5,10,15])))
print(list(filter(only_odd, my_list)))
print(my_list)

#zip
your_list = [30,40,50,60]

print(list(zip(my_list, your_list)))

def accumulator(acc, item):
    print(acc, item)
    return acc + item

#reduce
print(reduce(accumulator, my_list, 0))
print(my_list)