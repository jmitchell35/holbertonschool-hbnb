from app.services.facades.user_facade import UserFacade
from app.services.facades.place_facade import PlaceFacade
from app.services.facades.review_facade import ReviewFacade
from app.services.facades.amenity_facade import AmenityFacade

class HBnBFacade:
    def __init__(self):
        self.users = UserFacade()
        self.places = PlaceFacade()
        self.reviews = ReviewFacade()
        self.amenities = AmenityFacade()

    # Placeholder method for creating a user
    def create_user(self, user_data):
        # Logic will be implemented in later tasks
        pass

    # Placeholder method for fetching a place by ID
    def get_place(self, place_id):
        # Logic will be implemented in later tasks
        pass