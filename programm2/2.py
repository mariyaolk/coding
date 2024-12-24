def avg_5(a, b, c, d):
  """Calculates the average of four numbers and rounds to 5 decimal places. Includes error handling.

  Args:
    a, b, c, d: Four numbers.

  Returns:
    The average of the four numbers, rounded to 5 decimal places.
    Returns an error message if any of the inputs are not numbers.
  """
  try:
    average = (a + b + c + d) / 4
    return round(average, 5)
  except TypeError:
    return "Error: Inputs must be numbers."

print(avg_5(1, 2, 3, 4))    
print(avg_5(10, 20, 30, 40)) 
print(avg_5(1.1, 2.2, 3.3, 4.4)) 
print(avg_5(1, 2, "a", 4))  