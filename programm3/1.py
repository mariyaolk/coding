def dislike_6(a):
    if a == 6 and isinstance(a, (int, float)):
        return "Только не 6"
    return True

print(dislike_6(5))      
print(dislike_6(6))     
print(dislike_6(6.0))    
print(dislike_6("6"))     
print(dislike_6([6]))     
