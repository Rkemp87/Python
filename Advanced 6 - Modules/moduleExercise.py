import sys
import random

random_number = random.randint(sys.argv[1],sys.argv[2])
print(random_number)

while True:
    guess = int(input('Guess a number between 1 and 10.'))
    if guess == random_number:
        print('Correct!')
        break
    else:
        print('Try again!')