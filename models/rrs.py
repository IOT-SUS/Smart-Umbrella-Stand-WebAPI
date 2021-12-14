import uuid

from datetime import datetime

from flask_bcrypt     import Bcrypt
from app import app
from app import mongo

bcrypt = Bcrypt(app)

class rrsModel():

    @staticmethod
    def add(rrs):
        now_time = datetime.now().isoformat()
        rrs['public_id']  = str(uuid.uuid4())[:8]
        rrs['current_time'] = now_time
        mongo.db.rrs.insert_one(rrs)
        
    @staticmethod
    def find(rrs_id):
        return list(mongo.db.rrs.find({'public_id': rrs_id}))

    @staticmethod
    def find_all():
        return rrsModel.rrs

    @staticmethod
    def update(rrs_id, update_query):
        mongo.db.rrs.update_one({'public_id': rrs_id}, {'$set': update_query})
    
    @staticmethod
    def delete(rrs_id):
        mongo.db.rrs.delete_one({'public_id': rrs_id})


