# Error Handling
while True:
    try:
        age = int(input('what is your age?'))
        10/age
        raise ValueError('stop this program')
    # except ValueError:
    #     print('Please enter a number')
    except ZeroDivisionError:
        print('Please enter a number higher than 0')
    else:
        print('Thank you!')
        break
    finally:
        print('okay, I am finally done')

def sum(num1, num2):
    try:
        return num1/num2
    except (TypeError, ZeroDivisionError) as err:
        print(f'please enter a number{err}')

print(sum(2,0))