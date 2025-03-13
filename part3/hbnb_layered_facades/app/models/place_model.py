from app.models.base_model import SQLBaseModel
from app import db

class Place(SQLBaseModel):
    __tablename__ = 'places'

    title = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)

    def __init__(self, title, description, price, latitude, longitude, owner_id, amenities=[]):
        self.title = title
        self.description = description
        self.price = price
        self.latitude = latitude
        self.longitude = longitude
        self.owner_id = owner_id
        self.amenities = amenities
        self.reviews = []  # List to store related reviews

    # A revoir
    def add_review(self, review):
        """Add a review to the place."""
        self.reviews.append(review)

    # A revoir
    def add_amenity(self, amenity):
        """Add an amenity to the place."""
        self.amenities.append(amenity)
    
    def update(self, data=None):
        if not data:
            return self
        updatable_attr = ['title', 'description', 'price', 'latitude',
                          'longitude', 'amenities']
        for key in data:
            if key in updatable_attr:
                setattr(self, key, data[key])
        if 'places' in data.keys():
            for place in data['places']:
                self.reviews.append(place)
        if 'reviews' in data.keys():
            for review in data['reviews']:
                self.reviews.append(review)
        return self
