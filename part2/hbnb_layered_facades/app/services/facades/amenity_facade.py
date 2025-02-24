from app.persistence.gateways.amenity import AmenityGateway
from app.services.facades import BaseFacade

class AmenityFacade(BaseFacade):
    def __init__(self):
        self.gateway = AmenityGateway()