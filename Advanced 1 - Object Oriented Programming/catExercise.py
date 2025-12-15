#Given the below class:
class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats
cat1 = Cat('Orion',5)
cat2 = Cat('Polaris', 31)
cat3 = Cat('Cosmo', 20)
#cat_list = [cat1, cat2, cat3]
# 2 Create a function that finds the oldest cat
def find_oldest_cat(*args):
    return max(args)
   #oldest = 0
    #for cat in cats:
     #   if cat.age > oldest:
      #      oldest = cat.age

print(f'Oldest cat is {find_oldest_cat(cat1.age, cat2.age, cat3.age)} years old.')

# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2