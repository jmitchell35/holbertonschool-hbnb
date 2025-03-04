from app.persistence.gateways.repository import InMemoryRepository


class UserGateway(InMemoryRepository):
    def __init__(self):
        super().__init__()

    def add(self, obj):
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