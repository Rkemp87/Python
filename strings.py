days_of_study = 5
goal_days_of_study = 100
print(type(days_of_study))
print(type(str(days_of_study)))

this_is_a_basic_string = "This is a basic string"
print(this_is_a_basic_string)

this_is_a_long_format_string = '''
This
is
a
long
formatted
string'''

print(this_is_a_long_format_string)

this_is_a_formatted_string = f'I have been studying for {days_of_study} days'
print(this_is_a_formatted_string)

this_is_a_formatted_type_string = 'I have been studying for {} days'

## This is for python 2 but it's good to know!
print(this_is_a_formatted_type_string.format('45'))
print(this_is_a_formatted_type_string.format(days_of_study))

lets_change_the_order = 'My goal is study for {1} days. My current streak is {0}.'
print(lets_change_the_order.format(days_of_study, goal_days_of_study))

lets_change_the_order = 'My goal is study for {new_goal_days_of_study} days. My current streak is {new_days_of_study}.'
print(lets_change_the_order.format(new_days_of_study = 6, new_goal_days_of_study = 105))