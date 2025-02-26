from app.persistence.gateways.repository import InMemoryRepository


class UserGateway(InMemoryRepository):
    def __init__(self):
        super().__init__()

    def add(self, obj):
        self._storage[obj.id] = obj
        return obj
    
    def update(self, user):
        self._storage[user.id] = user
        return user
        
    def email_exists(self, email):
        return self.get_by_attribute('email', email)