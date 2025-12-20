#list, set, dictionary comprehensions

#my_list = [param for param in interable]
my_list = [char for char in 'hello']
# for char in 'hello':
#     my_list.append(char)
print(my_list)

my_list2 = [num for num in range(0,100)]
my_list3 = [num**2 for num in range(0,100)]
my_list4 = [num**2 for num in range(0,100) if num % 2 == 0]
print(my_list2)
print(my_list3)
print(my_list4)

#sets are the exact same thing as lists just change brackets to curly braces

#dictionary
simple_dict = {
    'a': 1,
    'b': 2,
    'c': 3
}
my_dict = {key:value**2 for key, value in simple_dict.items() if value % 2 == 0 }

new_dict = {num:num*2 for num in [1,2,3]}
print(simple_dict.items())
print(my_dict)
print(new_dict)
