from app.persistence.gateways.repository import InMemoryRepository

class PlaceGateway(InMemoryRepository):
    def __init__(self):
        super().__init__()

    def add(self, obj):
        if obj.id in self._storage:
            raise ValueError("An object with this ID already exists")

        self._storage[obj.id] = obj
        return obj
    
    def update(self, obj_id, data):
        obj = self.get(obj_id)
        if obj:
            obj.update(data)
            return obj
        return None
    
    def delete_review(self, obj, review_id):
        (obj.reviews).remove(review_id)
        return obj