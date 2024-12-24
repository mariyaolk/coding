def multiply_numbers(num_str):
    numbers = num_str.split(', ')
    
    numbers = [float(num) for num in numbers]

    product = 1
    for num in numbers:
        product *= num
    
    return product

input_str = "2, 3.5, 4"
result = multiply_numbers(input_str)
print(f"Произведение чисел: {result}")