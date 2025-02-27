from app.persistence.gateways.repository import InMemoryRepository


class AmenityGateway(InMemoryRepository):
    def __init__(self):
        super().__init__()

    def amenity_exists(self, amenity):
        return self.get_by_attribute('amenity', amenity)

    def add(self, obj):
        self._storage[obj.id] = obj
        return obj