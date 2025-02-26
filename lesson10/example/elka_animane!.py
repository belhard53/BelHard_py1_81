'''
Запросить высоту елочки - число от 3 до 20. 
Напечатать на экране елочку где ее высота равна числу строк. 
Пример елочки из 4 строк:
   *
  ***
 *****
*******

'''


"""
Запросить высоту елочки - число от 3 до 20. 
Напечатать на экране елочку где ее высота равна числу строк. 
Пример елочки из 4 строк:
   *
  ***
 *****
*******
"""

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
            t1.append((" " if random.randint(0, snow_rate) else "."))
        t1.append(" ")
        t1 = t1+  list(tree_char * (2 * i + 1))
        t1.append(" ")
        for k in range(0, rows - i - 1):
            t1.append((" " if random.randint(0, snow_rate) else "."))
        t.append(t1)
    
    return t
    
    

def next_frame(rows):    
    for y in range(rows-2, -1, -1 ):
        for x, s in enumerate(tree[y]):
            weight = 0
            if y < rows - 3 and s == "*":
                weight = 1
            try:
                if tree[y+1+weight][x-wind] != tree_char:
                    tree[y+1+weight][x-wind] = tree[y][x]
            except:
                pass
    
    for x, s in enumerate(tree[0]):            
        if s != tree_char :                
            if random.randint(0, snow_rate):
                tree[0][x] = " " 
            else:
                if  around_is_empty(x):
                    tree[0][x] = random.choice(snow)
                   

def around_is_empty(x):
    # проверяет пусто ли в ближайших 2х клеточках
    res = []    
    for x_shift in range(-2, 3):
        for y in range(0, 3):
            try:                
                res.append(tree[y][x + x_shift] == ' ')
            except Exception as e:
                res.append(False)    
    return all(res)
    

import time
rows = 30 
snow_rate = 15
snow = ['.', '+', '.', '.', '*', '*', '.']
tree_char = "Ж"
wind = -1
tree = c_tree(rows)



ticks = 0

while 1:
    tree_txt = "\n".join("".join(l) for l in tree)    
    print(tree_txt, end = '')
    print('\b'*rows*3, end = '', flush = True)
    next_frame(rows)
      
    ticks += 1
    if not ticks%30:
        wind = random.randint(-1, 1)
   
    time.sleep(0.1)  