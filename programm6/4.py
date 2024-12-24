def remove_extra_spaces(input_string):
    words = input_string.strip().split()
    cleaned_string = ' '.join(words)
    return cleaned_string

test_string = "   Привет,    мир!  Как   дела?   "
result = remove_extra_spaces(test_string)
print(result)