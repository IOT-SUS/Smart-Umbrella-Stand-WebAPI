from app import mongo

class umbrellasModel():
    umbrellas = {
    }

    def find(public_id):
        data = umbrellasModel.umbrellas[public_id] if public_id in umbrellasModel.umbrellas else None
        return data
    
    def find_all():
        return umbrellasModel.umbrellas