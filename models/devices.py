import uuid

from datetime import datetime 
from flask_bcrypt     import Bcrypt
from app import app
from app import mongo

bcrypt = Bcrypt(app)
 
class devicesModel():
 
    @staticmethod
    def add(device):
        now_time = datetime.now().isoformat()
        device['public_id']         = str(uuid.uuid4())[:8]
        device['status']            = [None, None]
        device['status_updated_at'] = now_time
        mongo.db.devices.insert_one(device)
        return device['public_id']
       
    @staticmethod
    def find(device_id):
        return list(mongo.db.devices.find({'public_id': device_id}))[0]
 
    #find by locaiotn
    @staticmethod
    def find_by_loc(location):
        return list(mongo.db.devices.find({'location': location}))
 
    @staticmethod
    def find_all():
        return list(mongo.db.devices.find({}))
 
    @staticmethod
    def update(device_id, update_query):
        mongo.db.devices.update_one({'public_id': device_id}, {'$set': update_query})
    
    @staticmethod
    def update_status(device_id, update_query):
        now_time = datetime.now().isoformat()
        update_query['status_updated_at'] = now_time
        mongo.db.devices.update_one({'public_id': device_id}, {'$set': update_query})

    @staticmethod
    def delete(device_id):
        mongo.db.devices.delete_one({'public_id': device_id})