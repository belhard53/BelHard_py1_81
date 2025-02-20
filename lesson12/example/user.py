# ООП

class User:
    login = '__'
    password = '123'
    
    @staticmethod
    def calc_age(age):
        return 2025 - age
    
    @classmethod
    def change_login(cls, new_login):
        cls.login = new_login
    
     
    # конструктор
    def __init__(self, name, sn, age):
        # name = 'Вася'
        self.name = name
        self.surname = sn
        self.age = age
        self.projects = []
        
    # для пользователя
    def __str__(self):
        return f"{self.name} {self.surname}"
    
    # для машины 
    def __repr__(self):
        return f"User('{self.name}', '{self.surname}', {self.age})"
    
    def __len__(self):
        return len(self.projects)
    
    def __eq__(self, other_obj):
        return self.surname == other_obj.surname
    
    def __lt__(self, other_obj):
        return self.age < other_obj.age
    
    # аналогично
    # __ne__(self, other)   obj1 != obj2
    # __le__(self, other)   obj1 <= obj2
    # __gt__(self, other)   obj1 >  obj2
    # __ge__(self, other)   obj1 >= obj2
    
    
    def __call__(self, *args, **kwds):
        print(f"Я {self.name}")
    
    def info(self):
        print(f"{self.name} {self.surname} {self.age} {self.login} {self.projects}")
        return 1
    
    def info2(self):
        a = self.info()
        print('еще принт')
    
    def proj_add(self, proj):
        
        self.projects.append(proj)
    


class Users:
    def __init__(self):
        self.users = []
        self.n = 0

    # делает объект итерируемым      
    def __iter__(self):
        return iter(self.users)

    def __next__(self):
        if self.n >= len(self.users):
            raise StopIteration
        res =  self.users[self.n]
        self.n+=1
        return res

    def add_user(self, user):        
        self.users.append(user)
        
    def __getitem__(self, key):
        return self.users[key] 
    
    def __setitem__(self, key, value):
        self.users[key] = value


if __name__ == "__main__":
    user1 = User('Вася', "Васечкин", 33)    
    user2 = User('Петя', "Петячкин", 25)
    user3 = User('Вася2', "Васечкин", 22)
    
    group1 = Users()
    group1.add_user(user1)
    group1.add_user(user2)
    group1.add_user(user2)
    
    print(group1[2]) # getitem
    group1[2] = user3 # setitem
    print(group1[2]) # getitem
    

    # user1() # вызывается __call__


    # # print(user1.password)
    # # print(user2.password)
    # # print(user1.age)
    # # print(user2.age)
    # user1.age = 40
    # # user1.login = "vvvv"
    # # user2.login = "pppp"

    # user1.proj_add('pr1')
    # user2.proj_add('pr2')
    
    # # user1.info()
    # # user2.info()

    # # print(len(user1)) # __len__

    # print(user1 == user3) # __eq__
    # print(user1 < user3) # __lt__

    # users = [user1, user2, user3]

    # users.sort() # сортировка возможна т.к. есть __lt__
    # print(users)
    
    # ------------------------------
    # user2.login = "login_user2"
    # print(user2.login)
    
    # User.change_login("new_login1")
    # print(User.login)
    # user1.__class__.login = "new_login2" # можно еще так менять
    # print(User.login)    
    
    # user4 = User("User4", "User44", 55)    
    # print(2, user2.login) # остался такой же как и был
    # print(3, user3.login) # поменялся т.к. изначально было значение из класса по дефолту, хоть и создавался до изменения cls
    # print(4, user4.login) # новый пользователь создан с новым логином 


    # ------------------------------------
    # # user1.name
    # a = "name"
    # getattr(user1, a)
    # setattr(user1, "name2", "qwiuqyiw")
    # delattr()

    # -------------------------------------------
    try:
        print(next(group1)) # __next__
        print(next(group1)) # __next__
        print(next(group1)) # __next__
        print(next(group1)) # __next__
    except StopIteration:
        print('больше нет')
        
    for user in group1: # __iter__
        print(user)
        
    print(list(group1)) # __iter__


