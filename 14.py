def reverser(st):
    word = ''

    for i in range(len(st)-1,-1,-1):
        word += st[i]
    st = ''
    for letter in word:
        if letter.isupper():
            st += letter.lower()
        if letter.islower():
            st += letter.upper()
    return st

print(reverser('freeDOM'))