from app import app
from models.devices import devicesModel

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