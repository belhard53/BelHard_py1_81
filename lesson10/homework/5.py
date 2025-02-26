"""
Написать функцию счетчик которая с помощью замыкания (без глобальных переменных)
будет хранить в себе количество запусков и каждый раз возвращать число на 1 больше.
Функция должна принимать число с которого начинается отсчет.

Пример:
с1 = counter(1)
с10 = counter(10)

print(c1()) -> 2
print(c1()) -> 3
print(c1()) -> 4 

print(c10()) -> 11 
print(c10()) -> 12 
print(c10()) -> 13 

"""


def get_counter(initial=0):
    counter = initial
    def inner():
        nonlocal counter
        counter += 1
        return counter
    return inner

с1 = get_counter(1)
print(с1()) # печатает 2
print(с1()) # печатает 3
print(с1()) # печатает 4

c10 = get_counter(10)
print(c10()) # печатает 11
print(c10()) # печатает 12
print(c10()) # печатает 13
