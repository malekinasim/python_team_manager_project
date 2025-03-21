from utils.decoders.decoder import Decoder
from typing import Type,TypeVar,Generic,Union
from models.basic_types.basic_type import BasicObject 

T=TypeVar('T',bound=BasicObject)
class DbRecordDecoder(Decoder[T,tuple],Generic[T]):
        
    @staticmethod
    def __validate_data(row:Union[tuple,dict])->bool:
        if (row is None or len(row) == 0):
            return False
        return True
    
    @staticmethod   
    def decode(row:Union[tuple,dict],target_class:Type[T])->T:
        if(not DbRecordDecoder.__validate_data(row)):
            raise ValueError("not validate")
        try:
            if(isinstance(row,tuple)):
                return target_class(*row)
            elif(isinstance(row,dict)):
                return target_class(**row)
        except Exception as e:
            raise Exception(f"Error decoding string: {e}")    