import datetime

from models.users import usersModel
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
        validation = usersModel.login(email, password) # True or False
        if validation == False:
            res.message = 'Login failed.'
            res.statusCode = 403
            return res
        
        # create json web token
        user_id = usersModel.find_user_by_email(email)
        token = jwt.createToken(user_id = user_id)

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
        
        name       = data['name']
        email      = data['email']
        password   = data['password']
        birthday   = data['birthday']
        phone      = data['phone']

        # need to add phone, name, birthday
        user = {
            'name' : name,
            'email' : email,
            'password' : password,
            'birthday' : birthday,
            'phone' : phone
        }
        usersModel.add(user)

        # check if email already exist...

        # create user
        # ...

        # make response
        res.message = 'Created successfully.'
        return res
