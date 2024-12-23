def all_eq(lst):
    """Pads strings in a list to the length of the longest string.  Raises exceptions for invalid input.

    Args:
        lst: A list of strings.

    Returns:
        A new list with all strings padded to the same length (length of the longest string).
        Raises TypeError if input is not a list or contains non-string elements.
    """
    if not isinstance(lst, list):
        raise TypeError("Input must be a list.")
    if not all(isinstance(s, str) for s in lst):
        raise TypeError("List must contain only strings.")
    max_len = max(len(s) for s in lst)
    return [s.ljust(max_len, '_') for s in lst]

strings = ["apple", "banana", "kiwi", "orange"]
padded_strings = all_eq(strings)
print(padded_strings)

try:
    print(all_eq([1,2,3])) 
except TypeError as e:
    print(f"Error: {e}")
try:
    print(all_eq(["a","b", 1]))
except TypeError as e:
    print(f"Error: {e}")