#lambda expressions - one time anonymous functions
#that you don't need more than once

# lambda param: action(param) - automatically returns


from functools import reduce

my_list = [1,2,3,4,5,6,7,8,9,10]
your_list = [5,4,3]

print(list(map(lambda item: item**2, your_list)))

print(list(map(lambda item: item*3, my_list)))
print(list(filter(lambda item: item % 2 != 0, my_list)))
print(reduce(lambda acc, item: acc + item, my_list))

a = [(0,2), (4,3), (9,9), (10,-1)]
a.sort(key=lambda x: x[1])
print(a)