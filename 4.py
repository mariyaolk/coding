def useless(s):
  """
  Finds the largest number in a list and divides it by the list's length.

  Args:
    s: A list of numbers.

  Returns:
    The largest number in the list divided by the list's length.
  """
  if not s:
    raise ValueError("List cannot be empty")
  if not all(isinstance(x, (int, float)) for x in s):
      raise ValueError("List must contain only numbers")

  return max(s) / len(s)
print(useless([1, 2, 3, 4, 5])) 
print(useless([10, 5, 20, 15])) 