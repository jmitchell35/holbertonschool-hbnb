from app.models.base_model import SQLBaseModel
from app import db

class Review(SQLBaseModel):
    __tablename__ = 'reviews'

    text = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Integer, nullable=False)

    def __init__(self, text, rating, place_id, user_id):
        self.text = text
        self.rating = rating
        self.place_id = place_id
        self.user_id = user_id
    
    def update(self, data=None):
        if not data:
            return self
        updatable_attr = ['text', 'rating']
        for key in data:
            if key in updatable_attr:
                setattr(self, key, data[key])
        return self