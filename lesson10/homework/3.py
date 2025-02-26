"""
Написать функцию которая принимает строку в которой есть 
круглые скобки и возвращает True или False анализируя все ли скобки 
являются закрытыми и расставлены в правильном порядке.
Примеры:
    (()()) -> True
    (()()() -> False
    (hello(2)ver()(33)python) -> True
    (hello(2()ver(33)python)) -> True
    (hello(2()ver(33)python) -> False

"""


def is_valid(text: str, braces=('(', ')')) -> bool:
    opened, closed = braces
    stack = []

    if not text:
        raise ValueError("Строка не может быть пустой!")
    
    if not isinstance(text, str):
        raise TypeError("Значение должно быть строкой!")

    for char in text:
        if char == closed and not stack:
            return False
        
        if char == opened:
            stack.append(char)

        if char == closed:
            stack.pop()

    return len(stack) == 0      

try:
    print(is_valid(")("))
    print(is_valid("(()()()"))
    print(is_valid("(hello(2)ver()(33)python)"))
    print(is_valid("(hello(2()ver(33)python))"))
    print(is_valid("(hello(2()ver(33)python)"))
    print(is_valid(""))
    print(is_valid(1))
except ValueError as e:
    print("Упс... Что-то пошло не так.", e)
except TypeError as e:
    print("Упс... Что-то пошло не так.", e)
