ball_price1 = 150 # int
ball_price2 = 130.35 #float
text = "Hello" # str


ball_price1 = ball_price1 + 10
ball_price1 += 10

ball_price1 = "150" 

# t = type(ball_price1)
print(type(ball_price1))

print(ball_price1+str(3)) # int str
print(int(ball_price1)+3) # int str

print(1+1*2)
print((1+1)*2)

print(15%7) # остаток 
print(15//7) # целая часть

a = 10
a += 1 # a = a + 1
a -= 1 # a = a - 1
a /= 1
a *= 1


a1, a2, a3 = 1, 2, 5
b1 = b2 = b3 = 4
print(a1, a2)
print(a3)
print(b1, b2, b3, sep=" ----- ", end="=end\n")

print(r'Hello c:\new "Python"') # raw строка - отключает 

a1, a2 = a2, a1 # замена значений
a4 = a1
print(id(a1), id(a4))
print(a1 is a4 )

# name = input('Имя?') # результат всегда строка
# print('Привет', name)

# from time import time
# print(time())

# from datetime import datetime
# date_now = datetime.now()
# print(type(date_now))

# year = int(input("гр?"))
# # year = int(year) 
# age = date_now.year - year
# print(age)


# тут видно что у изменяемых тиров при изменении одной переменной меняются 
# остальные с таким же id
l1 = [1, 2, 10, 'Hello', True] # список, list
l2 = [1, 2, 3]
l3 = l2
print(l3 is l2) # True - одинаковые id
l2.append(4)
print(l2)
print(l3) # 4 тоже добавилась - l2 и l3 по сути это один и тот же объект

None # отдельный тип данных
a = None
    
# логический тип
ok = True
ok = False

is_send = True

2 + 2 # арифм выражение
3 < 4 # логическое выражение -> True False

ok = 2 > 5

a, b = 2, 7
ok = a > b
ok = a < b
ok = a <= b
ok = a >= b
ok = a != b
ok = a == b

print(ok)

#проверить пароль
# password = input("Пароль?")
# ok = password == '111'

print(bool(1))
print(bool(2+2))
print(bool(2-2))
print(bool(-1323))
print(bool(0))
print(bool(""))
print(bool("22"))
print(bool("ds;dl's;"))
ok = type(a) == int
print(f"Переменная 'а' это целое число - {ok}")


# a = 100**1000 # int не ограничен по величине
# print(a)


a = 0.111 + 2.111 + 0.111
a = round(a, 2)
print(a)
print(int(a))

# import math
# math.floor

#print(int("11.55")) # ОШИБКА
print(float('11.55'))

menu = '''
1 - asdas
2 - dsds
3 - dsds
4 - sdsdds
'''
# input(menu)

a = 23_212_121 # для удобства можно писать так - получиться обычное число
print(a)

name = "Вася"
age = 25
print('Привет ' + name + ' тебе ' + str(age) + ' лет.')
print('Привет', name,  'тебе',  age, 'лет.') # главное понимать что через зпт можно только в print
print(f"Привет {name} тебе {age} лет.")










