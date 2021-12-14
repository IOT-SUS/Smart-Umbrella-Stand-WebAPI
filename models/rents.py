import uuid
from app import app
from app import mongo
from datetime import datetime
from flask_bcrypt     import Bcrypt

bcrypt = Bcrypt(app)

class rentsModel():

    @staticmethod
    def add(rent):
        now_time = datetime.now().isoformat()
        rent['public_id']  = str(uuid.uuid4())[:8]
        rent['return_device_id']  = None
        rent['rent_time']  = now_time
        rent['return_time']  = None
        mongo.db.rents.insert_one(rent)
        
    @staticmethod
    def find(rent_id):
        return list(mongo.db.rents.find({'public_id': rent_id}))

    @staticmethod
    def find_all():
        return rentsModel.rents

    @staticmethod
    def update(rent_id, update_query):
        mongo.db.rents.update_one({'public_id': rent_id}, {'$set': update_query})
    
    @staticmethod
    def delete(rent_id):
        mongo.db.rents.delete_one({'public_id': rent_id})


