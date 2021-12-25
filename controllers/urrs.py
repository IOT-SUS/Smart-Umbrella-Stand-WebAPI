from app import app
from models.rrs import rrsModel

class urrs():
    @staticmethod
    def addRent(req, res):
        # get url variable
        device_id = req.url_variable['device_id']
        # get user id
        user_id = req.user_id

        returner_status = {
            'action'    : '0',
            'status'    : 'S0',
            'user_id'   : user_id,
            'device_id' : device_id
        }

        # insert renter_status to mongoDB
        rrs_data = rrsModel.add(returner_status)
        del rrs_data['_id']

        # make response
        res.message = 'Create rrs table of returner status successfully.'
        res.data    = rrs_data
        return res
    
    @staticmethod
    def addReturn(req, res):
        # get url variable
        device_id = req.url_variable['device_id']
        # get user id
        user_id = req.user_id

        renter_status = {
            'action'    : '1',
            'status'    : 'S0',
            'user_id'   : user_id,
            'device_id' : device_id
        }

        # insert renter_status to mongoDB
        rrs_data = rrsModel.add(renter_status)
        del rrs_data['_id']

        # make response
        res.message = 'Create rrs table of renter status successfully.'
        res.data    = rrs_data
        return res

    @staticmethod
    def info(req, res):
        # get url variable
        rrs_id = req.url_variable['rrs_id']
        
        # not done yet, this is for future work
        rrs_data = rrsModel.find(rrs_id)
        del rrs_data['_id']        

        # make response
        res.message = 'Get rrs information successfully.'
        res.data    = rrs_data
        return res

    @staticmethod
    def update(req, res):
        # get request data
        data = req.get_json()
        
        rrs_id = data['rrs_id']

        # not done yet, this is for future work
        test = rrsModel.find(rrs_id)
        
        updating = {
            'status' : 'S1'
        }

        rrsModel.update(rrs_id, updating)

        # make response
        res.message = 'Updating rrs successfully.'
        return res

    @staticmethod
    def devicePolling(req, res):
        # get url variable
        device_id = req.url_variable['device_id']
        action    = req.url_variable['action']

        # find by device_id & action
        rrs_data = rrsModel.find_by_device(device_id, action, 'S0')
        del rrs_data['_id']

        # make response
        res.data = rrs_data
        res.message = 'Device polling successfully, action: ' + action
        return res

    @staticmethod
    def userPolling(req, res):
        # get url variable
        user_id = req.user_id
        action  = req.url_variable['action']
        
        # find by device id
        rrs_data = rrsModel.find_by_user(user_id, action, 'S0')
        del rrs_data['_id']
        
        # make response
        res.data = rrs_data
        res.message = 'User polling successfully, action: ' + action
        return res
