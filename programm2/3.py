def mul_to_int(a, b):
    try:
        product = a * b
        if product % 1 == 0:
            return int(product)
        else:
            return float(product)
    except TypeError:
        return "Error: Inputs must be numbers."

print(mul_to_int(2, 3))      
print(mul_to_int(2.5, 2))     
print(mul_to_int(2.5, 2.2))   
print(mul_to_int(2, 3.0))     
print(mul_to_int(2.5, 2.0))  