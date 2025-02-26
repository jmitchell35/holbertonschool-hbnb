from app.persistence.gateways.place_gateway import PlaceGateway
from app.models.place_model import Place

class PlaceFacade:
    def __init__(self):
        self.gateway = PlaceGateway()