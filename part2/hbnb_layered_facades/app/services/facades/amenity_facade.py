from app.persistence.gateways.amenity_gateway import AmenityGateway
from app.services.facades import BaseFacade

class AmenityFacade(BaseFacade):
    def __init__(self):
        self.gateway = AmenityGateway()