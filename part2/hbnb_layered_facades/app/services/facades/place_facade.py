from app.persistence.gateways.place import PlaceGateway
from app.services.facades import BaseFacade

class PlaceFacade(BaseFacade):
    def __init__(self):
        self.gateway = PlaceGateway()