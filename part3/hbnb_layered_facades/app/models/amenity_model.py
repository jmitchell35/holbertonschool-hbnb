from app.models.base_model import SQLBaseModel
from app import db

class Amenity(SQLBaseModel):
    __tablename__ = 'amenities'

    name = db.Column(db.Text, nullable=False, unique=True)
    
    from app.models.place_model import place_amenity

    places = db.relationship('Place', secondary=place_amenity,
                             back_populates='amenities')
    
    def __init__(self, name):
        self.name = name
        self.places = []
    # A revoir
    def add_places(self, place):
        self.places.append(place)

    def update(self, data=None):
        if not data:
            return self
        updatable_attr = ['name']
        for key in data:
            if key in updatable_attr:
                setattr(self, key, data[key])
        return self