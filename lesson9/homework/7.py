"""
Дан список пользователей след. формата: 
[{"name":"some_name", "login":"some_login", "password":"some_password" },
 ...
]

Отфильтровать используя функцию filter() список на предмет паролей 
которые менее 5 символов.

*Отфильтровать используя функцию filter() список на предмет валидных логинов. 
Валидный логин должен содержать только латинские буквы, цифры и черту подчеркивания. 
Каждому пользователю с плохим логином вывести текст 
"Уважаемый user_name, ваш логин user_login не является корректным."

"""


import re

users_list = [
    {"name":"Vasya", "login":"vas", "password":"123456"},
    {"name":"Denis", "login":"Denis123", "password":"qwesdr"},
    {"name":"Petya", "login":"Petr.1", "password":"password"}
]

def check_login(login):
    return re.match(r'^[a-zA-Z0-9_]+$', login) is not None

wrong_pass = list(filter(lambda user: len(user["password"]) < 5, users_list))
if wrong_pass:
    print(wrong_pass)
# [{'name': 'Denis', 'login': 'Denis123', 'password': 'qwer'}]

valid_logins = list(filter(lambda user: check_login(user["login"]), users_list))

wrong_logins = list(filter(lambda user: not check_login(user["login"]), users_list))
for user in wrong_logins:
    print(f"Уважаемый {user['name']}, ваш логин {user['login']} не является корректным.")