from app.services.exception import (UserNotFound, PlaceNotFound,
                                    InvalidReviewData)

class ReviewWorkflowManager:
    def __init__(self, place_facade, user_facade, review_facade):
        self.place_facade = place_facade
        self.user_facade = user_facade
        self.review_facade = review_facade
    
    def create_review(self, data):
        try:
            user = self.user_facade.get(data['user_id'])
            self.place_facade.get(data['place_id'])
            new_review = self.review_facade.create_review(data)
            self.place_facade.update_place(data['place_id'],
                                     {'reviews': [new_review.id]})
            self.user_facade.update_user(user, {'reviews': [new_review.id]})
            return new_review
        except UserNotFound:
            raise UserNotFound
        except PlaceNotFound:
            raise InvalidReviewData
        
    def get_reviews_by_place(self, place_id):
        try:
            self.place_facade.get(place_id)
            return 
        except PlaceNotFound:
            raise PlaceNotFound