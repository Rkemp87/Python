print(range(0, 100))

for number in range(1,101):
    print(number)

for id in range(0,100,2):
    print(id)

for _ in range(2):
    print(list(range(10)))

# enumerate prints index of each item

for i,char in enumerate('Helllooooo'):
    print(i,char)

for i,char in enumerate((1,2,3)):
    print(i,char)

for i,char in enumerate(list(range(100))):
    if char == 50:
        print(f'index of 50 is: {i}')

i = 0
while i < 50:
    print(i)
    i += 1
else:
    print('Done with all the work')

while True:
    response = input('say something:')
    if response == 'bye':
        break

# break works in both for and while loops - breaks out of current enclosing loop

#continue - continue on to the top of the loop

#pass - doesn't do anything- good place holder

my_list = [1,2,3]

for item in my_list:
    pass

i = 0
while i < len(my_list):
    print(i)
    i += 1
