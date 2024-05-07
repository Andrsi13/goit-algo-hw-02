def are_brackets_balanced(text):
    stack = []
    # Визначаємо відповідність відкриваючих і закриваючих дужок
    brackets = {"(": ")", "{": "}", "[": "]"}
    opening_brackets = set(brackets.keys())
    closing_brackets = set(brackets.values())
    for char in text:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            # Перевіряємо, чи є відповідна відкриваюча дужка в стеку
            if not stack or brackets[stack.pop()] != char:
                return False
    # Перевіряємо, чи не залишилися непарні відкриваючі дужки
    return len(stack) == 0

# Приклад використання
input_str = "( ){[ 1 ]( 1 + 3 )( ){ }}"
if are_brackets_balanced(input_str):
    print(f"{input_str}: симетричні.")
else:
    print(f"{input_str}: не симетричні.")

