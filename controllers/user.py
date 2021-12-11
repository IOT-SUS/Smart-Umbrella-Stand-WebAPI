from app import app

class user():
    @staticmethod
    def info(req, res):
        """user information"""
        # search user
        fake_user = {
            'id'        : 'ef8697123',
            'name'      : '王小明',
            'email'     : 'dummy@gmail.com',
            'subscriber': True,
            'status'    : 0
        }

        # make response
        res.message = 'Get user information successfully.'
        res.data    = fake_user
        return res