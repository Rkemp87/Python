from operator import truediv

for item in 'Zero To Mastery':
    print(item)

print(f"Item is now {item}")

for item in [1,2,3,4,5]:
    print(item)

print(f"Item is now {item}")

for item in (1,4,7):
    for x in ['a','b','c']:
        print(item,x)

print(f"Item is now {item}")

for item in {1,2,3,'d'}:
    print(item)

print(f"Item is now {item}")

user = {
    'name' : 'Rebecca',
    'age' : 20,
    'can_swim': True
}

for key,value  in user.items():
    print(key,value)

for item in user.values():
    print(item)

for item in user.keys():
    print(item)
