from app.persistence.gateways.review_gateway import ReviewGateway
from app.services.facades import BaseFacade
from app.models.review_model import Review

class AmenityFacade(BaseFacade):
    def __init__(self):
        self.gateway = ReviewGateway()