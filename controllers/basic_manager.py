from utils.repositories.storage import Storage
from typing import TypeVar, Generic
from models.basic_types.basic_type import BasicObject

T = TypeVar('T', bound=BasicObject)

class BasicManager(Generic[T]):
    def __init__(self, storage: Storage[T]):
        self.__storage = storage

    def find_by_id(self, id):
        return self.__storage.find_by_id(id)
    
    def find_last_membership_Fee(self,dict_properties:dict)->T:
        raise NotImplementedError("subclass should implement this method")

    def save_entity(self, entity):
        self.__storage.save_entity(entity)

    def find_all(self):
        return self.__storage.find_all()

    def remove_entity(self, id):
        self.__storage.delete_by_id(id) 

    def update_entity(self, entity):
        self.__storage.update_entity(entity) 
    
        
    def  find_all_by_properties(self,dict_properties:dict)->list[T]:
        return self.__storage.find_all_by_properties(dict_properties) 
    

    
    
    
    
    

