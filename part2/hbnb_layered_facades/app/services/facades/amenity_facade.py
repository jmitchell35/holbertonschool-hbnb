from app.persistence.gateways.amenity_gateway import AmenityGateway
from app.services.facades import BaseFacade
from app.models.amenity_model import Amenity

class AmenityFacade(BaseFacade):
    def __init__(self):
        self.gateway = AmenityGateway()