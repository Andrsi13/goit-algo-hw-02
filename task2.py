from collections import deque

def check_palindrom(text):
    #Форматуємо текст прибираючи пробіли і приводимо до нижнього регістру
    organized_text = str(text).replace(" ", "").lower()
    #Додаємо в чергу
    char_deque = deque(organized_text)

    #перевіряємо чи є текст паліндромом
    while len(char_deque) > 1:
        if char_deque.popleft() != char_deque.pop():
            return print(f'{text} НЕ є паліндромом')
    return print(f'{text} є паліндромом')


check_palindrom("hello world")
check_palindrom("level")

