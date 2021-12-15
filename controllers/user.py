from app import app
from models.users import usersModel

class user():
    
    @staticmethod
    def info(req, res):
        """user information"""
        # get token user id
        user_id = req.user_id

        # search user
        user = usersModel.find(user_id)
        del user['_id']

        # make response
        res.message = 'Get user information successfully.'
        res.data    = user
        return res

    @staticmethod
    def update(req, res):
        """user information"""
        # get token user id
        user_id = req.user_id
        data = req.get_json()

        # search user
        name       = data['name']
        email      = data['email']
        phone      = data['phone']

        updating = {
            'name' : name,
            'email' : email,
            'phone' : phone
        }


        usersModel.update(user_id, updating)

        # make response
        res.message = 'Update user information successfully.'
        return res

    @staticmethod
    def delete(req, res):
        """user information"""
        # get token user id
        user_id = req.user_id

        usersModel.delete(user_id)

        # make response
        res.message = 'Delete user account successfully.'
        return res