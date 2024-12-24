def camel_case(st):
    result = []
    upper = True 
    for char in st:
        if char.isalpha():
            if upper:
                result.append(char.upper())
            else:
                result.append(char.lower())
            upper = not upper 
        else:
            result.append(char)
            
    return ''.join(result)

input_string = "топ 17 на всероссийских"
output_string = camel_case(input_string)
print(output_string)