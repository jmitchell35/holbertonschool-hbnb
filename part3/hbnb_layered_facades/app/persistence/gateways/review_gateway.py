from app.persistence.gateways.repository import SQLAlchemyRepository

class ReviewGateway(SQLAlchemyRepository):
    def __init__(self):
        from app.models.review_model import Review
        super().__init__(Review)
