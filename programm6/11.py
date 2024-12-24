def stonks(numbers):
    a = numbers[0]
    for i in range(1, len(numbers)):
        if a > numbers[i]:
            return 'Не возраставет'
        else:
            a = numbers[i]
    return 'Возрастает'

print(stonks([1, 2, 3, 4, 5]))
print(stonks([1, 2, 3, 4, 5,3]))
print(stonks([955, 2, 3, 4, ]))
print(stonks([-10,53,367346,34563463467347])) 