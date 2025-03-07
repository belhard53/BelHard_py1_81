"""
Написать генератор последовательности Фибоначчи, 
который принимает максимальное количество чисел в последовательности 
из чисел Фибоначчи и генерирует последовательность. 
Затем  вывести на экран элементы данного генератора. 
Фибоначчи последовательность - первые два числа которой являются 0 и 1, 
а каждое последующее за ними число является суммой двух предыдущих. 
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55 и так далее.  
"""



def gen_fibonacci_numbers():
    a, b = 0, 1
    while True:
        a, b = b, a + b
        yield a

fibonacci_gen = gen_fibonacci_numbers()

print(next(fibonacci_gen)) #-> 1
print(next(fibonacci_gen)) #-> 2
print(next(fibonacci_gen)) #-> 2
print(next(fibonacci_gen)) #-> 3
print(next(fibonacci_gen)) #-> 5
