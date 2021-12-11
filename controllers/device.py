from app import app

class device():
    @staticmethod
    def infos(req, res):
        """devices information"""
        # search all deviecs information
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

        # make response
        res.message = 'Get devices information successfully.'
        res.data    = fake_devices[device_id]
        return res