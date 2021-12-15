from os import device_encoding
from app import app
from models.devices import devicesModel
 
class device():
    @staticmethod
    def infos(req, res):
        """devices information"""
        # search all deviecs information
        fake_devices = devicesModel.find_all()
 
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
        fake_device = devicesModel.find(device_id)
 
        # make response
        res.message = 'Get devices information successfully.'
        res.data    = fake_device
        return res
 
    @staticmethod
    def add(req, res):
        """add new device"""
        # get request data
        data = req.get_json()
       
        location       = data['location']
        embedded_code  = data['embedded_code']
 
        if devicesModel.find_by_loc(location) :
            # make error response
            res.message = 'error: duplicate device.'
        else:
            device = {
                'location' : location,
                'embedded_code' : embedded_code,
            }
            device_id=devicesModel.add(device)
 
            # make response
            res.message = 'Created device successfully.'
            res.data    = {
                'device_id' : device_id
            }
        return res
 
    @staticmethod
    def update(req, res):
        """update device information"""
        # get token device id
        device_id = req.device_id
        data = req.get_json()
 
        location        = data['location']
        embedded_code   = data['embedded_code']
        updating = {
            'location'      : location,
            'embedded_code' : embedded_code
        }
        devicesModel.update(device_id, updating)
 
        # make response
        res.message = 'Update device information successfully.'
        return res
 
    @staticmethod
    def delete(req, res):
        """user information"""
        # get token device id
        device_id = req.device_id
 
        devicesModel.delete(device_id)
 
        # make response
        res.message = 'Delete device successfully.'
        return res
 
   
   

