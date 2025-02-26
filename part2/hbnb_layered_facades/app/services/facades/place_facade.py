from app.persistence.gateways.place_gateway import PlaceGateway
from app.services.facades import BaseFacade
from app.models.place_model import Place

class PlaceFacade(BaseFacade):
    def __init__(self):
        self.gateway = PlaceGateway()