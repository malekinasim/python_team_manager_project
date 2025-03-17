from utils.decoders.decoder import Decoder
from typing import Type,Generic,TypeVar
from models.basic_types.basic_type import BasicObject

T=TypeVar('T',bound=BasicObject)
class StringDecoder(Decoder[T,str],Generic[T]):
    
    @staticmethod
    def _validate_data(code:str)->bool:
        if (code is None or code.strip()==''):
            return False
        return True
    
    @staticmethod
    def decode(code:str, target_class: Type[T]) -> T:
        if(not StringDecoder._validate_data(code)  ):
            raise ValueError("Data is not a string")
        try:
            
            object=target_class.decode_entity(code)
            return object
        except Exception as e:
            raise Exception(f"Error decoding string: {e}")    