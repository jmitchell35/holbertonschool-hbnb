from app.models.base_model import BaseEntity

class User(BaseEntity):
    def __init__(self, first_name, last_name, email, is_admin=False):
        super().__init__()
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.is_admin = is_admin
        self.reviews = []
        self.places = []

    def add_review(self, review):
        """Written review by the user."""
        self.reviews.append(review)

    def add_places(self, place):
        """Add a place to the user."""
        self.places.append(place)
        
    def format_validation(self):
        from email_validator import validate_email, EmailNotValidError
        
        if type(self.first_name) is not str or\
            type(self.last_name) is not str:
            return None
        if len(self.first_name) > 50 or len(self.last_name) > 50:
            return None
        if type(self.is_admin) is not bool:
            return None

        try:
            emailinfo = validate_email(self.email, check_deliverability=True)
            self.email = emailinfo.normalized
            return self
        except (EmailNotValidError, AttributeError):
            return None
        
    def update(self, data):
        super().update()
        updatable_attr = ['first_name', 'last_name', 'email']
        for key in data:
            if key in updatable_attr:
                self.key = data[key]