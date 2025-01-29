# # СПИСКИ list 
# a = list()
# b = []
# a = [1, 2, 3]
# a = list("hello")
# b.append(1)

# ========================================
# КОРТЕЖИ tuple

# c = tuple() 
# pos = (100, 200) # x y
# rgb = (123, 100, 50)


# c = (1,)
# print(c, type(c))
# b = 1, 2, 3
# print(b, type(b))
# b = (1, 2, "dsds")
# print(b)

# a = [1, 2, 3]
# b = tuple(a)
# print(b, type(b))


# ========================================
# МНОЖЕСТВА set

# a = set()
# b = {1, 2, 3, 4, 1, 2, 9}
# b.add(10)
# print(b, type(b))

# a = frozenset(b)
# print(a, type(a))

# c = [1, 2, 3, 1, 2, 3]
# c2 = set(c)
# print(c, c2)

# a = set("Hello Python")
# print(a)



# a = {8, 3, 1, 5 }
# # b = {6, 7, 8, 3}
# b = {8, 1, 3}

# # Включает ли set другой set
# print(a.issubset(b)) # все элементы a принадлежат b.
# print( a <= b )

# print(a.issuperset(b)) # все элементы b принадлежат a.
# print( a >= b )


# #объединение и пересечение

# print(a | b) # об] объединить
# print(a.union(b)) # объединить

# print(a.intersection(b)) # пересечение - только общие
# print(a & b)

# print(a.difference(b)) # разность - есть только в первом
# print(a - b)

# print(a.symmetric_difference(b)) # есть в обоих но не общие
# print(a ^ b)



# ========================================
# словари dict

# {ключ:значение, ключ2:значение2}

# user = ['Vasya', 'vassssia', 23, "iweuryiwe"]
# print(user[2])
# d1 = {}
# d2 = dict()


# d1 = {"key1":"value1", "key2":"value2"} 
# d2 = dict(key1="value1", key2 = "value2") # аналогичная запись
# print(d1, d2)

# d1 = dict.fromkeys(["key1", "key2"], "value")
# d2 = dict.fromkeys(["key1", "key2"])
# print(d1, d2)

# sp = [("key1", "value1"), ("key2", "value2")]
# d1 = dict(sp)
# print(d1)

# d1[1] = 11 # добавить в ключ 1 со значением 11 
# d1["key3"] = "value3" # добавить в ключ key3 со значением value3
# print(d1)



# user1 = {
#     "name":"Vasya", 
#     "login":"vvasiiiia", 
#     "age":23, 
#     "2":"1217628", 
#     'phones':{
#         'mts':'1212121', 
#         'vel':'4203948230'
#     }, 
#     "child":[
#         '1212', 
#         2121]
# }

# user2 = {"name":"Vasya2", "login":"vvasiiiia2", "age":23, "2":"1217628", 
#                 'phones':{'mts':'1212121', 'vel':'4203948230'}, 
#                 "child":['1212', 2121]}

# users = {1:user1, 2:user2} # словарь из словарей
# print(users[1]['phones']['mts'])

# users2 = [user1, user2] # список из словарей
# print(users2[0]['child'][1])

# key - неизменяемые тд
# value - любые

# print(list(user.keys()))
# print(list(user.values()))
# a = list(user.items())[2][1]
# print(a)

# user1['name'] = 'Petya'
# user1['pas'] = '1234' # добавить новый

# print(user1['surname'])
# print(user1.get('name', "Нет"))

# del user1['age']



# users3 = [
#     {"name":"Vasya1", "login":"vvasiiiia",  "age":23},    
#     {"name":"Vasya2", "login":"vvasiiiia",  "age":23},    
#     {"name":"Vasya3", "login":"vvasiiiia",  "age":23},    
#     {"name":"Vasya4", "login":"vvasiiiia",  "age":23},    
#     {"name":"Vasya5", "login":"vvasiiiia",  "age":23},    
#     {"name":"Vasya6", "login":"vvasiiiia",  "age":23},    
#     {"name":"Vasya7", "login":"vvasiiiia",  "age":23},    
#     {"name":"Vasya8", "login":"vvasiiiia",  "age":23}
# ]


# d1 = {"key1":"value1"}
# d2 = {"key2":"value2"}
# d3 = {"key3":"value3"}
# d1.update(d2) # добавить к словарю второй словарь, меняет словарь d1
# d5 = d2 | d3 # сложить два словаря - не меняет d1 d2 - возвращает объединенный
# print(d1)
# print(d5)



