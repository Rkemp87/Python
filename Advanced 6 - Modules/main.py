# import utility
from utility import multiply, divide
# import shopping.more_shopping.shopping_cart
# from shopping.more_shopping.shopping_cart import buy
from shopping.more_shopping import shopping_cart

# print(utility)
# print(shopping.more_shopping.shopping_cart.buy('apple'))
# print(buy('apple'))
print(shopping_cart.buy('apple'))
print(divide(5,2))

#This just makes sure that if this is the main file and not the exported file
#this will only run then
if __name__ == '__main__':
   print('please run this')

