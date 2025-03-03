from app.persistence.gateways.place_gateway import PlaceGateway
from app.models.place_model import Place
from app.services.exception import InvalidPlaceData, PlaceNotFound

class PlaceFacade:
    def __init__(self):
        self.gateway = PlaceGateway()
    
    def create_place(self, place_data):
        place = Place(**place_data)
        verif = place.format_validation()
        if not verif:
            raise InvalidPlaceData
        return self.gateway.add(place)

    def get_all_places(self):
        places = self.gateway.get_all()
        return [
            {
                'id': place.id,
                'title': place.title,
                'latitude': place.latitude,
                'longitude': place.longitude
            }
            for place in places
        ]
    
    def get(self, place_id):
        place = self.gateway.get(place_id)
        if place is None:
            raise PlaceNotFound
        return place
    
    def update_place(self, place_id, place_data):
        # retreive place updating his profile
        updating_place = self.gateway.get_by_attribute('id', place_id)
        if not updating_place:
            raise PlaceNotFound
        updating_place.update(place_data)
        # checking format validation before writing into storage
        verif = updating_place.format_validation()
        if not verif:
            raise InvalidPlaceData
        return self.gateway.update(place_id, place_data)