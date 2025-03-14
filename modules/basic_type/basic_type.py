from datetime import datetime
import uuid
class BasicType:
    def __init__(self):
        self.set_id()
        self._create_date=datetime.now()
        self._update_date=datetime.now()
        
    def set_id(self):
        self._id=uuid.uuid4()
    
    def get_id(self):
        return self._id
    
    def get_create_Date(self):
        return self._create_date
    
    def get_create_Date(self):
        return self._update_date
    
    