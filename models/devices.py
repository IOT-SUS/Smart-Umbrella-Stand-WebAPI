
class devicesSchema():
    devices = {
        'sdfe297123' : {
            'location': '台北市文山區汀州路四段88號',
            'amount'  : 10
        },
        'ddcd291217' : {
            'location': '台北市大安區和平東路一段162號',
            'amount'  : 0
        }
    }

    def find(public_id):
        data = devicesSchema.devices[public_id] if public_id in devicesSchema.devices else None
        return data
    
    def find_all():
        return devicesSchema.devices