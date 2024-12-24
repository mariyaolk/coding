def cumulative_sum(arr):
    result = []
    cumulative_total = 0
    
    for number in arr:
        cumulative_total += number
        result.append(cumulative_total)
    
    return result

input_list = [1, 2, 3, 4]
output_list = cumulative_sum(input_list)
print(output_list) 