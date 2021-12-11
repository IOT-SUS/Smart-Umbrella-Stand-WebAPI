from app import app

class ureturn():
    @staticmethod
    def checkAvailable(req, res):
        """"check device umbrella rent available"""
        # get url variable
        device_id = req.url_variable['device_id']
        
        # search device by id
        fake_devices = {
            'sdfe297123' : {
                'location': '台北市文山區汀州路四段88號',
                'amount'  : 10
            },
            'ddcd291217' : {
                'location': '台北市大安區和平東路一段162號',
                'amount'  : 0
            }
        }

        assert device_id in fake_devices

        # check amount
        available = True if fake_devices[device_id]['amount'] < 15 else False

        # make response
        res.message = 'Check device umbrella return successfully.'
        res.data    = {
            'available' : available
        }
        return res