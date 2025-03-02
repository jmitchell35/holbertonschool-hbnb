class PlaceWorkflowManager():
    def __init__(self, place_facade, user_facade, amenity_facade):
        self.place_facade = place_facade
        self.user_facade = user_facade
        self.amenity_facade = amenity_facade