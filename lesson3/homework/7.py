'''
Запросить логин и пароль.
Вывести - True/False  соответственно
если ввели логин - 'admin', пароль - '12345'.
Формат вывода: "Логин:True / Пароль:True"

'''

login = input("login : ")
password = input("password : ")
print(f"Логин:{login == 'admin'} / Пароль:{password == '12345'}")


# --------------------------------2

login = input("Введите логин: ")
password = input("Введите пароль: ")

is_login_correct = login == 'admin'
is_password_correct = password == '12345'

print(f"Логин: {is_login_correct} / Пароль: {is_password_correct}")