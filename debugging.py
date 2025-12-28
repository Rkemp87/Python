#recommended ways to make debugging easier
#linting - detect as we code issues with our code
#ide/editor
#read errors
#pdb - python debugger - built in modules
import pdb

def add(num1, num2):
    pdb.set_trace()
    return num1 + num2

print(add(4, 'adaadda'))
