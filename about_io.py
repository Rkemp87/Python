#input/output

#built in function allows to open and write to files

# my_file = open('test.txt') #idea of a cursor - can only read once
#
# print(my_file.read()) #will print
# print(my_file.read()) #will do nothing
# my_file.seek(0) #moves the cursor back
# print(my_file.read()) #will print because cursor is moved back
# print(my_file.read()) #will do nothing
# my_file.seek(0) #moves the cursor back
# print(my_file.readline())
# print(my_file.readline()) #will move to the second line
# print(my_file.readline()) #will move to the third line
# my_file.seek(0) #moves the cursor back
# print(my_file.readlines()) #will print out a list of all the lines
#
# my_file.close() # you have to close this to be able to use it in another file
# print('closing file')

# with open("test.txt", mode='w' ) as my_file: #default param is mode='r'
#     print(my_file.read()) #this will error since we do only write
#
# with open("test.txt", mode='r+') as my_file: #this allows reading and writing
#     text = my_file.write('testing the writing function') #overwrites whatever is in there
#     print(text)
#
with open("test.txt", mode='a') as my_file: #append mode
     text = my_file.write(' testing the append function') #appending whatever is in there
     print(text) #each time you run this it will append so be careful

with open ('creating_file.txt', mode='r+') as new_file:
    text = new_file.write('testing the creating new file')
    print(text)
    new_file.seek(0)
    print(new_file.read())
