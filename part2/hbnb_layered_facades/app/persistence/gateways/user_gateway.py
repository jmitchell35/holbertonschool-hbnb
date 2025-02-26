from app.persistence.gateways.repository import InMemoryRepository


class UserGateway(InMemoryRepository):
    def __init__(self):
        super().__init__()

    def add(self, obj):
        self._storage[obj.id] = obj
        return obj
    
    def update(self, data):
        obj = self._storage.get(data.id)
        if obj:
            obj.update(data)
        updated_user = self.add(obj)
        return updated_user
        
    def email_exists(self, email):
        return self.get_by_attribute('email', email)