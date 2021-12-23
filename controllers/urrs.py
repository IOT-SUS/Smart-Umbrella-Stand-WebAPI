from re import I
from app import app
from models.rrs import rrsModel
from models.umbrellas import umbrellasModel

class urrs():
    @staticmethod
    def device_polling(req, res):
        # get url variable
        device_id = req.url_variable['device_id']
        action = req.url_variable['action']

        # find by device_id & action
        rrs_item = rrsModel.find_by_device(device_id, action, 'S0')
        
        # delete the '_id' thing
        del rrs_item['_id']

        # make response
        res.data = rrs_item
        res.message = 'Device polling successfully, action: ' + action
        return res

    @staticmethod
    def user_polling(req, res):
        # get url variable
        user_id    = req.url_variable['user_id']
        action  = req.url_variable['action']
        
        # find by device id
        rrs_item = rrsModel.find_by_user(user_id, action, 'S0')
        
        # delete the '_id' thing
        del rrs_item['_id']
        
        # make response
        res.data = rrs_item
        res.message = 'User polling successfully, action: ' + action
        return res

    @staticmethod
    def device_updating_rrs(req, res):
        # get url variable
        rrs_id = req.url_variable['rrs_id']
        
        # not done yet, this is for future work
        test = rrsModel.find(rrs_id)
        
        updating = {
            'status' : 'S1'
        }

        rrsModel.update(rrs_id, updating)

        # make response
        res.message = 'Device updating rrs successfully'
        return res