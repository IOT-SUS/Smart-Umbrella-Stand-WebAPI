import uuid

from datetime import datetime

from flask_bcrypt     import Bcrypt
from app import app
from app import mongo

bcrypt = Bcrypt(app)

class devicesModel():

    @staticmethod
    def add(device):
        device['public_id']  = str(uuid.uuid4())[:8]
        mongo.db.devices.insert_one(device)
        
    @staticmethod
    def find(device_id):
        return list(mongo.db.devices.find({'public_id': device_id}))

    @staticmethod
    def find_all():
        return devicesModel.devices

    @staticmethod
    def update(device_id, update_query):
        mongo.db.devices.update_one({'public_id': device_id}, {'$set': update_query})
    
    @staticmethod
    def delete(device_id):
        mongo.db.devices.delete_one({'public_id': device_id})


