def counter(st):
    alphabet = 'abcdefghiklmnopqrstuvwxyz'
    sum = 0
    for letter in st:
        for i in range (len(alphabet)):
            if letter == alphabet[i]:
                sum += i+1
    return sum


print(counter('der')) 