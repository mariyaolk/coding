def encode_string(input_string):
    replacements = {
        'а': '4',
        'е': '3',
        'и': '1',
        'о': '0',
        'и': '1',
        ' ': ' '
    }

    encoded_string = ""
    
    for char in input_string:
        if char in replacements:
            encoded_string += replacements[char]
        else:
            encoded_string += 'з' + char
    
    return encoded_string

input_str = "Привет, как дела?"
encoded_str = encode_string(input_str)
print(encoded_str)