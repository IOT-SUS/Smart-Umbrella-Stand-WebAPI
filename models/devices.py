import uuid

from app import app
from app import mongo
from datetime import datetime
from flask_bcrypt     import Bcrypt

bcrypt = Bcrypt(app)

class devicesModel():

    @staticmethod
    def add(device):
        now_time = datetime.now().isoformat()
        device['public_id']  = str(uuid.uuid4())[:8]
        device['created_at'] = now_time
        device['updated_at'] = now_time
        mongo.db.devices.insert_one(device)
        
    @staticmethod
    def find(device_id):
        return list(mongo.db.devices.find({'public_id': device_id}))

    @staticmethod
    def find_all():
        return devicesModel.devices

    @staticmethod
    def update(device_id, update_query):
        now_time = datetime.now().isoformat()
        update_query['updated_at'] = now_time
        mongo.db.devices.update_one({'public_id': device_id}, {'$set': update_query})
    
    @staticmethod
    def delete(device_id):
        mongo.db.devices.delete_one({'public_id': device_id})
