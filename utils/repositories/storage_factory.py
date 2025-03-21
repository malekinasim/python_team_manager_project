from utils.repositories.storage_type import StorageType
from utils.repositories.storage import Storage
from typing import TypeVar,Generic
from models.basic_types.basic_type import BasicObject

T = TypeVar('T', bound=Storage)
U=TypeVar("U", bound=BasicObject)
class StorageFactory(Generic[T,U]): 
    '''this is a generic interface for storage'''
    __instances={}
    # Constructor for singleton subclass it's support that one instance of each decoder subclass is created
       
    @staticmethod
    def getStorage(storage_name,config: dict,entity_class:U)->T:
        storage_class=StorageType.get_by_name(storage_name)
        if( storage_class is None or config is None):
            raise ValueError("invalid storage type or configuration provided")
        return StorageFactory.__get_instance(storage_class,config,entity_class)
    
    @staticmethod
    def __get_instance(storage_class, config: dict, entity_class: U):
        key = (storage_class, entity_class)
        if key not in StorageFactory.__instances:
            StorageFactory.__instances[key] = storage_class.create_instance(config, entity_class)
        return StorageFactory.__instances[key]