# f = open('111.txt', "r") # только чтение
# f = open('111.txt', "w") # стирает все - пишет новое
# f = open('111.txt', "a") # добавить к старой информации

import os
file_dir = os.path.dirname(__file__)

print(1111, file_dir)

with open(f'{file_dir}\\111.txt', "r") as file:
    
    # txt = file.read() # читаем все
    
    # for line in file: # читаем по строкам
    #     print(line)
    
    
    lines = file.readlines() # читаем все строки в список

print(lines)    
# print(txt)
# f.close()



# ---------------------

# with open(f'{file_dir}\\222.txt', "w", encoding='utf-8') as file:
#     file.write("123456\n7890\nпривет пайтон")



# ---------------------------------    
# сохраняем объекты в файл
# import pickle

# sp = [1, 2, 3, 4, 9]

# # with open(f'{file_dir}\\333.data', "wb") as file:
# #    pickle.dump(sp, file)
   
# with open(f'{file_dir}\\333.data', "rb") as file:
#    sp1 = pickle.load(file)   
   
# print(sp, sp1)