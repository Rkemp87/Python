# Dictionary - way to organize data - unordered key value pair
dictionary = {
    'a': [1,2,3],
    'b': 2,
    'c': 'this is a string',
    'd': True
}

my_list = [{'a': [1,2,3],
            'b': 'hello',
            'x': True},
           {'a': [4,5,6],
            'b': 'world',
            'x': False}
           ]
print(dictionary['a'])
print(dictionary['a'] [1])
print(dictionary['b'])
print(dictionary['c'])
print(dictionary['d'])

print(my_list[1]['a'] [2])

#dictionary keys
dictionary_keys = {
    123: [1,2,3],
    'test': 20,
    'string': 'test'
}

print(dictionary_keys['string'])
print(dictionary_keys[123])
print(dictionary_keys['test'])

#keys have to be unique otherwise it will be override by the latest assignment

print(dictionary_keys.get('age')) # this will avoid the error and return none

user2 = dict(name='rebecca')
print(user2)

print(123 in dictionary_keys)
print('size' in dictionary_keys)

print('size' in dictionary_keys.keys())
print('size' in dictionary_keys.values())

print(dictionary_keys.items())

user3 = user2.copy()
##dictionary_keys.clear()
##print(user2.clear())
print(user2)
print(user3)

print(dictionary_keys)
print(dictionary_keys.pop(123))
print(dictionary_keys)
print(dictionary_keys.popitem())
print(dictionary_keys)
print(dictionary_keys.update({'tests': 55}))
print(dictionary_keys)