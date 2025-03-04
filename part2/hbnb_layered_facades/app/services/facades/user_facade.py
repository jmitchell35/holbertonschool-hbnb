from app.persistence.gateways.user_gateway import UserGateway
from app.models.user_model import User
from app.services.exception import (EmailAlreadyExists, InvalidUserData,
                                    UserNotFound, ReviewNotFound)

class UserFacade:
    def __init__(self):
        self.gateway = UserGateway()
    
    def create_user(self, user_data):
        if self.gateway.email_exists(user_data['email']):
            raise EmailAlreadyExists

        user = User(**user_data)
        verif = user.format_validation()
        if not verif:
            raise InvalidUserData
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

    def update_user(self, user, user_data):
        # retreive user updating his profile
        updating_user = self.gateway.get_by_attribute('id', user.id)
        if not updating_user:
            raise UserNotFound
        # retreiving user associated with email if any
        if 'email' in user_data.keys():
            existing_email = self.gateway.get_by_attribute(
                'email', user_data['email'])
        
            if existing_email and updating_user.id != existing_email.id:
                raise EmailAlreadyExists

        # Either email is not registered, or registered email matches user
        updating_user.update(user_data)
            
        # checking format validation before writing into storage
        verif = updating_user.format_validation()
        if not verif:
            raise InvalidUserData
        return verif
            
    def get(self, user_id):
        user = self.gateway.get(user_id)
        if user is None:
            raise UserNotFound
        return user
    
    def delete_review(self, review_id, user_id):
        user = self.get(user_id)
        self.gateway.delete_review(user, review_id)
        if review_id in user.reviews:
            raise ReviewNotFound
        return user