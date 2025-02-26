
# абстракция
# наследование
# полиморфизм
# инкапсуляция

# ---------------------
# наследование

# class A:
#     a1 = 1
#     def __init__(self, val=0):
#         self.a2 = 2
#         self.val = val
#         print(111)
        
# class B:        
#     b1 = 1
#     def __init__(self):
#         self.b2 = 2
#         print(222)

# # mixin 
# class Mixin1:
#     def print1(self):
#         print(2)

        
# class C(A,  B, Mixin1):
#     def __init__(self, val=0, val3=0):
#         A.__init__(self, val)
#         B.__init__(self)
#         self.val3 = val3
        

# class D(A):
#     def __init__(self, val1=0, val2=0):
#         # A.__init__(self, val1) # или так или ниже
#         super().__init__(val1)
#         self.val2 = val2
        
      

# a = C(1, 2)
# # print(vars(a))
# print(a.__dict__)
# print(a.s1)
# a.print1()        
       
#   ------------------     
       
# from turtle import *

# class Tur(Turtle):
#     def __init__(self, shape = "turtle", color_='red', x=100, y=100):
#         super().__init__(shape=shape)
#         self.color(color_)
#         self.goto(x, y)

        
# t = Tur(color_="blue", x=200, y=200)        
# mainloop()


# ---------------------------
# from typing import Any

# class MyList(list):
#     def slice(self, n):
#         for i in range(n):
#             self.insert(0, self.pop())

      # полиморфизм
#     # переписали метод appepnd - теперь он вставляет не в конец а в начало       
#     def append(self, __object: Any) -> None:
#         # super().append('a')
#         self.insert(0, __object)
        

# a = MyList()
# a += [1,2,3,4,5,6]
# a.append(7)
# # a.slice(3)
# print(a)


# -----------------------
# инкапсуляция


# class User:   
#     # __age: int = 0    # private
#     _flag = False     # protect - доступно через наследование
    
    
#     # def __check_age(self, age):
#     #     return age >= 14
    
#     @staticmethod
#     def __check_age(age):
#         return age >= 14
    
#     def __init__(self, name, age):
#         self.name = name
#         if not self.__check_age(age):
#             raise ...
#         self.__age = age
    
    
#     @property #getter  
#     def age(self):        
#         return self.__age
    
#     @age.setter
#     def age(self, val):
#         if self.__check_age(val):
#             self.__age = val
#         else:
#             raise ValueError ("Возраст меньше 14")
    
#     def change_type(self):
#         self._flag = not self._flag
    
#     def add_age(self):
#         self.age += 1
    
#     @property
#     def type(self):
#         return int(self._flag)




# user = User("Вася", 33)
# user.age = 15
# # user.age = 6 # не пройдет проверку - ошибка
# print(1, user.age)


# # print(2, user.__age) # ошибка т.к. __age приватная и ее имя изменено \
#                        # механизмом name mangling и __age как бы не существует
# user.__age = 11 # а Python создаст новую переменную с именем __age в объекте user,
# print(3, user.age) # выдает 15 т.к. обращается к оригинальной приватной __age
# print(4, user.__age) # уже не выдает ошибку, т.к. в 142 стр мы ее создали
#                      #но это все еще другая __age 


# print(user._flag) 
# print(user.type)
# user.change_type()
# print(user.type)



# -----------------------------------------------
# # Утиная типизация 

# class A:
#     def foo1(self):
#         print(1)
#     def __len__(self):
#         return 1
    
# class B:
#     def foo1(self):
#         print(2)
#     def __len__(self):
#         return 2

# def f1(obj):
#     obj.foo1()
        
# a = A()
# b = B()

# f1(a)
# f1(b)

# l = [A(), B(), A(), "sas"]
# print(list(map(len, l)))
# for obj in l:
#     try:
#         obj.foo1()
#     except:
#         print('err')




# -----------------------------------------------       
# # абстрактные классы 
# # только для наследования
# from abc import ABC, abstractmethod

# class Basic(ABC):
#     __slots__ = ['a','b']
    
#     @abstractmethod # только для перезаписывания
#     def foo1(self):
#         print(1)


# class Child(Basic):    
#     def foo1(self): # должен быть обязательно
#         super().foo1()
#         print(2)
        

# # a = Basic()
# b = Child()
# # a.foo1()
# b.foo1()        


# ----------------------------

      

# декораторы класса
# def class_decorator(cls):
#     attrs = dict(a=1, b=2, c=3)
#     for attr, val in attrs.items():
#         setattr(cls, attr, val) 
#     return cls

# @class_decorator
# class A:    
#     def a():
#         print(1)
        
        
# a = A()    
# print(a.a, a.b)	
# print(a.__dict__)


# *****************************
# from dataclasses import dataclass

# # @dataclass(frozen=True)
# @dataclass()
# class User:
#     # получаем упрощенную запись класса
#     # с реализованными методами __init__, __repr__, __str__ и __eq__
         
#     # аннотации типов обязательны
#     name:str
#     age:int
#     a: Any
    
# user = User('Alex', 33, 1)
# user.age = 20


# users = [
#     user,
#     User("Max", 20, '1'),
#     User("Djo", 20, True)
# ]

# for user in users:
#     print(user.age)
#     # user.send_email()