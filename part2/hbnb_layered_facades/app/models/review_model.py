from app.models.base_model import BaseEntity

class Review(BaseEntity):
    def __init__(self, text, rating, place_id, user_id):
        super().__init__()
        self.text = text
        self.rating = rating
        self.place_id = place_id
        self.user_id = user_id
        
    def format_validation(self):
        if type(self.rating) is not int:
            return None        
        return self