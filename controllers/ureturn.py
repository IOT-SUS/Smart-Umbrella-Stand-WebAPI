from models.rents     import rentsModel
from models.umbrellas import umbrellasModel

from controllers.urrs import urrs

class ureturn():
        
    @staticmethod
    def add(req, res):
        """"add return"""
        # get url variable
        device_id = req.url_variable['device_id']

        # get request data
        data = req.get_json()
        
        rfid    = data['rfid']

        # check umbrella rfid
        rent_reocrd = rentsModel.find_by_rfid(rfid)
        req.user_id = rent_reocrd['user_id']

        # check vacancy
        res = ureturn.checkVacancy(req, res)
        assert res.data['vacancy'] == True

        # create rrs table
        res = urrs.addReturn(req, res)
        return res

    @staticmethod
    def checkVacancy(req, res):
        """"check device umbrella rent available"""
        # get url variable
        device_id = req.url_variable['device_id']
        
        # check vacancies
        umbrella_amount = umbrellasModel.checkAmount(device_id) 

        # check amount
        vacancy = True if umbrella_amount < 5 else False

        # make response
        res.message = 'Check device umbrella return successfully.'
        res.data    = {
            'vacancy' : vacancy
        }
        return res
    
    @staticmethod
    def success(req, res):
        # get url variable
        device_id = req.url_variable['device_id']

        # get request data
        data = req.get_json()
        
        rfid    = data['rfid']
        
        # check umbrella rfid
        rent_reocrd = rentsModel.find_by_rfid(rfid)
        del rent_reocrd['_id']
        user_id = rent_reocrd['user_id']

        # need to rfid user_id, rent_device_id, return_device_id
        return_item = {
            'return_device_id' : device_id
        }

        # update rrs rent table
        res = urrs.update(req, res)

        # update umbrella status id
        umbrellasModel.update(rfid, {'status_id': device_id})

        rent_data = rentsModel.update(rent_reocrd['public_id'], return_item)
        del rent_data['_id']

        res.message = 'Return umbrella successfully.'
        res.data    = rent_data
        return res