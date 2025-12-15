#:=

a = 'hellooooooo'

if len(a) > 10:
    print(f'too long {len(a)} elements')

# can be rewritten to

if (n := len(a)) > 10:
    print(f'too long {n} elements')

while (n := len(a)) > 5:
    print(n)
    a = a[:-1]

print(a)
