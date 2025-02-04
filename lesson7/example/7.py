# while - когда не знаем сколько повторов
# for - когда знаем сколько раз повторить, или что то перебрать


# ---------------------------------
# бесконечные циклы
# while 1:   
    # pass
# while True:
    # pass
 
# i = 0 
# while i < 10:
#     # print(1)
#     # print(2)
#     # print(3)
#     print(i)
#     i += 1  # переменная счетчик
    
# print('ok')
    
# -------------------

# pas = input("Пароль?")
# i = 1
# while pas != "1234" and i <= 3:
#     print('err')
#     pas = input()
#     i += 1
# else:
#     print(i, 'ok')
    
# pas = ""
# i = 1
# while i <= 3:
#     pas = input("")
#     if pas == '1234':
#         break # останавливает цикл на этом месте
#     print('err')
#     i += 1

# a = 1
# b = 10   
# while a == 1 and b < 20:
#     b += 1
#     if b == 13:
#         continue #  пропускает данную итерацию
#     print("ok")
    
    
# import time
# a = 5
# while a >= 0:
#     print(a)
#     time.sleep(1)
#     a -= 1
    
    
# бесконечный выбор меню пока не введут стоп    
# menu = '''
# 1 - ПОГОДА
# 2 - АНЕКДОТ
# 3 - КУРСЫ ВАЛЮТ
# 0 - ВЫХОД
# '''
# res = input(menu)
# while res != '0':
#     if res == 1:
#         print(1)
#     elif res == 2:
#         print(2)
#     elif res == 3:
#         print(4)
#     res = input(menu)


# =========================================

# for i in [0, 1, 2, 3, 4]:
# for i in range(5):
#     # print('---')
#     print(i)
#     # print('---')

# print(list(range(5)))
# print(list(range(5, 51)))
# print(list(range(5, 51, 5)))

# for i in range(3): # три попытки
#     if pas = '1234':
#         break
# else:
#    print('err')

# перебор списка
# users = ['user1','user2','user3']
# for user in users:
# #     print(user)

# перебор списка и потом перебор каждого элемента списка по символам
# for user in users:
#     print(user)
#     for symbol in user: 
#         print(symbol)



# a = [1, 2, 3]
# b = [4, 5, 6]
# for i1, i2 in zip(a, b): # перебор двух списков
#     print(i1, i2)

# users3 = [
#     {"name":"Vasya1", "login":"vvasiiiia",  "age":23},    
#     {"name":"Vasya2", "login":"vvasiiiia",  "age":23},    
#     {"name":"Vasya3", "login":"vva@siiiia!",  "age":23},    
#     {"name":"Vasya4", "login":"vvasiiiia",  "age":23},    
#     {"name":"Vasya5", "login":"vvasiiiia!",  "age":23},    
#     {"name":"Vasya6", "login":"vv#asiiiia",  "age":23},    
#     {"name":"Vasya7", "login":"vvasiiiia",  "age":23},    
#     {"name":"Vasya8", "login":"vvasiiiia!",  "age":23}
# ]
    
# bad_symbols = "!@#$%^&*())"
# for user in users3:
#     log = user['login']
#     for s in log:
#         if s in bad_symbols:
#             print(f"{user['name']} err - {s}")



# a, b = (1, 2)  # распаковка списка в переменные

# for i, user in enumerate(users3, 1): # [(0, item1), [1, item2], ...]
#     print(i, user)
#     log = user['login']
#     for s in log:
#         if s == "!":
#             print("   ", i, user['name'], 'err')

# print(*enumerate(users3))


# перебор словаря - перебираются ключи
# for key in users3[0]: 
#     print(key, users3[0][key])

# for key, val in users3[0].items():
#     print(key, val)
    
# for val in users3[0].values():
#     print(val)
    
# for i in range(10):
#     print(i)
#     if i == 4:
#         break


# for s in "Python Hello":
#     print(s)