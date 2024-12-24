def total_volume(boxes):
    total = 0
    for box in boxes:
        a, b, h = box
        volume = a * b * h
        total += volume
    return total

boxes = [(2, 3, 4), (1, 1, 1), (5, 5, 5)] 
print("Общий объем коробок:", total_volume(boxes)) 