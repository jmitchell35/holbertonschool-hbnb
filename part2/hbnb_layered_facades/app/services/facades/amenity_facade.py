from app.persistence.gateways.amenity_gateway import AmenityGateway
from app.models.amenity_model import Amenity
from app.services.exception import InvalidAmenityData

class AmenityFacade:
    def __init__(self):
        self.gateway = AmenityGateway()

    def create_amenity(self, amenity_name):
        amenity = Amenity(**amenity_name)
        verif = amenity.format_validation()
        if not verif:
            raise InvalidAmenityData('Invalid input data')
        written = self.gateway.add(amenity)
        return written
    
    def get_all_amenities(self):
        amenities = self.gateway.get_all()
        return [
        {
            'id': amenity.id,
            'name': amenity.name
        }
        for amenity in amenities
    ]

    def get(self, amenity_id):
        return self.gateway.get(amenity_id)
    
    def update_amenity(self, ):