# замыкания

# def f1(a):
#     def wrapper(x):
#         print(a + " " + x)
#     return wrapper
    
# # f3 = f1

# # f1("Hello")()
# # b = f1("Hello")
# # b()

# def f2(f):
#     a = "Python"
#     f(a)

# f2(f1("Hello1"))
# f2(f1("Hello2"))
# f2(f1("Hello3"))
# ----------------------

# def f1(a):
#     def f2(b):
#         return a*b
#     return f2

# a_1 = f1(1)
# a_2 = f1(2)
# print(a_1(5))
# print(a_2(5))
# ------------------------


def print1(a):
    def wrapper(b):
        print(f"{a}{' - ' if a else ''}{b}")
    return wrapper

pr_err = print1("Error")
pr_info = print1("Внимание")
pr = print1("")

pr_err("Пароль неверный") # перед сообщением будет слово Error
pr_info("В пароле должно быть более 7 символов")
pr("Ok")