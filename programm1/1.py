user_input = input("Введите элементы списка через запятую: ")
elements = [element.strip() for element in user_input.split(",")]
reversed_elements = elements[::-1]
print("Список в обратном порядке:")
print(reversed_elements)