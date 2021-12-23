from pymongo.common import partition_node
from app import app
from models.devices import devicesModel
from models.rents import rentsModel
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
    def delete(req, res):
        """user information"""
        # get url variable
        device_id = req.url_variable['device_id']
 
        devicesModel.delete(device_id)
 
        # make response
        res.message = 'Delete device successfully.'
        return res

    @staticmethod
    def rentSuccess(req, res):
         # get request data
        data = req.get_json()
        
        user_id          = data['user_id']
        rfid             = data['rfid']
        rent_device_id   = data['rent_device_id']

        # need to rfid user_id, rent_device_id, return_device_id
        rent_item = {
            'rfid'             : rfid,
            'user_id'          : user_id,
            'rent_device_id'   : rent_device_id
        }
        rentsModel.add(rent_item)
              
        res.message = 'Create rent table successfully'
        return res

    @staticmethod
    def returnSuccess(req, res):
        # get url variable
        rent_table_id = req.url_variable['rent_table_id']

         # get request data
        data = req.get_json()
        
        return_device_id = data['return_device_id']
        

        # need to update return_device_id
        return_item = {
            'return_device_id' : return_device_id
        }
        rentsModel.update(rent_table_id, return_item)
        
        return_res = rentsModel.find(rent_table_id)
        del return_res['_id']

        res.message = 'Update rent table successfully. The whole process has been completed.'
        res.data = return_res
        return res