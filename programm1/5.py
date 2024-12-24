def list_sort(lst):
  """Sorts a list of numbers by decreasing absolute value.

  Args:
    lst: A list of numbers.

  Returns:
    A new list sorted by decreasing absolute value.  Returns an empty list if the input is invalid.

  """
  if not isinstance(lst, list):
    return []
  if not all(isinstance(x, (int, float)) for x in lst):
      return []

  return sorted(lst, key=lambda x: abs(x), reverse=True)


print(list_sort([1, -5, 2, -3, 0, 4])) 
print(list_sort([1.5, -2.7, 0.8, -1.2])) 
print(list_sort("not a list")) 
print(list_sort([1,2,'a'])) 