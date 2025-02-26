from app.persistence.gateways.user_gateway import UserGateway
from app.models.user_model import User

class UserFacade:
    def __init__(self):
        self.gateway = UserGateway()
    
    def create_user(self, user_data):
        if self.gateway.email_exists(user_data['email']):
            return {'error': 'Email already registered'}, 400
        
        user = User(**user_data)
        verif = user.format_validation()
        if not verif:
            return {'error': 'Invalid input data'}, 400
        written = self.gateway.add(user)
        return {'id': written.id, 'first_name': written.first_name, 'last_name': written.last_name, 'email': written.email}, 201
    
    def get_all_users(self):
        users = self.gateway.get_all()
        return [
        {
            'id': user.id, 
            'first_name': user.first_name, 
            'last_name': user.last_name, 
            'email': user.email,
            'is_admin': user.is_admin,
            'created at': user.created_at.isoformat(),
            'updated_at': user.updated_at.isoformat()
        } 
        for user in users
    ]
        
    def update_user(self, user_id, user_data):
        # 1 - retreive user
        # 2 - retreive user_id
        # 3 - check email existence - retreive existing_user correspondant
        # 4 - Si le mail existe, et que existing_user.id = user.id 
        # => Le user conserve son mail : pas de souci
        #   - Sinon, il veut enregistrer un mail qui correspond a un autre user
        # => impossible
        updating_user = self.gateway.get_by_attribute('id', user_id)
        existing_email = self.gateway.get_by_attribute(
            'email', user_data['email'])

        if not existing_email or updating_user.id == existing_email.id:
            updating_user = updating_user.update(user_data)
            verif = updating_user.format_validation()
            if not verif:
                return {'error': 'Invalid input data'}, 400
            written = self.gateway.update(updating_user)
            return {'id': written.id, 'first_name': written.first_name, 'last_name': written.last_name, 'email': written.email}, 200
        else:
            return {'error': 'Email already registered'}, 400