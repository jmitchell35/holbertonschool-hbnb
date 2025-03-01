from app.models.base_model import BaseEntity

class Place(BaseEntity):
    def __init__(self, title, description, price, latitude, longitude, owner_id):
        super().__init__()
        self.title = title
        self.description = description
        self.price = price
        self.latitude = latitude
        self.longitude = longitude
        self.owner_id = owner_id
        self.amenities = []
        self.reviews = []  # List to store related reviews

    def add_review(self, review):
        """Add a review to the place."""
        self.reviews.append(review)

    def add_amenity(self, amenity):
        """Add an amenity to the place."""
        self.amenities.append(amenity)
    
    def format_validation(self):
        if type(self.price) is not float:
            return None
        if self.price < 0.0:
            return None
        if self.latitude < -90.0 or self.latitude > 90.0:
            return None
        if self.longitude < -180.0 or self.longitude > 180.0:
            return None
        return self