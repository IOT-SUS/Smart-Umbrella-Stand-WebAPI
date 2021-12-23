import re

from pymongo.common import partition_node
from app import app
from models.devices import devicesModel
from models.rents import rentsModel
from models.rrs import rrsModel
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
        """check device umbrella rent available"""
        # get url variable
        device_id = req.url_variable['device_id']

        # get request data
        data = req.get_json() 

        # need to add action, status, user_id, device_id
        action    = data['action']
        status    = data['status']
        user_id   = data['user_id'] 
        device_id = data['device_id']

        returner_status = {
            'action' : action,
            'status' : status,
            'user_id' : user_id,
            'device_id' : device_id
        }

        # insert renter_status to mongoDB
        rrsModel.add(returner_status)

        # make response
        res.message = 'Create rrs table of returner status successfully.'
        return res