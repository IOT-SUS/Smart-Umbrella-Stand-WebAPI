import re

from pymongo.common import partition_node
from app import app
from models.devices import devicesModel
from models.rents import rentsModel
from models.umbrellas import umbrellasModel

class ureturn():
    @staticmethod
    def checkVacancy(req, res):
        """"check device umbrella rent available"""
        # get url variable
        device_id = req.url_variable['device_id']
        
        # check vacancies
        vacancy = umbrellasModel.checkAmount(device_id) 

        # check amount
        available = True if vacancy < 5 else False

        # make response
        res.message = 'Check device umbrella return successfully.'
        res.data    = {
            'available' : available
        }
        return res

    @staticmethod
    def returnUmbrella(req, res):
        # get url variable
        device_id   = req.url_variable['device_id']
        
        # search db and check if there has a match device id
        device = devicesModel.find(device_id)

        # get request data
        data = req.get_json()
        
        rfid = data['rfid']
        #print(umbrella_id)
        umbrellasModel.update(rfid, {"status_id" : device_id})

        # make response
        res.message = 'Return umbrella successfully.'
        return res