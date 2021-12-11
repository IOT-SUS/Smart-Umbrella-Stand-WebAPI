from app import app

def authentication(req, res):
    res.message = 'authentication error!'
    res.statusCode = 400