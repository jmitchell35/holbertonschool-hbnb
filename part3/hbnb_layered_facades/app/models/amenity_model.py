from app.models.base_model import BaseEntity

class Amenity(BaseEntity):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.places = []
    
    def add_places(self, place):
        self.places.append(place)

    def update(self, data=None):
        super().update()
        if not data:
            return self
        updatable_attr = ['name']
        for key in data:
            if key in updatable_attr:
                setattr(self, key, data[key])
        return self