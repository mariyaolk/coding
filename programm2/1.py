def to_float(num):
  """Converts a number to a floating-point number. Uses isinstance for type checking.

  Args:
    num: The number to convert.

  Returns:
    The floating-point representation of the number, or "Невозможно преобразовать" if conversion fails.
  """
  if isinstance(num, (int, float, str)):
    try:
      return float(num)
    except ValueError:
      return "Невозможно преобразовать"
  else:
    return "Невозможно преобразовать"

print(to_float(10))        
print(to_float(3.14))      
print(to_float("10"))       
print(to_float("3.14"))     
print(to_float("abc"))    
print(to_float([1, 2, 3])) 
