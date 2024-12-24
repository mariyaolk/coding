def shortener(st):
    stack = []
    result = []
    
    for char in st:
        if char == '(':
            stack.append(len(result)) 
        elif char == ')':
            if stack:
                stack.pop()  
        else:
            if not stack:  
                result.append(char)
    
    return ''.join(result)


text = "я не люблю егора (но это не точно) и (всё ещё люблю (нет))."
cleaned_text = shortener(text)
print(cleaned_text)