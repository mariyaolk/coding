def search_substr(subst, st):
    subst_lower = subst.lower()
    st_lower = st.lower()
    
    if subst_lower in st_lower:
        return "Есть контакт!"
    else:
        return "Мимо"

result = search_substr("тест", "Это просто Тест строки")
print(result) 