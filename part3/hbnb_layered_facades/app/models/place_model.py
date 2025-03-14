from app.models.base_model import SQLBaseModel
from app import db


place_amenity = db.Table('place_amenity',
                         db.Column('place_id', db.Integer,
                                   db.ForeignKey('places.id'), primary_key=True),
                         db.Column('amenity_id', db.Integer,
                                   db.ForeignKey('amenities.id'), primary_key=True)
                         )
class Place(SQLBaseModel):
    __tablename__ = 'places'

    title = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    owner_id = db.Column(db.String, db.ForeignKey('users.id'), nullable=False)

    owner = db.relationship('User', back_populates='places')
    reviews = db.relationship('Review', back_populates='place', lazy=True)

    amenities = db.relationship('Amenity', secondary=place_amenity, lazy='subquery',
                                back_populates='places')

    def __init__(self, title, description, price, latitude, longitude, owner_id, amenities=[]):
        self.title = title
        self.description = description
        self.price = price
        self.latitude = latitude
        self.longitude = longitude
        self.owner_id = owner_id
        self.amenities = amenities
        self.reviews = []  # List to store related reviews

    # encore utile ?
    def add_review(self, review):
        """Add a review to the place."""
        self.reviews.append(review)
        db.session.commit()

    def add_amenity(self, amenity):
        """Add an amenity to the place."""
        if amenity not in self.amenities:
            self.amenities.append(amenity)
        db.session.commit()
    
    def update(self, data=None):
        if not data:
            return self
        updatable_attr = ['title', 'description', 'price', 'latitude',
                          'longitude']
        for key in data:
            if key in updatable_attr:
                setattr(self, key, data[key])
        if 'amenities' in data:
            for amenity in data['amenities']:
                if amenity not in self.amenities:
                    self.amenities.append(amenity)
        db.session.commit()
        return self
