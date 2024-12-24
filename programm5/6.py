def cleaned_str(st):
    result = []
    
    for char in st:
        if char == '@':
            if result: 
                result.pop() 
        else:
            result.append(char)  
    
    return ''.join(result)  

print(cleaned_str("гр@оо@лк@оц@ва")) 
print(cleaned_str("аб@вг@д@")) 
print(cleaned_str("т@ест@стр@ока@"))  