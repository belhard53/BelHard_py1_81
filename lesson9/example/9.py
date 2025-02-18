# функция видит внешние(глобальные) переменные и может их использовать 
# Но не может их менять
# def f1(a):
#     print(a + 1)
    

# def f2():
#     global a, b # сообщаем что a и b используем из глобальной области программы
#     
#     # если 'a' из глобальной области то меняем ее, 
#     # иначе 'а' создастся новая в локальной области функции
#     a = 4 
#     a += 1 # в обоих случаях ее можно менять
#     
#     print(1, a)
#     # print(locals())
#     
#     def f3():
#         # global a # сообщаем что "a" используем из глобальной области программы
#         # nonlocal a # сообщаем что "а" используем из функции f2

#         # если не global и не nonlocal \    
#         # 'а' создастся новая в локальной области функции
#         # a = 15 

#         a += 10 # меняется та "а" которую используем
#         print(2, a)
    
#     f3()
#     print(4, a)
  
  
# переменные созданные в программе  а не в функции считаются глобальными
# a, b = 2, 5
# # f1(a)

# f2()
# # print(globals())

# print(3, a)

# ---------------------------------
# рекурсия

# n = 0
# def f1(text):
#     global n
#     n += 1
#     if text:
#         print(n, text)
#         f1(text[:-1])
#     return
    
    
# f1("Hello Python")

#----------------------------
# неограниченное количество аргументов

# def f1(*args, **kwargs):    
#     # print(args, kwargs)
#     for t in args:
#         # print(t*2, **kwargs)
#         print(t*2, kwargs['end'], kwargs['sep'])


# # f1("hello", "1", 12323, end="/", sep = ' - ', n=4)
    
# def f2(a, *, b): # после звездочки обязательно только именованные аргументы
#     pass    
# f2(1, b="1")

# -----------------------------------------
# a = lambda : 2+2
# print(a())

# a = lambda x: x+2
# print(a(5))

# print((lambda x: x+24)(5))
# print((lambda x: x == 1)(5))
# print((lambda x: True if x == 1 else False)(5))
# print((lambda x, b: x+b+24)(5, 7))

# def f1(x):
#     return x*2**2+3

# a1 = map(f1, [1,2,3,4,5])
# a2 = map(lambda x: x*2**2+3, [1,2,3,4,5])
# print(*a1)
# print(*a2)

# ---------------- filter
# users = [
#     {'name':'vasia!',
#         'age':25, 
#         'surname':'vasiapupkin', 
#         'phone':'3752323232'},
#     {'name':'DIma11111111111', 
#         'age':33,
#         'surname':'DimaKrivenyz', 
#         'phone':'3752323232'},
#     {'name':'Petia', 
#         'age':21,
#         'surname':'DimaKrivenyz', 
#         'phone':'3752323232'}
# ]

# def f1(user):    
#     return user['name'] == 'DIma'

# f = filter(f1, users)
# print(*f)

# f = filter(lambda user: "!" in user['name'], users)
# print(*f)

# # --------- sorted
# a = [[11, 2], [2, 4], [1, 5], [8, 3]]
# b = sorted(a, key=lambda x: x[0])
# print(b)

# # def sort_user(user):
# #     pass
# # b = sorted(users, key=sort_user, reverse=True)    

# b = sorted(users, key=lambda user: user['age'], reverse=True)
# b = sorted(users, key=lambda user: len(user['name']), reverse=True)

# print(b)



# d = {1:11, 9:22, 3:33, 4:77, 7:44}
# print(d.items())
# d2 = dict(sorted(d.items(), key=lambda item:item[0])) # сортировка по ключу
# d3 = dict(sorted(d.items(), key=lambda item:item[1])) # сортировка по значению
# print(d2)
# print(d3)