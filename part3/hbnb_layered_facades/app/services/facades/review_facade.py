from app.persistence.gateways.review_gateway import ReviewGateway
from app.models.review_model import Review
from app.services.exception import InvalidReviewData, ReviewNotFound

class ReviewFacade:
    def __init__(self):
        self.gateway = ReviewGateway()
        
    def create_review(self, data):
        if self.is_valid(data) is not True:
            raise InvalidReviewData

        review = Review(**data)
        self.gateway.add(review)
        return review
    
    def get_all_reviews(self):
        reviews = self.gateway.get_all()
        return [
        {
                'id': review.id,
                'text': review.text,
                'rating': review.rating
        } 
        for review in reviews
    ]
    
    def get(self, review_id):
        review = self.gateway.get(review_id)
        if review is None:
            raise ReviewNotFound
        return review
    
    def update_review(self, review_id, review_data):
        # retreive place updating his profile
        review = self.gateway.get(review_id)
        if not review:
            raise ReviewNotFound
        # checking format validation before writing into storage
        if self.is_valid(review_data) is not True:
            raise InvalidReviewData

        review.update(review_data)
        return review
    
    # A revoir peut-être
    def delete_review(self, review_id):
        self.gateway.delete(review_id)
        return True
    
    def is_valid(self, data):
        if 'rating' in data.keys() and (type(data['rating']) is not int or
        data['rating'] < 1 or
        data['rating'] > 5):
            raise InvalidReviewData

        if 'text' in data.keys() and (type(data['text']) is not str or
                                      len(data['text']) < 2):
            raise InvalidReviewData

        return True