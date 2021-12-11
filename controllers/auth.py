from app import app

class auth():
    @staticmethod
    def login(req, res):
        """"user login"""
        # get request data
        data = req.get_json()

        email    = data['email']
        password = data['password']

        # do some user vaildation
        # ...

        # make response
        res.message = 'Login successfully.'
        res.data    = {
            'token' : app.config['FAKE_TOKEN']
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

        # create user
        # ...

        # make response
        res.message = 'Created successfully.'
        return res