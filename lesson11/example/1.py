# def f1():
#     print(1)
    
# def f2():
#     print(2)




# d = {
#     "+":f1,
#     "-":f2
# }

# a = "+"
# # d["-"]()
# d[a]()

# --------------------------------------



## ----------- внутренние свойства функций 
def bar(objs: list):
    '''
    docs 123
    '''
    for obj in objs:  # type: int
        print(obj)


print(1, bar.__annotations__)
print(2, bar.__name__)
print(3, bar.__code__)
print(4, bar.__builtins__)
print(5, bar.__dict__)
print(6, bar.__sizeof__())
print(7, bar.__class__)








