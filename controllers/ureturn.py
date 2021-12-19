import re
from app import app
from models.devices import devicesModel
from models.rents import rentsModel
from models.umbrellas import umbrellasModel

class ureturn():
    @staticmethod
    def checkAvailable(req, res):
        """"check device umbrella rent available"""
        # get url variable
        device_id = req.url_variable['device_id']
        
        # search device by id
        fake_device = devicesModel.find(device_id)

        # check amount
        available = True if fake_device['amount'] < 15 else False

        # make response
        res.message = 'Check device umbrella return successfully.'
        res.data    = {
            'available' : available
        }
        return res

    @staticmethod
    def returnUmbre(req, res):
        # get url variable
        device_id   = req.url_variable['device_id']

        # get request data
        data = req.get_json()
        umbrella_id = data['umbrella_id']

        umbrellasModel.update(umbrella_id, {"status_id" : device_id})

        # make response
        res.message = 'Check device umbrella return successfully.'
        return res