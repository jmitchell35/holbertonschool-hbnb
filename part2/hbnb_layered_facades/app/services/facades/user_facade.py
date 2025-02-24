from app.persistence.gateways.user_gateway import UserGateway
from app.services.facades import BaseFacade

class UserFacade(BaseFacade):
    def __init__(self):
        self.gateway = UserGateway()