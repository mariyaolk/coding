def merge_coordinates(x_coords, y_coords):
    if len(x_coords) != len(y_coords):
        raise ValueError("Длины массивов должны быть одинаковыми")
    points = [(x, y) for x, y in zip(x_coords, y_coords)]
    return points

x_coordinates = [1, 2, 3]
y_coordinates = [4, 5, 6]
result = merge_coordinates(x_coordinates, y_coordinates)
print(result)