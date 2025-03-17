from utils.repositories.storage_type import StorageType
from utils.repositories.storage import Storage
from typing import TypeVar,Generic
from models.basic_types.basic_type import BasicObject

T = TypeVar('T', bound=Storage)
U=TypeVar("U", bound=BasicObject)
class StorageFactory(Generic[T,U]): 
    '''this is a generic interface for storage'''
    _instances={}
    # Constructor for singleton subclass it's support that one instance of each decoder subclass is created
       
    @staticmethod
    def getStorage(storage_name,config: dict,entity_class:U)->T:
        storage_class=StorageType.get_by_name(storage_name)
        if( storage_class is None or config is None):
            raise ValueError("invalid storage type or configuration provided")
        return StorageFactory._get_instance(storage_class,config,entity_class)
    
    
    @staticmethod
    def _get_instance(storage_class,config:dict,entity_class:U):
        '''this method is used to get the instance of the storage class if this storage  
        currently doesn't have any instance it will create one and return it otherwise 
        it will return the already created instance'''
        return StorageFactory._instances.setdefault((storage_class,entity_class),storage_class._create_instance(config,entity_class))
    