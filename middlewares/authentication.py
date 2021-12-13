from app import app
from libs.utils.jsonWebToken import jsonWebToken as jwt

def authentication(req, res):
    try:
        author  = req.headers['Authorization']
        token   = author.split(' ')[-1]
        user_id = jwt.validateToken(token)

        req.user_id = user_id
        res.message = 'Authentication successful!'
    except:
        res.message = 'Authentication error!'
        res.statusCode = 401