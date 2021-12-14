import uuid

from datetime import datetime

from flask_bcrypt     import Bcrypt
from app import app
from app import mongo

bcrypt = Bcrypt(app)

class rentsModel():

    @staticmethod
    def add(rents):
        now_time = datetime.now().isoformat()
        rents['public_id']  = str(uuid.uuid4())[:8]
        rents['return_device_id']  = None
        rents['rent_time']  = now_time
        rents['return_time']  = None
        mongo.db.rents.insert_one(rents)
        
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


