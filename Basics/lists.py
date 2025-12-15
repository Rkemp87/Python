matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
# expected to print out '2'
print(matrix[0][1])

basic_list = [1,2,3,4,5,6,7,8,9]
print(basic_list)
# List Methods
basic_list.append(100)
new_list = basic_list
print(basic_list.append(200))

basic_list.insert(4,1100)
print(basic_list)
print(new_list)

basic_list.extend([150])
print(basic_list)
print(new_list)

#removing

basic_list.pop()
print(basic_list)
print(new_list)

basic_list.pop()
print(basic_list)
print(new_list)

basic_list.pop(4)
print(basic_list)
print(new_list)

basic_list.remove(9)
print(basic_list)
print(new_list)

basic_list.clear()
print(basic_list)
print(new_list)
basic_list = [1,2,3,4,5,6,7,8,9]
print(basic_list.index(2))


# more list methods

new_methods = ['a','b', 'c', 'x','d','e','f']

print(new_methods.index('c', 0, 4))

print('x' in new_methods)
print('d' in new_methods)

print ('check' in 'this is me checking this')

print(new_methods.count('a'))
new_methods.append('a')

print(new_methods.count('a'))
new_methods.sort()
print(new_methods)

sorted(new_methods)
print(new_methods)
new_methods.reverse()
print(new_methods)
#sort keeps the array but sorted produces a new array

print(new_methods[: : -1])
print(new_methods)

print(list(range(1,100)))

print(list(range(2)))

new_sentence = ' '.join(['hi', 'my', 'name', 'is', 'rebecca'])

print(new_sentence)

#list unpacking

a,b,c, *other, d, e = [1,2,3,4,5,6,7,8]

print(a,b,c)
print(other)
print(d)
print(e)


# none type

weapons = None

