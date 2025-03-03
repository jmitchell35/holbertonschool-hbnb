from app.services.exception import (UserNotFound, PlaceNotFound,
                                    InvalidReviewData)

class ReviewWorkflowManager:
    def __init__(self, place_facade, user_facade, review_facade):
        self.place_facade = place_facade
        self.user_facade = user_facade
        self.review_facade = review_facade
    
    def create_review(self, data):
        try:
            self.user_facade.get(data['user_id'])
            self.place_facade.get(data['place_id'])
            return self.review_facade.create_review(data)
        except UserNotFound:
            raise UserNotFound
        except PlaceNotFound:
            raise InvalidReviewData