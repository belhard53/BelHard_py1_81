# Создание таблиц
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from models2 import User, PhoneNumber, add_data

engine = create_engine('sqlite:///test3.db')

# до v.2.0
# from sqlalchemy.orm import sessionmaker
# Session = sessionmaker(autoflush=False, bind=engine)

#drop_all
# Base.metadata.create_all(engine)

with Session(autoflush=False, bind=engine) as db:
    add_data(engine, db)
    
    
    # ------  READ  ----
    users = db.query(User).all()
    # users = db.query(User).one()
    print(*users, sep="\n")
    print()
    for user in users:
        print(user, user.fname)                        
    db.commit()
    
    user = db.get(User, 1)    
    print(user)
    for phone in user.phones:
        print(phone.phone_type, phone.number)
    
    
    user = db.query(User).filter_by(id=2).one()    
    users = db.query(User).filter(User.id>3).all()
    
    
    from sqlalchemy import or_
    users = db.query(User).filter(or_(User.fname=='Max1', User.fname=='Max2')).all()
    print(users)
    
    from sqlalchemy import or_
    users = db.query(User).filter(User.fname.like(r'%ax6%')).all()
    print(users)
    
    
    
    # ------  UPDATE  ----
    user = db.get(User, 1)    
    user.fname = "Gerald"
    user.phones.append(PhoneNumber('12345678', 'mts'))       
    user.phones[0].number = '99999999'
    db.commit()
    
    user = db.get(User, 1)    
    print(user)
    print(*user.phones, sep='\n')
    
    
    # ------  DELETE  ----    
    user = db.get(User, 1)    
    db.delete(user)    
    db.commit()
    
    user = db.get(User, 6)    
    print(user.phones)
    user.phones.pop()
    print(user.phones)
    
    
    user = db.get(User, 7)    
    print(user.phones)
    phone = user.phones[0]
    user.phones.remove(phone)
    print(user.phones)
    
    # ----------------------- pydantic
    
    input_user_json = """
    {        
        "fname": "John",
        "lname": "Doe",
        "gender": "Male",
        "age": 30,    
        "phones": [
            {"phone_type": "Мобильный", "number": "1111111111"},
            {"phone_type": "Рабочий", "number": "222222222"}
        ]
    }"""
    
    from schemas import UserSchema, PhoneNumberSchema
    
    user_s = UserSchema.model_validate_json(input_user_json) # проверка (валидация)
    phones = [PhoneNumber(**phone.model_dump()) for phone in user_s.phones]
    user_s.phones = []    
    user = User(**user_s.model_dump())    
    print(user)
    user.phones += phones
    db.add(user)
    db.commit()
    print(user)
    