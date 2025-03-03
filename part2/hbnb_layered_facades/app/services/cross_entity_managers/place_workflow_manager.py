from app.services.exception import (UserNotFound, InvalidPlaceData,
                                    OwnerNotFound, PlaceNotFound,
                                    AmenityNotFound)

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
            # Alternative
            # amenity_list = [{'id': obj.id, 'name': obj.name} 
                # for id in place.amenities
                # if (obj := self.amenity_facade.get(id))] (walrus operator)
            return {
                'id': place.id,
                'title': place.title,
                'description': place.description,
                'price': place.price,
                'latitude': place.latitude,
                'longitude': place.longitude,
                'owner_id': place.owner_id,
                'owner': {
                    'id': owner.id,
                    'first_name': owner.first_name,
                    'last_name': owner.last_name,
                    'email': owner.email
                },
                'amenities': amenity_list,
                'reviews': place.reviews
            }
        except PlaceNotFound:
            raise PlaceNotFound
        except UserNotFound:
            raise OwnerNotFound
        except AmenityNotFound:
            raise AmenityNotFound
        
    def update_place(self, place_id, place_data):
        try:
            if 'amenities' in place_data.keys():
                for id in place_data['amenities']:
                    self.amenity_facade.get(id)
            return self.place_facade.update_place(place_id, place_data)
        except PlaceNotFound:
            raise PlaceNotFound
        except (AmenityNotFound, InvalidPlaceData):
            raise InvalidPlaceData