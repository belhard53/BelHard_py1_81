from sqlalchemy import Column, Integer, String, Enum, ForeignKey
from sqlalchemy.orm import relationship, DeclarativeBase

# from sqlalchemy.ext.declarative import declarative_base # до Alh 2.0

class Base (DeclarativeBase):
    pass

class User(Base):
    __tablename__ = 'user'
    
    id = Column(Integer, primary_key=True)
    fname = Column(String(50), nullable=False)
    lname = Column(String(50), nullable=False)
    gender = Column(Enum('Male', 'Female', name='gender'), nullable=False)
    age = Column(Integer, nullable=False)
    
    phones = relationship('PhoneNumber', backref='user')

    # def __init__(self, name, **kw):
    #     super().__init__(**kw)
    #     self.fname = name

    def __repr__(self):
        return f"User(id={self.id}, fname='{self.fname}'," \
               f"lname='{self.lname}', gender='{self.gender}', " \
               f"age={self.age}, phones={self.phones})"

class PhoneNumber(Base):
    __tablename__ = 'phone_numbers'
    
    id = Column(Integer, primary_key=True)
    phone_type = Column(String(20), nullable=False)
    number = Column(String(20), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id')) # user.id - название таблицы
    
    def __init__(self, number, phone_type, **kw):
        super().__init__(**kw)
        self.phone_type = phone_type
        self.number = number
        
    
    # если вместо back_populates использовать  backref - можно не писать
    # user1 = relationship('User', backref='phones1')

    def __repr__(self):
        return f"PhoneNumber(id={self.id}, phone_type='{self.phone_type}', " \
                           f"number='{self.number}', user_id={self.user_id})"

def add_data(engine, db):
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    
    # user1 = User(fname = "Max1", lname="Maxovich", age=33, gender="Male")
    # user2 = User(fname = "Max2", lname="Maxovich", age=33, gender="Male")
    # user3 = User(fname = "Max3", lname="Maxovich", age=33, gender="Male")
    
    # db.add(user1)
    # db.add(user2)
    # db.add(user3)
    
    users = [
        User(fname = "Max1", lname="Maxovich", age=33, gender="Male"),
        User(fname = "Max2", lname="Maxovich", age=33, gender="Male"),
        User(fname = "Max3", lname="Maxovich", age=33, gender="Male"),
        User(fname = "Max4", lname="Maxovich", age=33, gender="Male"),
        User(fname = "Max5", lname="Maxovich", age=33, gender="Male")
     ]
    
    user1 = User(fname = "Max6", lname="Maxovich", age=33, gender="Male")
    user2 = User(fname = "Max66", lname="Maxovich", age=33, gender="Male")
    
    phone1 = PhoneNumber(phone_type = "type1", number='11111', user=user1)
    phone2 = PhoneNumber(phone_type = "type2", number='2222', user=user2)
    phone3 = PhoneNumber(phone_type = "type1", number='3333', user=users[0])
    phone3 = PhoneNumber(phone_type = "type2", number='3333', user=users[0])
    
    
    # телефоны добавлять не нужно т.к. они привязаны к пользователям и сами добавятся
    db.add_all(users + [user1, user2])
    db.commit()
    
    