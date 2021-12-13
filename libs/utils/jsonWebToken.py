import jwt
import datetime

from app import app

EXPIRE_TIME = app.config['TOKEN_EXPIRE_TIME']
SECRET_KEY  = app.config['TOKEN_SECRET_KEY']

class jsonWebToken():
    @staticmethod
    def createToken(user_id):
        payload = {
            'user_id': user_id,
            'exp'    : datetime.datetime.utcnow() + datetime.timedelta(minutes=EXPIRE_TIME)
        }
        return (jwt.encode(payload, SECRET_KEY)).decode('UTF-8')

    @staticmethod
    def validateToken(token):
        jwt_info = jwt.decode(token, SECRET_KEY)
        return jwt_info['user_id']
        