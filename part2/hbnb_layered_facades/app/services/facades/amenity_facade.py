from app.persistence.gateways.amenity_gateway import AmenityGateway
from app.models.amenity_model import Amenity
from app.services.exception import InvalidAmenityData, AmenityAlreadyExists, AmenityNotFound

class AmenityFacade:
    def __init__(self):
        self.gateway = AmenityGateway()

    def create_amenity(self, amenity_name):
        if self.gateway.amenity_exists(amenity_name['name']):
            raise AmenityAlreadyExists(f'Amenity {amenity_name['name']} is already registered')

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

        amenity = self.gateway.get(amenity_id)
        if amenity is None:
            raise AmenityNotFound
        return amenity
    
    def update_amenity(self, amenity, amenity_name):
        updating_amenity = self.gateway.get_by_attribute('id', amenity.id)
        if not updating_amenity:
            raise AmenityNotFound

        updating_amenity.update(amenity_name)

        verif = updating_amenity.format_validation()
        if not verif:
            raise InvalidAmenityData
        return self.gateway.update(amenity.id, amenity_name['name'])
