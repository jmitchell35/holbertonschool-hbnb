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
                'title': place.title,
                'description': place.description,
                'price': place.price,
                'latitude': place.latitude,
                'longitude': place.longitude,
                'owner_id': place.owner_id
            }
            for place in places
        ]
    
    def get(self, place_id):
        place = self.gateway.get(place_id)
        if place is None:
            raise PlaceNotFound
        return place