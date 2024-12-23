def has_adjacent_duplicates(word):
    for i in range(len(word) - 1):
        if word[i] == word[i + 1]:
            return True
    return False

print(has_adjacent_duplicates("привет"))  
print(has_adjacent_duplicates("колонна"))  
print(has_adjacent_duplicates("кооператив"))  