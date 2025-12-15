is_old = False
is_licensed = False

if is_old and is_licensed:
    print('You are old enough to drive and are licensed!')
elif is_old:
    print('You are old enough to drive but not licensed!')
elif is_licensed:
    print('You are licensed to drive!')
else:
    print('You are not old enough to drive!')
    print('check')

# Truthy and Falsy
print(bool('testing'))
print(bool(12))
print(bool(0))
print(bool(None))
print(bool(()))


#Ternary Operator

#condition_if_true if condition else condition_if_else
is_friend = True
can_message = "message allowed" if is_friend else "message denied"
is_user = True
print(can_message)

#Short Circuiting
print(is_friend and is_user)

if is_friend or is_user:
    print('one of the conditions were true')

# Logical Operators

#>
#<
#==
#>=
#<=
#!=
#and
#or
#not

print(not(1 == 1))
print(not(1 > 1))


#Logical Operator Exercise

is_magician = False
is_expert = True

#check if magician And expert: "you are a master magician

#check if magician but not expert: "at least you're getting there"

#check if you're not a magician: "You need magic powers"

if is_magician and is_expert:
   print("You are a master magician")
elif is_magician and not is_expert:
    print("At least you're getting there")
elif not is_magician:
    print("You need magic powers")

print(True == 1) #yes
print('' == 1)#no
print([] == 1)#no
print(10 == 10.0)#yes
print([] == []) #yes
print(False == 0) #yes
print('' == 0) # yes

# == checks for equality of value
# is checks for location in memory
checking_list = [1,3,5]
print(checking_list)
print(checking_list is [1,3,5])
print(checking_list == [1,3,5])
print(True is 1)
print('' is 1)
print([] is 1)
print(10 is 10.0)
print([] is [])
print(False is 0)
print('' is 0)
