from app.persistence.gateways.amenity_gateway import AmenityGateway
from app.models.amenity_model import Amenity

class AmenityFacade:
    def __init__(self):
        self.gateway = AmenityGateway()