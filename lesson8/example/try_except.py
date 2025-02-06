import time as t

print(1)
b = []
while 1:
    try:
        a = int(input(".."))
        print(7/a)
        # print(b[1])
        if a == 13:
            raise ValueError('1 - 13 нельзя') # создает исключение
        break
    except ZeroDivisionError:
        print('Ноль нельзя')
    except ValueError as ve:
        print("Только целое число")
        if ve[:2] == '13':
            print(ve)
    except Exception as e:
        print('eeerrrr')
        print(e)
    else:
        print("ok")
    finally:
        print("все")

print(2)

