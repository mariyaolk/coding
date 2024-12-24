def count_it(sequence):
    count_dict = {}
    for char in sequence:
        if char.isdigit(): 
            if char in count_dict:
                count_dict[char] += 1
            else:
                count_dict[char] = 1
    sorted_count = sorted(count_dict.items(), key=lambda item: item[1], reverse=True)
    top_three = dict(sorted_count[:3])
    
    return top_three
sequence = "123123312345678901234511223344556679"
result = count_it(sequence)
print(result)