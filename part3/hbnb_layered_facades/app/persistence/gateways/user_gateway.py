from app.persistence.gateways.repository import InMemoryRepository


class UserGateway(InMemoryRepository):
    def __init__(self):
        super().__init__()
        from app.models.user_model import User
        user = User('Admin', 'Admin', 'admin@gmail.com', 'password', True)
        self.add(user)

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

    def delete_place(self, owner, place_id):
        owner.places.remove(place_id)
        return owner
