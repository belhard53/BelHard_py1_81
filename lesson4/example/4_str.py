# s = "Hello Python"
# print(len(s)) # длина

# print(s.isdigit())
# b = s.find("P")
# print(s.find("P", b + 1)) # искать дальше
# ok = b > -1

# ok = "p" in s
# print(ok)


# # ФОРМАТИРОВАНИЕ
# name = "Vasya"
# age = 22
# print("Привет я %s мне %d года" % (name, age))
# print("Привет я {} мне {} года".format(name, age))
# print("Привет я {1} мне {0} года".format(age, name))
# print("Привет я {name1} мне {age1} года".format(name1=name, age1=age))
# print(f"Привет я {name} мне {age} года")
# print(f"Привет я {name:*<15} мне {age} года") # дополнят * до 12 знаков
# print(f"Привет я {name:=^15} мне {age} года")
# b = 12345678
# print(f"Сумма - {b:,}")
# print(f"Сумма - {b:_}")
# print(f"Сумма - {12.12162876:.3f}")
# print(f"Сумма - {323123:010}") # дополнят нулями до 10 знаков
# print(f"Сумма - {323123:010d}") # дополнят нулями до 10 знаков
# print("{}:{:02}:{:02}".format(12, 1, 2)) # время




# # СРЕЗЫ
# s = "0123456789"
# a = s[4]
# a = s[-4]
# a = s[4:7]
# a = s[2:] # до последнего 
# a = s[:6] # от первого
# a = s[::-1]
# a = s[-4:-2]

# print("12635476542342622".count("2"))
# print("{} -  {}".format(1, "hello"))


# a = input()
# b = a.lower()
# a = input().lower()
# b = a.upper()

# a = "hello"
# print(a.capitalize())
# print(a.center(50,'*'))
# print(a.ljust(50,'*'))
# print(a.rjust(50,'*'))
# print(a.zfill(15)) 

a = "12311"
# print(a.isalpha())
# print(a.isalnum())
# print(a.isdigit())
# print(a.isnumeric())

# text = "Hello world"
# print(text.endswith("rld"))
# print(text.startswith("Hel", 1, 7))

# print(text.removeprefix("Hell"))
# print(text.removesuffix("rld"))


# print("1234 92380 830928".replace("1234", "4321").replace("3", "__"))



# s = "1 3 25 56 33"
# a = s.split(' ')          
# a = s.split() # пробел по умолчанию      
# a = s.rsplit(sep="56", maxsplit=1) # сплит справа и только 1 раз    
# print(a) # print(1, 3, 25...)
# b = list(map(int, a))
# b = list(map(int, s.split()))

# print(a)
# c = "/ - -  /".join(a)
# print(c)

# sum([1,2,3])
# max(1, 2, 3)
# min()

# print(ord("A"))
# print("A" > "aaa")

# a = b'hello'
# b = "Hello пайтон".encode() # в байтовое представление
# print(b)
# print(b.decode("utf-8"))
# print(b.decode("cp1251")) 
# c = b.decode() # в строку
# print(c)


# множественная замена подстрок
# a = "Однажды, в студеную зимнюю пору"
# b = a.maketrans({"а":"А","у":"У","и":"И"})
# b = a.translate(b)
# print(b)

