from app.services.exception import UserNotFound, InvalidPlaceData, OwnerNotFound, PlaceNotFound, AmenityNotFound

class PlaceWorkflowManager():
    def __init__(self, place_facade, user_facade, amenity_facade):
        self.place_facade = place_facade
        self.user_facade = user_facade
        self.amenity_facade = amenity_facade

    def create_place(self, place_data):
        try:
            self.user_facade.get(place_data['owner_id'])
            return self.place_facade.create_place(place_data)
        except UserNotFound:
            raise OwnerNotFound
        except InvalidPlaceData:
            raise InvalidPlaceData
    
    def get_place_details(self, place_id):
        try:
            place = self.place_facade.get(place_id)
            owner = self.user_facade.get(place.owner_id)
            amenity_list = []
            for id in place.amenities:
                obj = self.amenity_facade.get(id)
                amenity_list.append({
                    'id': obj.id,
                    'name': obj.name
                })
            return {
                'id': place.id,
                'title': place.title,
                'description': place.description,
                'latitude': place.latitude,
                'longitude': place.longitude,
                'owner': {
                    'id': owner.id,
                    'first_name': owner.first_name,
                    'last_name': owner.last_name,
                    'email': owner.email
                },
                'amenities': amenity_list
            }
        except PlaceNotFound:
            raise PlaceNotFound
        except UserNotFound:
            raise OwnerNotFound
        except AmenityNotFound:
            raise AmenityNotFound