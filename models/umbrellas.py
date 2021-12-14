import uuid

from datetime import datetime

from flask_bcrypt     import Bcrypt
from app import app
from app import mongo

bcrypt = Bcrypt(app)

class umbrellasModel():

    @staticmethod
    def add(umbrella):
        now_time = datetime.now().isoformat()
        umbrella['public_id']  = str(uuid.uuid4())[:8]
        mongo.db.umbrellas.insert_one(umbrella)
        
    @staticmethod
    def find(umbrella_id):
        return list(mongo.db.umbrellas.find({'public_id': umbrella_id}))

    @staticmethod
    def find_all():
        return umbrellasModel.umbrellas

    @staticmethod
    def update(umbrella_id, update_query):
        mongo.db.umbrellas.update_one({'public_id': umbrella_id}, {'$set': update_query})
    
    @staticmethod
    def delete(umbrella_id):
        mongo.db.umbrellas.delete_one({'public_id': umbrella_id})


