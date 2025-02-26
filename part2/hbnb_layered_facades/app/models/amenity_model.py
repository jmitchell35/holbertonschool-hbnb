from app.models.base_model import BaseEntity

class Amenity(BaseEntity):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.places = []
    
    def add_places(self, place):
        self.places.append(place)