from models.basic_types.basic_type import BasicObject
from typing import TypeVar,Generic
'''creating Generic type for the storage interface to
    accept any type of data that is a subclass of basic_type
    creating a generic type variable T that is bound to basic_type'''

T=TypeVar("T", bound=BasicObject)


class Storage(Generic[T]):
    
    @classmethod
    def _create_instance(cls, config: dict,entity_class:T):
        raise NotImplementedError("Subclasses should implement this!")
  
    @classmethod 
    def save_entity(cls, data:T):
        raise NotImplementedError("Subclasses should implement this!")
    
 
    @classmethod
    def update_entity(cls, data:T):
        raise NotImplementedError("Subclasses should implement this!")
    
    
    @classmethod
    def find_all(cls)->list[T]:
        raise NotImplementedError("Subclasses should implement this!")
    
    @classmethod
    def find_all_by_properties(cls,filter: dict)->list[T]:
        raise NotImplementedError("Subclasses should implement this!")

    @classmethod
    def delete_by_id(cls, id):
        raise NotImplementedError("Subclasses should implement this!")
    
    @classmethod
    def find_by_id(cls, id)->T:
        raise NotImplementedError("Subclasses should implement this!")
    
    