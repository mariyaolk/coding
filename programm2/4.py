import math

def sphere_radius(volume):
  """Calculates the radius of a sphere given its volume.

  Args:
    volume: The volume of the sphere in cubic units.

  Returns:
    The radius of the sphere in the same units. Returns an error message if the input is invalid.
  """
  if volume <= 0:
    return "Error: Volume must be a positive number."
  try:
    radius = (3 * volume / (4 * math.pi))**(1/3) 
    return radius
  except TypeError:
    return "Error: Invalid input type. Volume must be a number."


print(sphere_radius(100)) 
print(sphere_radius(-10)) 
print(sphere_radius("abc"))
