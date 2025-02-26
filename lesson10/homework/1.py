'''
Добавить несколько черепах 
    - или сразу 
    * или в течении игры по одной через определенное количество кликов
    - на каждой забиндить клик через одну и туже функцию cath

'''



from turtle import *
from random import randint
import random

def catch_any(t_n):
    def catch(x,y):
        ts[t_n].goto(0,0)
        ts[t_n].left(randint(0, 360))
        global click_count, num_of_t, timer
        click_count += 1
        print(click_count)
        if click_count % timer == 0:
            num_of_t += 1
            add_turtle()
        
    return catch

def add_turtle():
    global num_of_t, ts, colors
    t = Turtle('turtle')
    t.speed(0)
    t.color(random.choice(colors))
    t.left((randint(1, 12) * 30))
    x = catch_any(len(ts))
    t.onclick(x)
    ts.append(t)

num_of_t = int(input("Введите сколько будет черепах? "))
timer = int(input("Сколько кликов до появления новой черепахи? "))
colors = ["red", "blue", "green", "purple", "brown"]

ts = []
click_count = 0

for i in range(num_of_t):
    add_turtle()

while 1:
    for t in ts: # берем каждую черепаху из списка
        t.forward(3) # вперед на 3 пикселя

mainloop()