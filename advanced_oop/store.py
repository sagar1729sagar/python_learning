from advanced_oop.databse import Database

class Store:
    def to_dict(self):
        pass

    def save(self):
        Database.insert(self.to_dict())
