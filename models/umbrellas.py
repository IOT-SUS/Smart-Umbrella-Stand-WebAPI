import uuid

from re import A
from app import app
from app import mongo
from datetime import datetime
from flask_bcrypt     import Bcrypt

bcrypt = Bcrypt(app)

class umbrellasModel():

    @staticmethod
    def add(rfid):
        umbrella = {}
        now_time = datetime.now().isoformat()
        umbrella['public_id']  = str(uuid.uuid4())[:8]
        umbrella['created_at'] = now_time
        umbrella['updated_at'] = now_time
        umbrella['status_id']  = None
        umbrella['rfid']       = rfid
        mongo.db.umbrellas.insert_one(umbrella)
        return umbrella['public_id']
        
    @staticmethod
    def find(umbrella_id):
        return list(mongo.db.umbrellas.find({'public_id': umbrella_id}))

    @staticmethod
    def find_by_userID(user_id):
        return list(mongo.db.umbrellas.find({'status_id': user_id}))

    @staticmethod
    def find_by_deviceID(device_id):
        return list(mongo.db.umbrellas.find({'status_id': device_id}))    

    @staticmethod
    def find_by_rfid(rfid):
        return list(mongo.db.umbrellas.find({'rfid': rfid}))[0]

    @staticmethod
    def find_all():
        return list(mongo.db.umbrellas.find({}))

    @staticmethod
    def update(rfid, update_query):
        now_time = datetime.now().isoformat()
        update_query['updated_at'] = now_time
        mongo.db.umbrellas.update_one({'rfid': rfid}, {'$set': update_query})
    
    @staticmethod
    def delete(umbrella_id):
        mongo.db.umbrellas.delete_one({'public_id': umbrella_id})

    @staticmethod
    def checkAmount(device_id):
        temp = list(mongo.db.umbrellas.find({'status_id': device_id}))
        return len(temp)
            
