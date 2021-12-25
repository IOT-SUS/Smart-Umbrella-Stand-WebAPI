import uuid
import datetime
from app import app
from app import mongo
from flask_bcrypt     import Bcrypt

bcrypt = Bcrypt(app)

class rrsModel():

    @staticmethod
    def add(rrs):
        now_time = datetime.datetime.now()
        rrs['public_id']  = str(uuid.uuid4())[:8]
        rrs['current_time'] = now_time.isoformat()
        rrs['expire_time'] = (now_time + datetime.timedelta(minutes=1)).isoformat()
        mongo.db.rrs.insert_one(rrs)
        return rrsModel.find(rrs['public_id'])

    @staticmethod
    def find(rrs_id):
        return list(mongo.db.rrs.find({'public_id': rrs_id}))[0]

    @staticmethod
    def find_all():
        return rrsModel.rrs

    @staticmethod
    def update(rrs_id, update_query):
        mongo.db.rrs.update_one({'public_id': rrs_id}, {'$set': update_query})
    
    @staticmethod
    def delete(rrs_id):
        mongo.db.rrs.delete_one({'public_id': rrs_id})

    # For device to searching rrs table 
    @staticmethod
    def find_by_device(device_id, action, status):
        now_time = datetime.datetime.now().isoformat()

        return list(mongo.db.rrs.find({'device_id': device_id, 
                                       'action' : action, 
                                       'status' : status, 
                                       'expire_time' : {"$gte" : now_time}}))[0]

    # For user to searching rrs table 
    @staticmethod
    def find_by_user(user_id, action, status):
        now_time = datetime.datetime.now().isoformat()

        return list(mongo.db.rrs.find({'user_id': user_id, 
                                       'action' : action, 
                                       'status' : status, 
                                       'expire_time' : {"$gte" : now_time}}))[0]