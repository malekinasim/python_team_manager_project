from datetime import datetime
import uuid
from abc import ABC, abstractmethod
class BasicObject(ABC):
    def __init__(self,code,created_date,id=uuid.uuid4() ): 
        self._id=id 
        self._set_code(code)
        self._created_date=created_date
        
    def _set_code(self,code):
        if(code is None):
            raise ValueError("the team name is required")   
        self._code=code
    
    def get_id(self):
        return self._id
    
    def get_created_date(self):
        return self._created_date
        
    @abstractmethod
    def code_entity(self):
        pass
    
    @staticmethod
    def get_table_name():
        raise NotImplementedError("Subclasses should implement this!")
    

    @staticmethod
    def get_id_column_name():
        raise NotImplementedError("Subclasses should implement this!")
    
    @staticmethod
    def decode_entity(str):
        raise NotImplementedError("Subclasses should implement this!")
    
    @staticmethod
    def format_columns(*args,sep,ljust=0):
        return sep.join(str(arg).ljust(ljust) if ljust else str(arg) for arg in args)