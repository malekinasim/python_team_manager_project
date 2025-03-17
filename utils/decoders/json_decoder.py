import json
from utils.decoders.decoder import Decoder
from typing import Generic, TypeVar,Type
from models.basic_types.basic_type import BasicObject

T=TypeVar('T',bound=BasicObject)
class JsonDecoder(Decoder[T,str],Generic[T]):
    @staticmethod
    def _validate_data(code:str):
        if code is None or not isinstance(code, str) or not code.strip(): 
            return False
        
        try:
            json.loads(code)
        except json.JSONDecodeError:
            return False
        
        return True
    
    @staticmethod
    def decode(code:str, target_class: Type[T]) -> T:
        if not JsonDecoder._validate_data(code):
            raise ValueError("Invalid JSON data")
        
        json_data = json.loads(code)  
        try:
            obj = target_class(**json_data)
            return obj
        except Exception as e:
            raise Exception(f"Error decoding JSON data: {e}")
