from app.models.base_model import BaseModel

class User(BaseModel):
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