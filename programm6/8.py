import math

def distance(point_a, point_b):
    x1, y1 = point_a['x'], point_a['y']
    x2, y2 = point_b['x'], point_b['y']
    
    d = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    return round(d, 3)

point_a = {'x': 1, 'y': 2}
point_b = {'x': 4, 'y': 6}
result = distance(point_a, point_b)
print(result)  