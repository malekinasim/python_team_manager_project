from utils.repositories.storage import Storage
from typing import TypeVar, Generic
from models.basic_types.basic_type import BasicObject

T = TypeVar('T', bound=BasicObject)

class BasicManager(Generic[T]):
    def __init__(self, storage: Storage[T]):
        self._storage = storage

    def get_storage(self):
        return self._storage

    def find_by_id(self, id):
        return self._storage.find_by_id(id)

    def save_entity(self, entity):
        self._storage.save_entity(entity)

    def find_all(self):
        return self._storage.find_all()

    def remove_entity(self, id):
        self._storage.delete_by_id(id) 

    def update_entity(self, entity):
        self._storage.update_entity(entity)   
    

    
    
    
    
    

