from app.persistence.gateways.user_gateway import UserGateway
from app.models.user_model import User
from app.services.exception import EmailAlreadyExists, InvalidUserData

class UserFacade:
    def __init__(self):
        self.gateway = UserGateway()
    
    def create_user(self, user_data):
        if self.gateway.email_exists(user_data['email']):
            raise EmailAlreadyExists(f"Email {user_data['email']} is already registered")
        
        user = User(**user_data)
        verif = user.format_validation()
        if not verif:
            raise InvalidUserData("Invalid input data")
        written = self.gateway.add(user)
        return written
    
    def get_all_users(self):
        users = self.gateway.get_all()
        return [
        {
            'id': user.id, 
            'first_name': user.first_name, 
            'last_name': user.last_name, 
            'email': user.email
        } 
        for user in users
    ]
        
    def update_user(self, user_id, user_data):
        # retreive user updating his profile
        updating_user = self.gateway.get_by_attribute('id', user_id)
        # retreiving user associated with email if any
        existing_email = self.gateway.get_by_attribute(
            'email', user_data['email'])

        # Either email is not registered, or registered email matches user
        if not existing_email or updating_user.id == existing_email.id:
            updating_user.update(user_data)
            
            # checking format validation before writing into storage
            verif = updating_user.format_validation()
            if not verif:
                return {'error': 'Invalid input data'}, 400

            written = self.gateway.update(user_id, user_data)
            
            return {
                'id': written.id,
                'first_name': written.first_name,
                'last_name': written.last_name,
                'email': written.email
            }, 200
            
    def get(self, user_id):
        return self.gateway.get(user_id)