from re import I
from app import app
from models.rrs import rrsModel
from models.umbrellas import umbrellasModel

class urent():
    @staticmethod
    def checkAvailable(req, res):
        """"check device umbrella rent available"""
        # get url variable
        device_id = req.url_variable['device_id']
        
        # search amount by device
        umbrella_amount = umbrellasModel.checkAmount(device_id)   
        
        # check amount
        available = True if umbrella_amount > 0 else False

        # make response
        res.message = 'Check device umbrella rent successfully.'
        res.data    = {
            'available' : available
        }
        return res

    @staticmethod
    def rentUmbrella(req, res):
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

        renter_status = {
            'action' : action,
            'status' : status,
            'user_id' : user_id,
            'device_id' : device_id
        }

        # insert renter_status to mongoDB
        rrsModel.add(renter_status)

        # make response
        res.message = 'Create rrs table of renter status successfully.'
        return res