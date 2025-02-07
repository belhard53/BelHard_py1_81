import time as t

print(1)
b = []
while 1:
    try:
        a = int(input(".."))
        print(7/a)
        # print(b[1])
        if a == 13:
            raise ValueError('13 нельзя') # создает исключение
        break
    except ZeroDivisionError:
        print('Ноль нельзя')
    except ValueError as ve:                  
        if ve.args[0][:2] == '13':
            print(ve)
        else:
            print("Только целое число")      
    except Exception as e:
        print('eeerrrr')
        print(123, e.with_traceback)
        
    else:
        print("ok")
    finally:
        print("все")

print(2)

