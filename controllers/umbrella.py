from app import app
from models.umbrellas import umbrellasModel
from os import device_encoding

class umbrella():
    
    @staticmethod
    def add(req, res):
        """Add a new umbrella"""
        # get request data
        data = req.get_json()

        # extract rfid from data
        rfid = data['rfid']

        new_umbrella = umbrellasModel.add(rfid)
        
        # make response
        res.message = 'Add new umbrella successfully.'
        res.data    = new_umbrella
        return res
    
    @staticmethod
    def record(req, res):
        """"check umbrell record"""
        # get url variable
        user_id = req.url_variable['user_id']

        # search umbrella table by user_id
        umbrella_data = umbrellasModel.find_by_userID(user_id)
        
        for data in umbrella_data:
            del data['_id']
    
        # make response
        res.message = 'Check umbrella records successfully.'
        res.data    = {
            'records' : umbrella_data
        }
        return res

    @staticmethod
    def records(req, res):
        # search all umbrella table
        umbrella_data = umbrellasModel.find_all()

        for data in umbrella_data:
            del data['_id']

        # make response
        res.message = 'Check all umbrella records successfully, total amounts of umbrella: ' + str(len(umbrella_data))
        res.data    = {
            'records' : umbrella_data
        }
        return res
