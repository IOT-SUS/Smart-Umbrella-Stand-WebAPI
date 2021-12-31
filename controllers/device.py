from app import app
from models.rents import rentsModel
from models.devices import devicesModel
from models.umbrellas import umbrellasModel

class device():
    
    @staticmethod
    def infos(req, res):
        """devices information"""
        # search all deviecs information

        devices = devicesModel.find_all()
        for s in range(len(devices)):
            del devices[s]['_id']
            amount = umbrellasModel.checkAmount(devices[s]['public_id'])
            devices[s]['amount'] = amount
            
        # make response
        res.message = 'Get devices information successfully.'
        res.data    = devices
        return res
 
    @staticmethod
    def info(req, res):
        """device information"""
        # get url variable
        device_id = req.url_variable['device_id']
       
        # search deviec information
        device = devicesModel.find(device_id)
        del device['_id']
 
        amount = umbrellasModel.checkAmount(device_id)
        device['amount'] = amount
 
        # make response
        res.message = 'Get devices information successfully.'
        res.data    = device
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
        # get url variable
        device_id = req.url_variable['device_id']
        
        # not done yet, this is for future work
        test = devicesModel.find(device_id)

        # get request data
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
    def update_status(req, res):
        """update device information"""
        # get url variable
        device_id = req.url_variable['device_id']
        
        # not done yet, this is for future work
        test = devicesModel.find(device_id)

        # get request data
        data = req.get_json()
        
        ip   = data['ip']
        wifi = data['wifi']
        
        updating = {
            'status': [ip, wifi]
        }
        devicesModel.update_status(device_id, updating)
 
        # make response
        res.message = 'Update device status successfully.'
        return res

    @staticmethod
    def delete(req, res):
        """user information"""
        # get url variable
        device_id = req.url_variable['device_id']
 
        devicesModel.delete(device_id)
 
        # make response
        res.message = 'Delete device successfully.'
        return res