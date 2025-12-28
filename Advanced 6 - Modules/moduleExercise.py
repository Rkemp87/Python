import sys
from random import randint

random_number = randint(int(sys.argv[1]), int(sys.argv[2]))
print(random_number)

while True:
    guess = int(input('Guess a number between 1 and 10.'))
    if guess == random_number:
        print('Correct!')
        break
    else:
        print('Try again!')