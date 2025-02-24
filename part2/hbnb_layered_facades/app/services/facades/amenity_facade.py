from app.persistence.repository import InMemoryRepository
from app.services.facades import BaseFacade

class AmenityFacade(BaseFacade):
    def __init__(self):
        self.gateway = InMemoryRepository()