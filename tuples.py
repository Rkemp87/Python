# Tuple - like lists but not immutable.

my_tuple = (1, 2, 3)
print(my_tuple[1])
print(5 in my_tuple)

#lists are in brackets but tuples are in braces
#tuples are valid keys in dictionaries

my_dictionary = {(1,2): 1, 'b': 2, 'c': 3}
print(my_dictionary[(1,2)])
new_tuple = my_tuple[1:3]
print(new_tuple)

x,y,z = (4,5,6)
print(x)

print(my_tuple.count(0))
print(my_tuple.index(3))
print(len(my_tuple))

