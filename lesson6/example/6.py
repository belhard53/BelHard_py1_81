
# if True:
#     print(1)
# else:
#     print(2)
    

# ok = 2 == 3
# ok = 2 > 3
# ok = 2 < 3
# ok = 2 <= 3
# ok = 2 >= 3
# ok = 2 != 3
# ok = not 2 == 2

# if ok:
#     pass



a = 1
b = 1
c = 3

# if not a==b:
#     print(1) # строчек внутри может быть много
#     print(2)
#     print(3)
# else:
#     print(2)
    
# if a==b:
#    # if b > c:    
#     if b != c:
#         print(1)
#     else:
#         print(3)
# else:
#     print(2)    
    
# c = []
#if not c:
    # pass

# if c:
#     pass    


# e = a == b
# # if e == True # bad practice
# if e:
#     pass



# -------------------
# # тернарный if
# a = a + 1 if b == 2 else 3    
# print(f"hello {1 if b == 1 else 2}")    
# print(f"hello"  if b == 2 else "python")  

    
# -----------------------    
# and or    
    
# # if a == 1 and b == 1 and c == 2:
# if a == 1 and (b == 1 or c == 2):
#     pass

# if a == 1 and b == 1 and c == 2:
#     print(1)
# else:
#     print(2)
    

# ok = True and True - True
# ok = True and False - False

# ok = True or True - True
# ok = True or False - True

# ok = True or False or False - True
# ok = True or False and True - True
# ok = True or False and False - False
# ok = False or False or False - False

# новый пример
# ok = False and False or True    # - True
# ok = False and (False or True)    # - False - скобки решают


# is_admin = False
# is_moderator = True
# age = 20
# if is_admin or is_moderator and age > 18:
# if is_admin or (is_moderator and age) > 18:    
# if (is_admin or is_moderator) and age > 18:    # так правильно 
#     print("Доступ разрешен!")
# else:
#     print("Доступ запрещен.")


# x = True
# y = False
# z = False
# if not x or y:
#     print(1)
# elif not x or not y and z:
#     print(2)
# elif not x or y or not y and x:
#     print(3)
# else:
#     print(4)

# ------------------
# # проверка перед сравнение чтобы не было ошибки
# user = ['name1', 'pass1','log1']
# user = []
# if user and user[1] == 'pass1':
#     print(1)



# --------------------
# # elif  - иначеесли 
# a = 7
# if a == 1:
#     print(1)
# else:
#     if a == 2:
#         print(2)
#     else:
#         if a == 3:
#             print(3)
#         else:
#             if a == 4:
#                 print(3)
#             else:
#                 print("err")




    
# a = 1
# if a == 1:
#     print(1)
# elif a == 2:
#     print(2)
# elif a == 3:
#     print(3)
# elif a == 4:
#     print(3)
# else:
#     print("err") 

# print('end')   


# if выше можно заменить словарем
# a = 1
# d = {1:"Hello",2:2,3:3,4:4}
# print(d[a])



# --------------------
# if type(a) == int:
#     print(1)

# # if isinstance(a, (int, bool) # или
# if isinstance(a, int | bool): # или  python 3.10+
#     pass

# print(all([1, 2, 0, True])) # все True
# print(any([1, 2, 0, True])) # хотя бы 1 True

# b = a or 2   
# print(b)

# x=True
# print((1,2)[x])


# a = 1
# if a == 1 or a == 5 or a == 6:
#     print(11)
# elif a == 2 or a == 9:
#     print(22)
# elif a == 3:
#     print(33)
# elif a == 4:
#     print(33)

# a = 9
# match a:
#     case 1 | 5 | 6:
#         print(11)
#     case 2|9:
#         print(2)
#     case 3:
#         print(33)



# # ------------------
# # диапазоны 
# a = 33

# if a < 20 or a > 40:
#     pass
# if  20 < a < 40:
#     pass
# if  20 <= a <= 40:
#     pass

