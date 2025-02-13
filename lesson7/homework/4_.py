'''
Запросить высоту елочки - число от 3 до 20. 
Напечатать на экране елочку где ее высота равна числу строк. 
Пример елочки из 4 строк:
   *
  ***
 *****
*******

'''



from random import Random
from rich.console import Console

random = Random()
console = Console()

# while True:
#     try:
#         rows = int(input("Введите высоту елочки от 3 до 20: "))
#     except ValueError:
#         print("Введите число")
#         continue

#     if rows < 3 or rows > 20:
#         print("Неверное значение")
#     else:
#         break

def c_tree(rows):
    # Рисуем зелёную елочку через rich со случайными белыми снежинками
    t = []
    for i in range(0, rows):      
        t1 = []
        for k in range(0, rows - i - 1):
            t1.append((" " if random.randint(0, 5) else "."))
        t1.append(" ")
        t1 = t1+  list("*" * (2 * i + 1))
        t1.append(" ")
        for k in range(0, rows - i - 1):
            t1.append((" " if random.randint(0, 5) else "."))
        t.append(t1)
    tree = "\n".join("".join(line) for line in t)
    # print(tree)
    return tree
    

import time

while 1:
    tree = c_tree(30)
    print(tree, end = '')
    print('\b'*len(tree), end = '', flush = True)    
    time.sleep(0.1)
   