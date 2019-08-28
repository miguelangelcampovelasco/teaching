
from pymongo import MongoClient

uri = "mongodb://useradmin:@liuhoward.tk"
client = MongoClient(uri)
db = client.get_database('admin')
print(db.name)

user_list = list()
with open('mis584_userlist.csv') as fp:
    for line in fp:
        user = line.replace('#', '').strip()
        user_list.append(user)

for user in user_list:
    db.command("createUser", user, pwd=f'{user}123', roles=[{ "role": "readWrite", "db": f"bigdata_{user}" },{"role": "read", "db": "Northwind" }])
    #db.command("dropUser", user)
    #client.drop_database(f'bigdata_{user}')
