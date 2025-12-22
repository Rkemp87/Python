def fib(num):
    num1 = 0
    num2 = 1
    for i in range(num):
        yield num1
        temp = num1
        num1 = num2
        num2 = temp + num2

for x in fib(21):
    print(x)


# def fib2(num):
#     num1 = 0
#     num2 = 1
#     result =[]
#     for i in range(num):
#         result.append(num1)
#         temp = num1
#         num1 = num2
#         num2 = temp + num2
#     return result
#
# print(fib2(21))