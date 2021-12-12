from app import app
from models.users import usersSchema

class user():
    @staticmethod
    def info(req, res):
        """user information"""
        # get url variable
        user_id = req.url_variable['user_id']

        # search user
        fake_user = usersSchema.find(user_id)

        # make response
        res.message = 'Get user information successfully.'
        res.data    = fake_user
        return res