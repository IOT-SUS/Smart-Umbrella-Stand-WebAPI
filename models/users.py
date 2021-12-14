from app import app
from app import mongo
from flask_bcrypt     import Bcrypt
from datetime import datetime
import uuid

bcrypt = Bcrypt(app)

class usersModel():
    
    @staticmethod
    def add(user):
        now_time = datetime.now().isoformat()
        user['password']   = bcrypt.generate_password_hash(user['password']).decode('utf-8')
        user['public_id']  = str(uuid.uuid4())[:8]
        user['created_at'] = now_time
        user['updated_at'] = now_time
        user['admin']      = False
        mongo.db.users.insert_one(user)
    
    @staticmethod
    def find(user_id):
        return list(mongo.db.users.find({'public_id': user_id}))

    @staticmethod
    def login(email, password):
        user = mongo.db.users.find({'email': email})[0]
        return bcrypt.check_password_hash(user['password'], password)

    @staticmethod
    def update(user_id, update_query):
        now_time = datetime.now().isoformat()
        update_query['updated_at'] = now_time
        mongo.db.users.update_one({'public_id': user_id}, {'$set': update_query})

    @staticmethod
    def delete(user_id):
        mongo.db.users.delete_one({'public_id': user_id})   

    @staticmethod
    def find_user_by_email(email):
        user = mongo.db.users.find({'email': email})[0]
        return user['public_id'] 

#2021