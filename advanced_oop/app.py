from advanced_oop.admin import Admin
from advanced_oop.databse import Database

a = Admin('rolf','1234',3)
a.save()

print(Database.find(lambda x: x['username'] == 'rolf'))

