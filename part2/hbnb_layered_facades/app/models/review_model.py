from app.models.base_model import BaseEntity

class Review(BaseEntity):
    def __init__(self, text, rating, place, author):
        super().__init__()
        self.text = text
        self.rating = rating
        self.place = place
        self.author = author