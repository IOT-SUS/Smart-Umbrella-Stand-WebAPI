from app import app
from models.users import usersModel

def adminAuthentication(req, res):
    try:
        user_id = req.user_id
        user    = usersModel.find(user_id)

        assert user['admin'] == True

        res.message = 'Admin authentication successful!'
    except:
        res.message = 'Admin authentication error!'
        res.statusCode = 401