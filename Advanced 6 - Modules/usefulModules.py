from collections import Counter, defaultdict, OrderedDict # count objects, defaultdict # allows you to create a default value, OrderedDict # keeps the order that the dictionary is added
from datetime import time, date
from array import array

arr = array('i', [1,2,3])

print(arr[0])

print(time(5,45,3))
print(date.today())

li = [1,2,3,4,5,6,5]

print(Counter(li))

dictionary = defaultdict(lambda: 8, {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6})

print(dictionary['z'])

dictionary2 = OrderedDict()
dictionary2['a'] = 1
dictionary2['b'] = 2

d2 = OrderedDict()
d2['b'] = 2
d2['a'] = 2

print(d2 == dictionary2)

#With python 3.7 and newer you no longer need ordered dictionary as all dictionaries are now ordered by default
