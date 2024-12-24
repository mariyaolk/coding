def to_dict(lst):
    return {item: item for item in lst}

my_list = ['apple', 'banana', 'cherry']
result = to_dict(my_list)
print(result)