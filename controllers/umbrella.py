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