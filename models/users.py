
class usersSchema():
    users = {
        'ef8697123': {
            'name'      : '王小明',
            'email'     : 'dummy@gmail.com',
            'subscriber': True,
            'admin'     : True
        },
        'bs9435451': {
            'name'      : '歐絣康',
            'email'     : 'dummy2@gmail.com',
            'subscriber': False,
            'admin'     : False
        }
    }

    @staticmethod
    def find( public_id):
        data = usersSchema.users[public_id] if public_id in usersSchema.users else None
        return data
    
    @staticmethod
    def find_all():
        return usersSchema.users