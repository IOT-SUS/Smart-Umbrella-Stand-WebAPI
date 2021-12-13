import datetime

from app import app
from libs.utils.jsonWebToken import jsonWebToken as jwt

class auth():
    @staticmethod
    def login(req, res):
        """"user login"""
        # get request data
        data = req.get_json()

        email    = data['email']
        password = data['password']

        # search users by email
        # check password

        fake_user_id = 'ef8697123'
        
        # create json web token
        token = jwt.createToken(user_id=fake_user_id)

        # make response
        res.message = 'Login successfully.'
        res.data    = {
            'token' : token
        }
        return res

    @staticmethod
    def signup(req, res):
        """"user signup"""
        # get request data
        data = req.get_json()
        
        email    = data['email']
        password = data['password']
        # need to add phone, name, birthday

        # check if email already exist...

        # create user
        # ...

        # make response
        res.message = 'Created successfully.'
        return res