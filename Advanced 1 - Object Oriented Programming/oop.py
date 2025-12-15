# Everything in python is an object
# Objects have methods
# We can create our own objects/data types with our own attributes or methods


class FirstObject:
    pass

obj1 = FirstObject() #instanciate
#print(type(obj1))

class PlayerCharacter:
    # Class Object Attribute - not dynamic applies to all objects
    membership = True

    #if you don't have attributes you want to assign you don't need to ue the init method
    def __init__(self, name, age): # dunder method - built into python
        if self.membership:
            self._name = name #attributes the _ means do not modify this
            self.age = age

    def shout(self): #example of abstraction since we don't really care how it actually is doing what it's doing
        print(f'my name is {self._name}')
        return 'done'

    @classmethod #decorator
    def adding_things(cls,num1, num2):
        return num1 + num2

    @staticmethod # we don't have access to the parameter of cls - we don't care about the state/attributes
    def adding_things2(num1, num2):
        return num1 + num2


player1 = PlayerCharacter('rebecca',38)
player2 = PlayerCharacter('joshua',34)
player2.attack = 50

#print(player1.adding_things(2,3))
#print(player1._name, player1.age)
#print(player2._name, player2.age)
#print(player1.shout())
#print(player2.shout())
#print(player2.attack)
#print(player1.membership)
#print(player2.membership)
# print(player1.attack) - This doesn't work because it's not a method for player 1

# 4 pillar of oop
#1 Encapsulation -  attributes - functions all encapsulated within class
#2 Abstraction - giving access to only what is necessary the rest is "hidden"
#_ next to an attribute it shouldn't be modified and it should be private
#3 Inheritance - new objects to take on properities of existing objects

class User:
   # def __init__(self, email):
     #   self.email = email
    def sign_in(self):
        print('logged in')

    def attack(self):
       print('do nothing')

class Wizard(User):
    def __init__(self, name, power): #email):
        #super().__init__(email) # with super you don't need to pass in self
        self.name = name
        self.power = power

    def attack(self):
        print(f'attacking with power of {self.power}')
        User.attack(self)
        print(f'attacking with name of {self.power}')

class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows
    def check_arrows(self):
        print(f'attacking with arrows: arrows left- {self.num_arrows}')

    def run(self):
        print('ran really fast!')
class HybridBorg(Wizard, Archer):
    def __init__(self, name, power, num_arrows):
        Archer.__init__(self, name, num_arrows)
        Wizard.__init__(self, name, power)
#isinstance(instance, Class
hb1 = HybridBorg('Joey', 50, 100)
print(hb1.run())
print(hb1.check_arrows())
print(hb1.attack())
print(hb1.sign_in())
#introspection - ability to determine type of object at runtime
wizard1 = Wizard('Merlin', 50)
#print(dir(wizard1)) # will give all methods and attributes wizard 1 has

#print(wizard1.email)
#print(isinstance(wizard1, User))
#print(isinstance(wizard1, object))
archer1 = Archer('Robin', 100)
# wizard1.attack()
#archer1.attack()

#wizard1.sign_in()
#archer1.sign_in()

#4 polymorphism - way in which object classes can share the
# same method name but act differently depending on what calls it
# example is the attack methods up above it prints something different

def player_attack(char):
    char.attack()

#player_attack(wizard1)
#player_attack(archer1)

#for char in [wizard1, archer1]:
#    char.attack()
#dunder methods
class Toy():
    def __init__(self, color, age):
        self.color = color
        self.age = age
        self.my_dict = {
            'name': 'yoyo',
            'has_pets': False
        }


# modifying a dunder method
    def __str__(self):
        return f'{self.color} {self.age}'

    def __del__(self):
        print('deleted!')

    def __call__(self):
        return 'yess??'

    def __getitem__(self, i):
        return self.my_dict[i]

action_figure = Toy('red', 0)
#print(action_figure.__str__())
#print(str(action_figure)) #only modified on the specific object
#print(str('action figure'))  #still works
#print(action_figure())
#print(action_figure['name'])
#del action_figure
#print(action_figure) # no longer available