from app.services.exception import (UserNotFound, PlaceNotFound,
                                    InvalidReviewData, ReviewNotFound)

class ReviewWorkflowManager:
    def __init__(self, place_facade, user_facade, review_facade):
        self.place_facade = place_facade
        self.user_facade = user_facade
        self.review_facade = review_facade
    
    # A revoir lors de l'implémentation DB
    def create_review(self, data):
        try:
            user = self.user_facade.get(data['user_id'])
            self.place_facade.get(data['place_id'])
            new_review = self.review_facade.create_review(data)
            self.place_facade.update_place(data['place_id'],
                                     {'reviews': [new_review.id]})
            self.user_facade.update_user(user,
                                         {'reviews': [new_review.id]})
            return new_review
        except UserNotFound:
            raise UserNotFound
        except (PlaceNotFound, InvalidReviewData):
            raise InvalidReviewData

    def get_reviews_by_place(self, place_id):
        try:
            reviews = (self.place_facade.get(place_id)).reviews
            reviews_list=[]
            for review in reviews:
                reviews_list.append(self.review_facade.get(review))
            return reviews_list
        except PlaceNotFound:
            raise PlaceNotFound
    
    # A revoir lors de l'implémentation DB
    def delete_review(self, review_id):
        try:
            review = self.review_facade.get(review_id)
            self.user_facade.delete_review(review_id, review.user_id)
            self.place_facade.delete_review(review_id, review.place_id)
            self.review_facade.delete_review(review_id)
            return {"message": "Review deleted successfully"}, 200
        except ReviewNotFound:
            raise ReviewNotFound