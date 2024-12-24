from collections import Counter

def top3(st):
    st = st.replace(' ', '')
    count = Counter(st)
    most_common = count.most_common(3)
    result = ', '.join(f"{char} — {num}" for char, num in most_common)
    return result

text = "Это пример строки для тестирования."
result = top3(text)
print(result)