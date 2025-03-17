from utils.decoders.decoder import Decoder
from typing import Type,TypeVar,Generic,Union
from models.basic_types.basic_type import BasicObject 

T=TypeVar('T',bound=BasicObject)
class DbRecordDecoder(Decoder[T,Union[tuple,dict]],Generic[T]):
    
    @staticmethod
    def _validate_data(data:Union[tuple,dict]):
        if (data is None or len(data) == 0):
            return False
        return True
    
    @staticmethod   
    def decode(data:Union[tuple,dict],target_class:Type[T])->T:
        if(not Decoder._validate_data(data)):
            raise ValueError("not validate")
        try:
            if(isinstance(data,tuple)):
                return target_class(*data)
            elif(isinstance(data,dict)):
                return target_class(**data)
        except Exception as e:
            raise Exception(f"Error decoding string: {e}")    