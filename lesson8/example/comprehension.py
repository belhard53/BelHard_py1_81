# a = list(range(11))
# a = [1, 2, 3]

a = []
for i in range(11):
    # if i == 5:
    #     continue
    if not i % 2:
        a.append(i**2)
    else:
        a.append(i**3)

print(a)    
    
b = [i**2 for i in range(11)]  
print(b)  

b = [i**2 for i in range(11) if not i % 2]
print(b)


users3 = [
    {"name":"Vasya1", "login":"vvasiiiia",  "age":23},    
    {"name":"Vasya2", "login":"vvasiiiia",  "age":23},    
    {"name":"Vasya3", "login":"vva@siiiia!",  "age":23},    
    {"name":"Vasya4asas", "login":"vvasiiiia",  "age":12},    
    {"name":"Vasya5", "login":"vvasiiiia!",  "age":23},    
    {"name":"Vasya6", "login":"vv#asiiiia",  "age":12},    
    {"name":"Vasya7", "login":"vvasiiiia",  "age":23},    
    {"name":"Vasya8", "login":"vvasiiiia!",  "age":23}
]

a = [user['name'] for user in users3 if user['age']==12]
print(a)

b = [name.lower() for name in [user['name'] for user in users3 if user['age']==12]]
print(b)


d = {user['name']:len(user['name']) for user in users3 if user['age']==12}
print(d)
