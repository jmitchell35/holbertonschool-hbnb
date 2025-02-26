from abc import ABC, abstractmethod
import uuid
from datetime import datetime

class BaseModel(ABC):
    @abstractmethod
    def __init__(self):
        pass
    
    @abstractmethod
    def update(self, data=None):
        pass
    
class BaseEntity(BaseModel):
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
    
    def update(self, data=None):
        self.updated_at = datetime.now()
        return self