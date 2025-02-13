"""
Напишите функцию yes_or_no, которая принимает список из целых чисел,
а возвращает список из Yes или No для каждого элемента, 
Yes - если число уже встречалось и No, если нет
[1,2,3,1,4] => [no, no, no, yes, no]

если в списке не все целые числа вернуть False.

"""



l = [1,2,3,1,4]

# 1 вариант
l2 = l.copy()
for i in range(len(l)):
    if l[0:i].count(l[i]) > 0:
        l2[i] = 'y'
    else:
        l2[i] = 'n'

# 2 вариант
l3 = ['y' if l[:i].count(l[i]) else 'n' for i in range(len(l))]

print(l2)
print(l3)