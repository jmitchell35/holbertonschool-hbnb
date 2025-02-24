from app.persistence.gateways.review_gateway import ReviewGateway
from app.services.facades import BaseFacade

class AmenityFacade(BaseFacade):
    def __init__(self):
        self.gateway = ReviewGateway()