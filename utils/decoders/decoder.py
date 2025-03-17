from typing import TypeVar, Generic,Type,Union
from models.basic_types.basic_type import BasicObject


T=TypeVar('T',bound=BasicObject)
U=TypeVar('U',bound=Union[str,tuple,dict])
class Decoder(Generic[T,U]): 
    
    @classmethod
    def _create_instance(cls,entity_class:T):
        raise NotImplementedError("Subclasses should implement this!")
    
    @staticmethod
    def _validate_data(code:U) -> bool:
        raise NotImplementedError("Subclasses should implement this!")

    @staticmethod
    def decode(code:str, target_class: Type[T]) -> T:
        raise NotImplementedError("Subclasses should implement this!")