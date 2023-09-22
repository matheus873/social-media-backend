from database.mongo import users_collection, posts_collection

class AbstractRepository:
    def __init__(self, collection):
        self.collection = collection
        
    def create(self, data):
        return self.collection.insert_one(data).inserted_id
    
    def update_one(self, query, data):
        return self.collection.update_one(query, data)

    
    