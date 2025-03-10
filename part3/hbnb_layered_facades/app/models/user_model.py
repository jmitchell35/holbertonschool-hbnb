from app.models.base_model import BaseEntity

class User(BaseEntity):
    def __init__(self, first_name, last_name, email, is_admin=False):
        super().__init__()
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.is_admin = is_admin
        self.reviews = []
        self.places = []

    def add_review(self, review):
        """Written review by the user."""
        self.reviews.append(review)

    def add_places(self, place):
        """Add a place to the user."""
        self.places.append(place)
        
    def update(self, data=None):
        super().update()
        if not data:
            return self
        updatable_attr = ['first_name', 'last_name', 'email']
        for key in data:
            if key in updatable_attr:
                setattr(self, key, data[key])
        if 'reviews' in data.keys():
            for review in data['reviews']:
                self.reviews.append(review)
        if 'places' in data.keys():
            for place in data['placess']:
                self.places.append(place)
        return self