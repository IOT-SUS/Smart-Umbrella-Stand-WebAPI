from app import app
from models.users import usersModel

class user():
    @staticmethod
    def info(req, res):
        """user information"""
        # get token user id
        user_id = req.user_id

        # search user
        fake_user = usersModel.find(user_id)

        # make response
        res.message = 'Get user information successfully.'
        res.data    = fake_user
        return res