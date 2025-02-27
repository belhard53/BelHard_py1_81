# import sys

# # print(sys.path)
# # sys.exit()
# args = sys.argv
# if args[1] == "--version":
#     print('1.1.0')
# else:
#     print(args)
    
# -------------------------------------------
# import os

# dir_ = os.getcwd()
# dir_ = os.path.join(dir_, "lesson14", "example")
# file = os.path.join(dir_, "lesson14", "example", "1.py")
# print(dir_)
# print(os.path.exists(file))
# print(os.listdir(dir_))
# ----------------------

# from pathlib import Path

# path = Path().home()
# path = Path(path, 'fold1', '111.jpg')
# print(111, path)
# print(222, path.parent.parent)
# for p in path.parents:
#     print(333, p)
    
# path = Path().cwd()
# # for p in path.iterdir():
# for p in path.glob('**/*'):
#     print(444, 'file' if p.is_file() else 'dir',  p )

# -------------------------------------------------------

# import math #математика
# math.sqrt(9)
# -----------------------
# import copy
# # copy.deepcopy()

# ------------------------

# import itertools
# itertools.count(start=0, step=1) #бесконечная арифметическая прогрессия с первым членом start и шагом step.
# itertools.cycle(iterable) #- возвращает по одному значению из последовательности, повторенной бесконечное число раз.
# itertools.repeat(elem, n=Inf) - повторяет elem n раз.
# itertools.accumulate(iterable) - аккумулирует суммы.

# ---------------------------------

# import decimal
# print(0.1 + 0.1 + 0.1)


# ----------------------------------

# from enum import Enum
# class CatColor(Enum):
#   WHITE = 0
#   BLACK = 1
#   GINGER = 2
  
  
# cat = CatColor.GINGER 

# # Выводит 2
# print(cat.value)
# # Выводит GINGER 
# print(cat.name)

# -----------------------------------------


# import logging    

# logging.basicConfig(level=logging.DEBUG, filename='111.log',
#                 format='%(asctime)s - %(levelname)s - %(message)s')


# logging.debug('111')
# logging.info('222')
# logging.warning('333')
# logging.error('444')
# logging.critical('55')
# ----------------------------------------