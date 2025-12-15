# goal is to have it print only the highest number.

def highest_even(li):
    highest_number = 0
    for number in li:
        if number % 2 == 0:
            if number > highest_number:
                highest_number = number
    return highest_number

print(highest_even([2,10,2,3,4,8,11]))