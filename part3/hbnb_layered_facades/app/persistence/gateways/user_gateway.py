from app.persistence.gateways.repository import SQLAlchemyRepository
from app import db


class UserGateway(SQLAlchemyRepository):
    def __init__(self):
        from app.models.user_model import User
        super().__init__(User)


    def delete_review(self, obj, review_id):
        (obj.reviews).remove(review_id)
        return obj

    def delete_place(self, owner, place_id):
        owner.places.remove(place_id)
        return owner
