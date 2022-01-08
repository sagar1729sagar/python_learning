from advanced_oop.databse import Database
class Savable:
    def save(self):
        Database.insert(self.to_dict())