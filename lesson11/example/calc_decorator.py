operators = {}

def op(operator):
    def operation(f):        
        operators[operator] = f
    return operation

#декораторы собирают инфу о функциях и операторах
@op(operator="+")
def summa(a, b):
    return a + b

@op(operator="*")
def reduce(a, b):
    return a * b

print(operators)

txt1  = "2 * 8".split()
txt2  = "2 + 6".split()

reduce(1, 5)

try:
    # запуск нужной функции происходит на основе собранной инфы
    print(operators[txt1[1]](int(txt1[0]), int(txt1[2])))
    print(operators[txt2[1]](int(txt2[0]), int(txt2[2])))
except:
    print("oops...")
