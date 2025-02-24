from app.persistence.gateways.place import PlaceGateway
from app.services.facades import BaseFacade

class AmenityFacade(BaseFacade):
    def __init__(self):
        self.gateway = PlaceGateway()