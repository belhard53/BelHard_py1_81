
# a = [1, 2, 3, "Hello", True]
# print(a)
# print(*a) # распаковка, тоже самое что написать каждый элемент списка через запятую

# print(a[:3]) # срезы как в строках

# a = list("Hel lo") # перевод в список
# print(a+a)
# print(a*3)

# a[0] = "Python"
# # "hello"[0] = "H" # со строками так нельзя

# print('l' in a)
# print('l' not in a)

# b = [] # пустой список
# b = list() # пустой список

# print(type(b))
# print(len(b), len(a))

# b.append(1)
# b.append(a)
# # b.append([1, 2, 3, [66, 44, [77, 33], 323], 323, 32, [3232, [323]]])

# print(b)
# b = [1, 2, 3, [66, 44, [77, 33], 323], 323, 32, [3232, [323]]]
# print(b[3][2][0])

# # 1 способ
# # users = []
# # user1 = ['Vasya', "Vasechken", 23]
# # user2 = ['Vasya2', "Vasechken3", 33]
# # user3 = ['Vasya3', "Vasechken3", 44]
# # # users.append(user1)
# # # users.append(user2)
# # # users.append(user3)

# # 2 способ
# # users = [user1, user2, user3]

# 3 способ
# users = [
#     ['Vasya', "Vasechken", 23, None], 
#     ['Vasya2', "Vasechken", 33],
#     ['Vasya3', "Vasechken", 44, [1112121, 212121]],
# ]

# users2 = users # обычная копия - переменных 2, а объект 1
# users2 = users.copy() # поверхностная копия - создает новый объект, но не касается вложенных списков 
# users2 = list(users) # тоже самое
# print(users is users2) 

# import copy
# users2 = copy.deepcopy(users) # глубокая копия - создает новый объект на всех уровнях вложенности



# users[0].append('VasyokTerminator')
# # print(a[1][2]) # возраст второго пользователя

# from pprint import pprint
# pprint(users) # красивый принт


users = ['Kolya', 'Vasya', "Petya"]

# users.clear()

# print(users.index('Vasya')) # какой индекс у элемента
# users.insert(0, 'Serg') # вставка на определенной место

# users.pop(2) # удаляет элемент по индексу, если индекс не написать удаляет последний
# user = users.pop() # также возвращает удаленный элемент
# users.remove('Serg') # удаляет элемент по значению
# del users[1] # удалить элемент с индексом 1
# del users[1:3] # удалить несколько элементов

# # 
# users.sort() # сортировка


users.reverse()
print(users[::-1]) # тоже самое но не меняет сам список

print(users)










