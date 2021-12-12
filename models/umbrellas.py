
class umbrellasSchema():
    umbrellas = {
    }

    def find(public_id):
        data = umbrellasSchema.umbrellas[public_id] if public_id in umbrellasSchema.umbrellas else None
        return data
    
    def find_all():
        return umbrellasSchema.umbrellas