from advanced_oop.admin import Admin
from advanced_oop.databse import Database
from advanced_oop.user import User

a = Admin('rolf','1234',3)
a.save()

u = User('Sag','password')

print(Database.find(lambda x: x['username'] == 'rolf'))

users = [a, u]
for user in users:
    user.save()

