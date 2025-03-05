# mongod --dbpath D:\PROGRAMS\mongoDB\bin\db\
    
# служба - C:\MongoDb\mongod.exe --config C:\MongoDb\mongo.config --install
"""mongo.config
        dbpath=C:\MongoDb\data
        logpath=C:\MongoDb\log\mongo.log"""
        
        
from pymongo import MongoClient        

client = MongoClient()

# client = MongoClient('localhost', 27017)
# client = MongoClient('mongodb://localhost:27017/')

db = client.test4

# users = db.users4 # выбрать коллекцию или создать
users = db["users6"] # выбрать коллекцию или создать

print(db.list_collection_names())

d1 = {"name": "John0", "address": "Highway4"}
x = users.insert_one(d1)
print(x)

x = users.find_one()
print(x)

x = users.find() # -> Cursor
x = users.find({"address": "Highway2"})
x = users.find({"address": "Highway2"}).limit(2)
x = users.find({"address": "Highway2"}).skip(2).limit(2)
x = users.find({"address": "Highway2"}).skip(2)
x = users.find({},{"name": True}).sort('name')
print(x)

for user in x:
    print(user)
    # print(user['name'])
