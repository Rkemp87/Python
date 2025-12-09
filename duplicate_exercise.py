#Exercise: Check for duplicates in list:
some_list = ['a','b','c','b','d','m','n','n']
duplicate_list = []
for letter in some_list:
    if some_list.count(letter) > 1:
        if letter not in duplicate_list:
            duplicate_list.append(letter)

print(duplicate_list)