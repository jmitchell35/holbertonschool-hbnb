from app.persistence.gateways.repository import InMemoryRepository


class UserGateway(InMemoryRepository):
    def __init__(self):
        super().__init__()

    def email_exists(self, email):
        # checks storage for existing email
        return self.get_by_attribute('email', email) is not None