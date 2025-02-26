from app.persistence.gateways.user_gateway import UserGateway
from app.services.facades import BaseFacade
from app.models.user_model import User

class UserFacade(BaseFacade):
    def __init__(self):
        self.gateway = UserGateway()
    
    def create_user(self, user_data):
        if self.gateway.email_exists(user_data['email']):
            return {'error': 'Email already registered'}, 400
        
        user = User(**user_data)
        return self.gateway.add(user)