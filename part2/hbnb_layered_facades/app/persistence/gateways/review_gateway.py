from app.persistence.gateways.repository import InMemoryRepository
from app.models.user_model import User

class ReviewGateway(InMemoryRepository):
    def __init__(self):
        super().__init__()
        
    def add(self, obj):
        self._storage[obj.id] = obj
        return obj