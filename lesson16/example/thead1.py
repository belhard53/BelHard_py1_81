from threading  import *
from time import time, sleep

def f1(s):
    sleep(s)
    print(1)

def f2(s):
    sleep(s)
    print(2)


t1 = Thread(target=f1, args=(2,))
t2 = Thread(target=f2, args=(1,))
t3 = Thread(target=f1, args=(1,))

start = time()

t1.start()
t2.start()
t3.start()

t1.join()# ожидаем окончания
t2.join()
t3.join()

end = time()
print(end-start)
print("end")
