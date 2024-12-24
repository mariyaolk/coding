def help_bool(letter):
  """Provides a description of a Boolean algebra property.

  Args:
    letter: A single-letter code representing the property:
            'к' - Коммутативность (Commutativity)
            'а' - Ассоциативность (Associativity)
            'д' - Дистрибутивность (Distributivity)
            'м' - Правило де Моргана (De Morgan's Law)

  Returns:
    A string describing the property, or an error message if the input is invalid.
  """
  letter = letter.lower()
  if letter == 'к':
    return "Коммутативность:  A ∧ B ≡ B ∧ A  и  A ∨ B ≡ B ∨ A  (Порядок операндов не важен)"
  elif letter == 'а':
    return "Ассоциативность: (A ∧ B) ∧ C ≡ A ∧ (B ∧ C)  и  (A ∨ B) ∨ C ≡ A ∨ (B ∨ C) (Порядок выполнения операций не важен)"
  elif letter == 'д':
    return "Дистрибутивность: A ∧ (B ∨ C) ≡ (A ∧ B) ∨ (A ∧ C)  и  A ∨ (B ∧ C) ≡ (A ∨ B) ∧ (A ∨ C) (Распределение одной операции над другой)"
  elif letter == 'м':
    return "Правило де Моргана: ¬(A ∧ B) ≡ ¬A ∨ ¬B  и  ¬(A ∨ B) ≡ ¬A ∧ ¬B (Инверсия конъюнкции и дизъюнкции)"
  else:
    return "Ошибка: Неверный символ.  Используйте 'к', 'а', 'д', или 'м'."

print(help_bool('к'))
print(help_bool('А'))
print(help_bool('д')) 
print(help_bool('м')) 
print(help_bool('x'))
