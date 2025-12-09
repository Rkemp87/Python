#defining default parameters
def say_hello(name = 'darth',age = 1000):
    print(f'Hello {name}, you are {age} years old')

#positional parameters/arguments
say_hello('rebecca', 38)

#keyword arguments
say_hello(age = 24, name = 'testing' )

#with default parameters
# functions typically should do one thing really well and should return something.
say_hello()

def sum(num1, num2):
    return num1 + num2

total = sum(10,5)
print(sum(4,5))
print(sum(10,total))

def another_sum(num1, num2):
    def another_func(n1, n2):
        return n1 + n2
        print('this will not actually print')
    print('this will print since it\'s above the return')
    return another_func(num1, num2)
    print('this will not actually print')

total = another_sum(10,20)
print(total)
#return auto exits the function