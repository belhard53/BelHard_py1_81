
import time


# # передача функции в виде аргумента и запуск ее внутри другой функции
# def f1(func):
#     print(111)
#     func()
#     print(222)

# def f2():
#     print('Hello ')
    
    
# f1(f2) 

# -------------------------------------
# тоже самое но с помощью декоратора


def f1(func):
    def wrapper(*args, **kwargs):
        print(1111)
        start = time.time()
        func(*args, **kwargs)
        print(2222)
        print(time.time()-start)
    return wrapper

def f11(func):
    def wrapper(*args, **kwargs):
        print(3333)
        start = time.time()
        func(*args, **kwargs)
        print(4444)
        print(time.time()-start)
    return wrapper


    
# @f11 # декораторов может быть несколько
@f1
def f2(a, b, c = 0):
    print('----', a, b, c)
    

@f1
def f3():
    print(12121212)
    

f2(1, 2, c=3)
    
# запустить функцию f2 без декоратора
# ищем ее в замыкании
f2_origin = f2.__closure__[0].cell_contents
print(f2_origin) # -> <function f2 at 0x00000230D7F7CAE0>
f2_origin(1, 2)


# ------------------------------
# декораторы с настройкой параметров
    
# def loging(filename='3.txt'):
#     # print(filename)
#     def _loging(func):
#         def wrapper(*args, **kwargs):
#             with open (filename, "a", encoding='utf8') as f:
#                 from time import time, ctime, strftime
#                 # f.write(f"{ctime()} - запущена {func.__name__}\n")
#                 f.write(f"{strftime('%M:%S')} - запущена {func.__name__}\n")                
#             func(*args, **kwargs)            
#         return wrapper
#     return _loging


# @loging(filename="log1.txt")
# def f1():
#     a = 1+1
    
# @loging(filename="log2.txt")
# def f2():
#     a = 1+1
    
# @loging()
# def f3():
#     a = 1+1
    
    
# f3()