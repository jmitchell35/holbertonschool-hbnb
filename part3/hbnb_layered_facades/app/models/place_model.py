from app.models.base_model import SQLBaseModel
from app import db
from app.models.associations import place_amenity

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

    amenities = db.relationship(
        'Amenity',
        secondary=place_amenity,
        lazy='subquery',
        back_populates='places'
    )

    def __init__(self, title, description, price, latitude, longitude,
                 owner_id):
        self.title = title
        self.description = description
        self.price = price
        self.latitude = latitude
        self.longitude = longitude
        self.owner_id = owner_id
        # Constructor doesn't need to set relation. w. Am, re, SQLalchemy does

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
