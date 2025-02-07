len("hello")
# print()

a: int  = 2 
    
# def print_10(text, num):
# def print_10(text: str, num: int, n_str: bool):
# def print_n(text: str, num: int = 1, n_str: bool = True, end="\n"):
def print_n(text: str, 
                param: dict,
                num: int = 1, 
                n_str: bool = True):
    a = 1
    for i in range(num):
        if n_str:
            # param это словарь
            # через ** он будет распакован 
            # и записан в виде - key1 = value1, key2 = value2, ...
            # в данном случае - end = " /// ", sep = " "
            # после распаковки - print(i, text, end = " /// ", sep = " ")
            print(i, text, **param)
        else:
            print(text, **param)

    
# param = {"end":" /// ", 'sep':" "}
    
# b = "python"   
# print_n('Hello1', n_str=False, param=param, num=5)
# print_n(b, param, 2, False)
# # # print("hello")



def s(a, b):            
    if a ==0:
        return False   #! return ВСЕГДА заканчивает функцию 
    # p = a*b   
    # return p
    print(1)
    return a*b
    

p = s(2, 3)
if p:
    print(p)

print(s(4, 5))

def max_n(a, b):    
    return a if a>b else b

#найти наибольшее из трех
a1, a2, a3 = 5, 4, 2
print(max_n(max_n(a1, a2), a3))