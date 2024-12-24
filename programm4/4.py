my_dict = {
    'first_key': 'first_value',
    'second_key': 'second_value',
    'third_key': 'third_value',
    'fourth_key': 'fourth_value',
    'fifth_key': 'fifth_value'
}
first_key = list(my_dict.keys())[0]
last_key = list(my_dict.keys())[-1]

my_dict[last_key], my_dict[first_key] = my_dict[first_key], my_dict[last_key]
second_key = list(my_dict.keys())[1]
del my_dict[second_key]
my_dict['new-key'] = 'new_value'

print(my_dict)