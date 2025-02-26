from app.persistence.gateways.review_gateway import ReviewGateway
from app.models.review_model import Review

class ReviewFacade:
    def __init__(self):
        self.gateway = ReviewGateway()