from app.persistence.repository import InMemoryRepository
from app.services.facades import BaseFacade

class ReviewFacade(BaseFacade):
    def __init__(self):
        self.gateway = InMemoryRepository()