from app import app
from models.devices import devicesSchema

class device():
    @staticmethod
    def infos(req, res):
        """devices information"""
        # search all deviecs information
        fake_devices = devicesSchema.find_all()

        # make response
        res.message = 'Get devices information successfully.'
        res.data    = fake_devices
        return res

    @staticmethod
    def info(req, res):
        """device information"""
        # get url variable
        device_id = req.url_variable['device_id']
        
        # search deviec information
        fake_device = devicesSchema.find(device_id)

        # make response
        res.message = 'Get devices information successfully.'
        res.data    = fake_device[device_id]
        return res