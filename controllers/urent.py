from models.rents     import rentsModel
from models.umbrellas import umbrellasModel

from controllers.urrs import urrs

class urent():
    
    @staticmethod
    def record(req, res):
        """"check rent record"""
        # get user id
        user_id   = req.user_id

        # search rent table by user_id
        rent_data = rentsModel.find_by_user(user_id)       
        
        for data in rent_data:
            del data['_id']
    
        # make response
        res.message = 'Check rent records successfully.'
        res.data    = {
            'records' : rent_data
        }
        return res

    @staticmethod
    def records(req, res):
        """"check rent record"""
        # search rent table by user_id
        rent_data = rentsModel.find_all()       
        
        for data in rent_data:
            del data['_id']
    
        # make response
        res.message = 'Check all rent records successfully.'
        res.data    = {
            'records' : rent_data
        }
        return res

    @staticmethod
    def add(req, res):
        """"add rent"""
        # check Available
        res = urent.checkAvailable(req, res)
        assert res.data['available'] == True
        
        # add rrs table
        res = urrs.addRent(req, res)
        return res

    @staticmethod
    def checkAvailable(req, res):
        """"check device umbrella rent available"""
        # get url variable
        device_id = req.url_variable['device_id']
        
        # search amount by device
        umbrella_amount = umbrellasModel.checkAmount(device_id)   
        
        # check amount
        Available = True if umbrella_amount > 0 else False

        # make response
        res.message = 'Check device umbrella rent successfully.'
        res.data    = {
            'available' : Available
        }
        return res

    @staticmethod
    def success(req, res):
        # get url variable
        device_id = req.url_variable['device_id']

        # get request data
        data = req.get_json()
        
        user_id = data['user_id']
        rfid    = data['rfid']
        
        # check umbrella is belong to this device
        umbrella = umbrellasModel.find_by_rfid(rfid)
        del    umbrella['_id']
        assert umbrella['status_id'] == device_id

        # need to rfid user_id, rent_device_id, return_device_id
        rent_item = {
            'rfid'           : rfid,
            'user_id'        : user_id,
            'rent_device_id' : device_id
        }

        # update rrs rent table
        res = urrs.update(req, res)

        # update umbrella status id
        umbrellasModel.update(rfid, {'status_id': user_id})

        rent_data = rentsModel.add(rent_item)
        del rent_data['_id']

        res.message = 'Create rent table successfully'
        res.data    = rent_data
        return res
