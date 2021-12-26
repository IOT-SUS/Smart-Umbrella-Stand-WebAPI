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
        rent['public_id']         = str(uuid.uuid4())[:8]
        rent['return_device_id']  = None
        rent['return_time']       = None
        rent['rent_time']         = now_time
        mongo.db.rents.insert_one(rent)
        return rentsModel.find(rent['public_id'])

    @staticmethod
    def find(rent_id):
        return list(mongo.db.rents.find({'public_id': rent_id}))[0]

    @staticmethod
    def find_by_user(user_id):
        return list(mongo.db.rents.find({'user_id': user_id}))

    @staticmethod
    def find_by_rfid(rfid):
        return list(mongo.db.rents.find({'rfid': rfid, 'return_time': None}))[0]

    @staticmethod
    def find_all():
        return list(mongo.db.rents.find({}))

    @staticmethod
    def update(rent_id, update_query):
        now_time = datetime.now().isoformat()
        update_query['return_time'] = now_time
        mongo.db.rents.update_one({'public_id': rent_id}, {'$set': update_query})
        return rentsModel.find(rent_id)
    
    @staticmethod
    def delete(rent_id):
        mongo.db.rents.delete_one({'public_id': rent_id})


